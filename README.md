# Insect-id-API
*⚠️ This service is in beta version and can undergo changes which might not be compatible with the curent version.*

[Insect.id](https://insect.id) offers insect identification API based on machine learning. [Obtain the API key](https://admin.mlapi.ai/signup) and get started with your implementation.

See our **[documentation](http://insect.kindwise.com/docs)** for the full reference.

## Insect Identification 🐞
Send us your insect images encoded in base64, and get a list of possible species suggestions with additional information.
```python
import base64
import requests

# encode images to base64
with open("unknown_insect.jpg", "rb") as file:
    images = [base64.b64encode(file.read()).decode("ascii")]

response = requests.post(
    "https://insect.mlapi.ai/api/v1/identification?details=common_names,url",
    json={
        "images": images,
        "similar_images": True,
    },
    headers={
        "Content-Type": "application/json",
        "Api-Key": "-- ask for one: https://admin.mlapi.ai/signup --",
    }).json()

for suggestion in response["result"]["classification"]["suggestions"]:
    print(suggestion["name"])                     # Lucanus cervus
    print(suggestion["details"]["common_names"])  # European Stag Beetle
    print(suggestion["details"]["url"])           # https://en.wikipedia.org/wiki/Lucanus_cervus
```
