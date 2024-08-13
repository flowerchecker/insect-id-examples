from datetime import datetime

from kindwise import InsectApi

if __name__ == '__main__':
    api = InsectApi('your_api_key')
    identification = api.identify(
        ['../images/photo_1.jpg', '../images/photo_2.jpg'],
        latitude_longitude=(13.3966042, 23.3150361),
        date_time=datetime(2024, 8, 13),
        details=[
            'common_names',     # list of strings - localized - local, non-scientific name
            'url',              # string - localized - link to insect profile page (usually Wikipedia)
            'description',      # string - localized, licensed - short description from Wikipedia
            'taxonomy',         # dict - scientific taxonomy
            'rank',             # string - taxonomic rank
            'gbif_id',          # int - id in GBIF database
            'inaturalist_id',   # int - id in iNaturalist database
            'image',            # string - with licence - url of representative image
            'images'            # list - with licences - list of more urls of representative images
        ],
        language='de',
        similar_images=True,
    )

    for suggestion in identification.result.classification.suggestions:
        print(suggestion.name)
        print(f'probability {suggestion.probability:.2%}')
        print(suggestion.details)
        print(suggestion.similar_images)
        print()
