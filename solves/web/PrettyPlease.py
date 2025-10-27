import requests

url = 'http://prettyplease.challs.olicyber.it'
payload ={'how':'pretty please'}
r = requests.post(url, data=payload).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)