import requests

url = 'http://no-robots.challs.olicyber.it'
r = requests.get(url)

print(r.text)
payload = '/robots.txt'

url_robots = url + payload
r = requests.get(url_robots)

print('Output of /robots.txt: \n' + (r.text))

txt = requests.get(url_robots).text
for line in txt.splitlines():
    if line.startswith("Disallow:"):
        disallow = line.split(":", 1)[1].strip()

url_flag = url + disallow
html = requests.get(url_flag).text

for line in html.splitlines():
    if "flag{" in line.lower():
        print("flag:\n", line)

