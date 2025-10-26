import requests

url ='http://web-09.challs.olicyber.it/login'

payload={'username':'admin', 'password':'admin'}
#headers={'Content-Type':'application/json'}

r=requests.post(url, json=payload) #headers=headers)

print(r.text)