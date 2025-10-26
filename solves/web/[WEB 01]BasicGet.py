import requests

url='http://web-01.challs.olicyber.it/'

r=requests.get(url)
print(r.text)