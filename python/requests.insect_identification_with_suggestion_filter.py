import base64

import requests

with open('../images/unknown_insect.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

# suggestion_filter - dict (optional) in format {"classification": "FILTER_NAME (filter examples below)"} Restricts
# the output of the model to specified list of classes (region or plant type) and adjusts the probabilities. The
# lists can be combined with logical operators and parentheses. The lists are available here:
# https://insect.kindwise.com/suggestion_filters

suggestion_filter = {'classification': 'coleoptera'}

response = requests.post(
    'https://insect.kindwise.com/api/v1/identification',
    params={'details': 'url,common_names', 'language': 'en,de'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images, 'suggestion_filter': suggestion_filter},
)

identification = response.json()

print('is insect' if identification['result']['is_insect']['binary'] else 'is not insect')
for suggestion in identification['result']['classification']['suggestions']:
    print(suggestion['name'])
    print(f'probability {suggestion["probability"]:.2%}')
    print(suggestion['details']['url'], suggestion['details']['common_names'])
    print()
