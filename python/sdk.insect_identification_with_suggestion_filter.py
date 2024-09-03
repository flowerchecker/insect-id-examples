from kindwise import InsectApi, MessageType

# suggestion_filter - str (optional) or dict (optional) in format {'classification': 'FILTER_NAME (filter examples
# below)'} Restricts the output of the model to specified list of classes (region or plant type) and adjusts the
# probabilities. The lists can be combined with logical operators and parentheses. The lists are available here:
# https://insect.kindwise.com/suggestion_filters

suggestion_filter = 'coleoptera'
api = InsectApi('your_api_key')
identification = api.identify(
    '../images/unknown_insect.jpg',
    details=['url', 'common_names'],
    extra_post_params={'suggestion_filter': suggestion_filter},
)

print('is insect' if identification.result.is_insect.binary else 'is not insect')
for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'], suggestion.details['common_names'])
    print()
