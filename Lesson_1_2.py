import requests

access_token = 'aedf791aa05e14b0ba0c38bb0b9def4a'
url_method = 'https://clc.li/api/url/add'
headers = {
           'url': 'https://dvmn.org/modules',
           'Authorization': 'Bearer access_token'
           }

response = requests.post(url_method, headers=headers)
response.raise_for_status()
#print(response.json())
print(response)