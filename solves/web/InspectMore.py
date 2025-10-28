import requests

url = 'http://inspect-more.challs.olicyber.it/validate_result'

# risultato nei commenti
payload = {"result": 0.0776}
r = requests.post(url, json=payload).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)

