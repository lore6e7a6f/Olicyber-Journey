import requests

# Soluzioni verifica 4 dicembre 2023 - da caricare --- > 2023-12-04
url = 'http://trova-le-soluzioni.challs.olicyber.it/soluzioni-2023-2024/soluzioni/20231204.txt'
r = requests.get(url).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)