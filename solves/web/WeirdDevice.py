import requests

url = 'http://weird-device.challs.olicyber.it'

# cercare default device credentials 
payload = {"username":"ubnt", "password":"ubnt"}
r = requests.post(url, data=payload).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)

