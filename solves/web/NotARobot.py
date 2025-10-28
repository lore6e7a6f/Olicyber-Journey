import requests

robotsTXT = "/robots.txt"
url = 'http://not-a-robot.challs.olicyber.it'

r = requests.get(url + robotsTXT)
print(r.text)

#Disallow: /pl5_d0nt_vi51t_me

r = requests.get(url +"/pl5_d0nt_vi51t_me").text

for i in r.split():
    if "flag{" in i.lower():
        print(i)