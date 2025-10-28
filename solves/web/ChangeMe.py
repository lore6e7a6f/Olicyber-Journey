import requests

url = 'http://change-me.challs.olicyber.it'

r = requests.post(url).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)

