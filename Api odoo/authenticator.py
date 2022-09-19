import json
import requests
import sys

AUTH_URL = 'http://172.18.15.108:8069/web/login'

headers = {'Content-type': 'application/json'}


#Autenticacao de credenciais
data = {
    'params': {
         'login': 'your@email.com',
         'password': 'yor_password',
         'db': 'your_db_name'
    }
}

# Autenticacao do user
res = requests.post(
    AUTH_URL, 
    data=json.dumps(data), 
    headers=headers
)


cookies = res.cookies


USERS_URL = ''



res = requests.get(
    USERS_URL, 
    cookies=cookies  
)


print(res.text)



USERS_URL = ''


params = {'query': '{id, name}'}

res = requests.get(
    USERS_URL, 
    params=params,
    cookies=cookies  
)


print(res.text)
