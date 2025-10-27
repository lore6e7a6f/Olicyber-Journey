import requests

r = requests.get('http://treasure.challs.olicyber.it/flag?password=Belandi%2C%20dammi%20la%20flag!').text
for i in r.split():
    if "flag{" in i.lower():
        print(i)
