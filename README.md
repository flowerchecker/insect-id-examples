# Insect-id-API

[Insect.id](https://www.kindwise.com/insect-id) offers insect identification API based on machine learning. [Obtain the API key](https://admin.kindwise.com/signup) and get started with your implementation.

 - **[documentation](https://insect.kindwise.com/docs)** - full API reference
 - **[python SDK](https://github.com/flowerchecker/kindwise-api-client)** - simply use API from pyhon 
 - API specification on **[Postman](https://www.postman.com/winter-shadow-932363/kindwise/collection/6gn02uf/insect-id)**
 - try [online demo](https://insect.kindwise.com/demo/)
 - more [python examples](python)

## Insect Identification 🐞

Send us your plant images, and get a list of possible species suggestions with additional information.

```bash
pip install kindwise-api-client
```

```python
from kindwise import InsectApi

api = InsectApi('your_api_key')
identification = api.identify('../images/unknown_insect.jpg', details=['url', 'common_names'])

for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'])
    print(suggestion.details['common_names'])
    print()
```

Same example in pure python

```python
import base64
import requests

# encode images to base64
with open('unknown_insect.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

response = requests.post(
    'https://insect.kindwise.com/api/v1/identification',
    params={'details': 'url,common_names'},
    json={
        'images': images,
        'similar_images': True,
    },
    headers={
        'Content-Type': 'application/json',
        'Api-Key': '-- ask for one: https://admin.kindwise.com/signup --',
    }).json()

for suggestion in response['result']['classification']['suggestions']:
    print(suggestion['name'])                     # Lucanus cervus
    print(suggestion['details']['common_names'])  # European Stag Beetle
    print(suggestion['details']['url'])           # https://en.wikipedia.org/wiki/Lucanus_cervus
```
