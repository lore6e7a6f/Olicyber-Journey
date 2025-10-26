import requests

url = "http://web-10.challs.olicyber.it/"
r = requests.options(url)

r = requests.request('POST', url)

# put, patch, post danno errori, bisogna sfruttarli cercando risposte nel body e negli headers

print(r.text)

# print(r.headers.items) non formattato

for nome, valore in r.headers.items():
    print(f"{nome}: {valore}")

