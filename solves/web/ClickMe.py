import requests

url = 'http://click-me.challs.olicyber.it'
payload = {'cookies':'10000000'}

"""
r=requests.get(url)
print(r.text)
"""
r=requests.post(url, cookies=payload).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)
