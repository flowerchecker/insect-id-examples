import requests

# Search insect knowledge base by query. Entities are searchable by scientific names, common names (in specified
# language), synonyms. Insect name and query are always matched from start of a word., i.e. 'Harmonia axyridis' is
# searchable by 'Harmonia', 'Harmon', 'axyridis', 'axyrid', 'Harmonia axyridis'...


insect_for_search = 'axyridis'
limit = 3        # int (optional) - maximum of returned result, max. 20, default 10
language = 'en'  # two-letter ISO 639-1 language code (optional, default en) - language of common names can be
# multiple (up to 3), separated by comma - i.e. (en,de,sv)

response = requests.get(
    'https://insect.kindwise.com/api/v1/kb/insect/name_search',
    params={'q': insect_for_search, 'limit': limit, 'language': language},
    headers={'Api-Key': 'your_api_key'},
)

search = response.json()
print(search)  # {'entities': [{'matched_in': 'Harmonia axyridis', 'matched_in_type': 'entity_name', 'access_token':
# 'XGkmQ29YCm9IeUV0B2R_T1BhNlVTMHVHAmZCczBRRnc-', 'match_position': 9, 'match_length': 8, 'entity_name': 'Harmonia
# axyridis'}], 'entities_trimmed': False, 'limit': 3}


# Get entity details based on access token from Insect search endpoint.
# One call cost 0.5 credits.

if search['entities']:
    access_token = search['entities'][0]['access_token']
    requested_insect_details = 'common_names,url,description,image'
    # comma separated list of requested insect details (required) see detail description in documentation (
    # https://insect.kindwise.com/docs)

    response = requests.get(
        f'https://insect.kindwise.com/api/v1/kb/insect/{access_token}',
        params={'details': requested_insect_details, 'language': language},
        headers={'Api-Key': 'your_api_key'},
    )

    detail = response.json()
    print(detail)
# {
# 'common_names': [
#   'Asian Lady Beetle',
#   'Multicolored Asian Lady Beetle',
#   'Asian Ladybird Beetle',
#   'Japanese Ladybug',
#   'Harlequin Lady Beetle',
#   'Asian Ladybug',
#   'Haxy',
#   'Harlequin Ladybird',
#   'Asiatic Ladybird',
#   'Many-named Ladybird',
#   'Pumpkin Ladybeetle',
#   'Orange Ladybug'
#   ],
# 'url': 'https://en.wikipedia.org/wiki/Harmonia_axyridis',
# 'description': {
#   'value': 'Harmonia axyridis is a large lady beetle or ladybug species that is most commonly known as the harlequin,
#       multicoloured Asian, or Asian lady beetle. This is one of the most variable species in the world, with an
#       exceptionally wide range of colour forms. It is native to eastern Asia, but has been artificially introduced to
#       North America and Europe to control aphids and scale insects. It is now common, well known, and spreading in
#       those regions, and has also established in Africa and widely across South America. This species is conspicuous
#       in North America, where it may locally be known as the Halloween beetle, as it often invades homes during
#       October to overwinter.When the species first arrived in the UK, it was labelled in jest as the "many-named
#       ladybird" due to the great quantity of vernacular names. Among those already listed other names include
#       multivariate, southern, Japanese, and pumpkin ladybird.\n\n',
#   'citation': 'https://en.wikipedia.org/wiki/Harmonia_axyridis',
#   'license_name': 'CC BY-SA 3.0',
#   'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/'
#   },
# 'image': {
#   'value': 'https://insect-id.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikispecies/bd2
#       /bd277ab6c571f84e7db39af05084ff6fc73d1da8.jpg',
#   'citation': '//commons.wikimedia.org/w/index.php?title=User:TheBookdetective&action=edit&redlink=1',
#   'license_name': 'CC BY-SA 4.0',
#   'license_url': 'https://creativecommons.org/licenses/by-sa/4.0/'
#   },
# 'language': 'en',
# 'entity_id': '5e7e11c01cc2d1a1',
# 'name': 'Harmonia axyridis'
# }
