import requests

url = 'http://gabibbo-says.challs.olicyber.it/'
paylaod = {"gabibbo":"angry"}
r=requests.post(url, data=paylaod).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)