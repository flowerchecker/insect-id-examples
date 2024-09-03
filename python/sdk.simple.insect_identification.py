from kindwise import InsectApi

api = InsectApi('your_api_key')
identification = api.identify('../images/unknown_insect.jpg', details=['url', 'common_names'])

print('is insect' if identification.result.is_insect.binary else 'is not insect')
for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)                              # Harmonia axyridis
    print(f'probability {suggestion.probability:.2%}')  # probability 96.47%
    print(suggestion.details['url'])                    # https://en.wikipedia.org/wiki/Harmonia_axyridis
    print(suggestion.details['common_names'])           # ['Asian Lady Beetle', 'Multicolored Asian Lady Beetle',
    # 'Asian Ladybird Beetle', 'Japanese Ladybug', 'Harlequin Lady Beetle', 'Asian Ladybug', 'Haxy', 'Harlequin
    # Ladybird', 'Asiatic Ladybird', 'Many-named Ladybird', 'Pumpkin Ladybeetle', 'Orange Ladybug']
    print()
