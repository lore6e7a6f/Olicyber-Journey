import requests
import base64

s = requests.Session()
s.get('http://cuki.challs.olicyber.it')   
val = s.cookies.get('session')            
print(base64.b64decode(val).decode())
