from time import sleep

from kindwise import InsectApi

if __name__ == '__main__':
    api = InsectApi('your_api_key')
    identification = api.identify('../images/unknown_insect.jpg', asynchronous=True)

    print('Waiting for results...')
    while identification.result is None:
        sleep(1)
        identification = api.get_identification(identification.access_token)
    print(identification.result)    # Result(classification=Classification(suggestions=[Suggestion(
    # id='5e7e11c01cc2d1a1', name='Harmonia axyridis', probability=0.9647, similar_images=[SimilarImage(
    # id='46a73673bfdd314cd433ec9b0a0ead07',
    # url='https://insect-id.ams3.cdn.digitaloceanspaces.com/similar_images/1/46a/73673bfdd314cd433ec9b0a0ead07.jpg',
    # similarity=0.777, url_small='https://insect-id.ams3.cdn.digitaloceanspaces.com/similar_images/1/46a
    # /73673bfdd314cd433ec9b0a0ead07.small.jpg', license_name=None, license_url=None, citation=None), SimilarImage(
    # id='3a4353cd3014ddbd992b42d1a11490e4',
    # url='https://insect-id.ams3.cdn.digitaloceanspaces.com/similar_images/1/3a4/353cd3014ddbd992b42d1a11490e4.jpeg
    # ', similarity=0.393, url_small='https://insect-id.ams3.cdn.digitaloceanspaces.com/similar_images/1/3a4
    # /353cd3014ddbd992b42d1a11490e4.small.jpeg', license_name='CC BY 4.0',
    # license_url='https://creativecommons.org/licenses/by/4.0/', citation='Cole Shoemaker')], details={'language':
    # 'en', 'entity_id': '5e7e11c01cc2d1a1'}), Suggestion(id='1c75089bf594dc22', name='Hippodamia variegata',
    # probability=0.0224, similar_images=[SimilarImage(id='33ff4bb6694cecb3753d6776fe83df05',
    # url='https://insect-id.ams3.cdn.digitaloceanspaces.com/similar_images/1/33f/f4bb6694cecb3753d6776fe83df05.jpeg
    # ', similarity=0.373, url_small='https://insect-id.ams3.cdn.digitaloceanspaces.com/similar_images/1/33f
    # /f4bb6694cecb3753d6776fe83df05.small.jpeg', license_name='CC BY 4.0',
    # license_url='https://creativecommons.org/licenses/by/4.0/', citation='Mattia Menchetti'), SimilarImage(
    # id='709b745d84a788b36fc0a81be68b928c',
    # url='https://insect-id.ams3.cdn.digitaloceanspaces.com/similar_images/1/709/b745d84a788b36fc0a81be68b928c.jpeg
    # ', similarity=0.339, url_small='https://insect-id.ams3.cdn.digitaloceanspaces.com/similar_images/1/709
    # /b745d84a788b36fc0a81be68b928c.small.jpeg', license_name='CC BY 4.0',
    # license_url='https://creativecommons.org/licenses/by/4.0/', citation='Lek Khauv')], details={'language': 'en',
    # 'entity_id': '1c75089bf594dc22'})]))
