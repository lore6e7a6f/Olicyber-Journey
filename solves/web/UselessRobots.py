import requests

url = 'https://useless-robots.challs.olicyber.it'
robots = '/robots.txt'

r = requests.get(url+robots).text
#print(r)

disallow ='/4a10eb719bf40679eec6'
r = requests.get(url+disallow).text
for i in r.split():
    if "flag{" in i.lower():
        print(i)
