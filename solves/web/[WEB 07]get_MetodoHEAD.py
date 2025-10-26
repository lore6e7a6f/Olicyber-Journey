import requests

url='http://web-07.challs.olicyber.it/'

r=requests.head(url)

#stampo header:descrizione

for nome, valore in r.headers.items():
    print(f"{nome}: {valore}")