import base64

import requests

with open('../images/unknown_insect.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

response = requests.post(
    'https://insect.kindwise.com/api/v1/identification',
    params={'details': 'common_names,gbif_id,taxonomy,rank', 'language': 'en,de'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images},
)

identification = response.json()
print(identification)
for suggestion in identification['result']['classification']['suggestions']:
    print(suggestion['name'])                               # Harmonia axyridis
    print(f'probability {suggestion["probability"]:.2%}')   # probability 96.48%
    print(suggestion['details']['common_names'])            # {'en': ['Asian Lady Beetle', 'Multicolored Asian Lady
    # Beetle', 'Asian Ladybird Beetle', 'Japanese Ladybug', 'Harlequin Lady Beetle', 'Asian Ladybug', 'Haxy',
    # 'Harlequin Ladybird', 'Asiatic Ladybird', 'Many-named Ladybird', 'Pumpkin Ladybeetle', 'Orange Ladybug'],
    # 'de': ['Harlekin-Marienkäfer', 'Vielfarbiger Marienkäfer', 'Asiatischer Marienkäfer']}
    print()
