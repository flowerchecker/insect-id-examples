from kindwise import InsectApi, SearchResult


# Search insect knowledge base by query. Entities are searchable by scientific names, common names (in specified
# language), synonyms. Insect name and query are always matched from start of a word., i.e. 'Harmonia axyridis' is
# searchable by 'Harmonia', 'Harmon', 'axyridis', 'axyrid', 'Harmonia axyridis'...

api = InsectApi('your_api_key')

insect_for_search = 'axyridis'
limit = 3        # int (optional) - maximum of returned result, max. 20, default 10
language = 'de'  # two-letter ISO 639-1 language code (optional, default en) - language of common names can be
# multiple (up to 3), separated by comma - i.e. (en,de,sv)
search_result: SearchResult = api.search(insect_for_search, language=language, limit=limit)

print(search_result)    # SearchResult(entities=[SearchEntity(matched_in='Harmonia axyridis',
# matched_in_type='entity_name', access_token='W24HYgI1AWQIOWZXVDdDc2VUE3BSMVNhBWEFNCRFU2I-', match_position=9,
# match_length=8)], entities_trimmed=False, limit=3)


# Get entity details based on access token from Insect search endpoint.
# One call cost 0.5 credits.

access_token = search_result.entities[0].access_token
requested_insect_details = 'common_names,url,description,image'
# comma separated list of requested insect details (required) see detail description in documentation (
# https://insect.kindwise.com/docs)

entity_details = api.get_kb_detail(access_token, requested_insect_details, language=language)
print(entity_details)
# {
# 'common_names': [
#    'Harlekin-Marienkäfer', 
#    'Vielfarbiger Marienkäfer', 
#    'Asiatischer Marienkäfer'
#    ],
# 'url': 'https://de.wikipedia.org/wiki/Asiatischer_Marienkäfer',
# 'description': {
#    'value': 'Der Asiatische Marienkäfer (Harmonia axyridis, auch „Vielfarbiger“ oder „Harlekin-Marienkäfer“) ist ein 
#    Käfer aus der Familie der Marienkäfer (Coccinellidae).\nUrsprünglich kommt die Art aus Asien und wurde Ende des 20.
#    Jahrhunderts zunächst in die USA und dann auch nach Europa zur biologischen Schädlingsbekämpfung eingeführt.
#    Inzwischen tritt der Käfer an vielen Stellen massenhaft wild auf, und man befürchtet, dass er einheimische 
#    Marienkäferarten und auch andere Insektenarten verdrängt. Im Herbst kann er Immobilienbesitzern lästig werden, da 
#    er dann Schwärme bildet, die zur Überwinterung Häuser und andere geschützte Orte aufsuchen.',
#    'citation': 'https://de.wikipedia.org/wiki/Asiatischer_Marienkäfer',
#    'license_name': 'CC BY-SA 3.0',
#    'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/'},
#    'image': {
#       'value': 'https://insect-id.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikispecies/bd2
#           /bd277ab6c571f84e7db39af05084ff6fc73d1da8.jpg',
#       'citation': '//commons.wikimedia.org/w/index.php?title=User:TheBookdetective&action=edit&redlink=1',
#       'license_name': 'CC BY-SA 4.0',
#       'license_url': 'https://creativecommons.org/licenses/by-sa/4.0/'
#       },
#    'language': 'de',
#    'entity_id': '5e7e11c01cc2d1a1',
#    'name': 'Harmonia axyridis'
#    }
