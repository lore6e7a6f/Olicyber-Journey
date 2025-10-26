import requests

url = "http://web-02.challs.olicyber.it/server-records" 
payload = {"id": "flag"}

r = requests.get(url, params=payload)  
print(r.text)

