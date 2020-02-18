# -*- coding: utf-8 -*-
import requests, uuid

api_key = '9dbcb058fe69462ba9d26b6af0965ee2'
api_endpoint = 'https://api-eur.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'
params = '&to=es&to=en&profanityAction=Marked&ProfanityMarker=Asterisk'
constructed_url = api_endpoint + path + params

headers = {
    'Ocp-Apim-Subscription-Key': api_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

body = [{
    'text': 'Menj a fenébe!'
}]

request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()
print(body[0].get('text'))
print(response[0].get('translations')[0].get('text'))
print(response[0].get('translations')[1].get('text'))
