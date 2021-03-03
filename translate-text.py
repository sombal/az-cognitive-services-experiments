# -*- coding: utf-8 -*-
import requests, uuid

api_key = ''
api_endpoint = ''
path = '/translate?api-version=3.0'
params = '&to=en&to=hu&to=sk&profanityAction=Marked&ProfanityMarker=Asterisk'
constructed_url = api_endpoint + path + params

headers = {
    'Ocp-Apim-Subscription-Key': api_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

body = [{
    'text': 'Ich würde wirklich gern Ihr Auto um den Block fahren ein paar Mal.'
}]

request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()
print(body[0].get('text'))
print(response[0].get('translations')[0].get('text'))
print(response[0].get('translations')[1].get('text'))
print(response[0].get('translations')[2].get('text'))
