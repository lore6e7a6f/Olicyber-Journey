import requests

url_cookie = 'http://web-06.challs.olicyber.it/token'
url_flag = 'http://web-06.challs.olicyber.it/flag'

s=requests.Session()
s.get(url_cookie) #salvo il cookie

r=s.get(url_flag) #con il cookie di prima apro url_flag

print(r.text)