import json

import requests

from decouple import config

API_KEY = config('apikey')

url_method = 'https://clc.li/api/url/add'

url_input = input ('Введите ссылку, которую хотите сократить:  ')
headers = {'Authorization': f'Bearer {API_KEY}'}
params = {'url' : url_input}

def shorten_link(token, url):
    response = requests.post(url_method, headers=headers, json=params)
    response.raise_for_status()
    shot_link = json.loads(response.text)
    return shot_link


try: 
    short_link_diсt = shorten_link(API_KEY, url_input)
    print (short_link_diсt)
    
except requests.exceptions.HTTPError:
    print ('Вы ошиблись')
    
    




