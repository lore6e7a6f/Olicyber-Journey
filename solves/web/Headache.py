import requests

url = 'http://headache.challs.olicyber.it'

r = requests.get(url)
print(r.text)

for nome, valore in r.headers.items():
    print(f"{nome}: {valore}")
