"""
  -- STAMPA HEADERS -- 

for nome, valore in r.headers.items():
    print(f"{nome}: {valore}")

"""

"""
 -- WEB SPIDER -- 

import requests
from bs4 import BeautifulSoup

url_base = ""
da_visitare = [url_base]      # pagine da visitare
visitate = set()              # per evitare loop

while da_visitare:

    url = da_visitare.pop(0)

    if url in visitate:
        continue #skippo il ciclo

    visitate.add(url) #aggiorno ad ogni pagina già controllata

    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.text, "lxml")

    # controlla se nel h1 c’è la flag
    h1 = soup.find("h1")
    if h1 and "flag{" in h1.text:
        print("Trovata flag in:", url)
        print(h1.text.strip())
        break

    # aggiunge nuovi link da visitare
    for tag in soup.find_all("a"):
        link = tag.get("href")
        if link:
            # normalizza link relativo se contiene href
            if not link.startswith("http"):
                link = url_base + link.lstrip("/")
            if link not in visitate:
                da_visitare.append(link) 

"""

"""
 -- ESTRAZIONE FLAG -- 

for line in html.splitlines():
    if "flag{" in line.lower():
        print("flag:\n", line)

"""

"""
 -- AES DECRYPT (salted)-- 

    from Crypto.Cipher import AES
    import hashlib
    import base64

    # dati 
    b64 = 'U2FsdGVkX1/JEKDXgPl2RqtEgj0LMdp8/Q1FQelH7whIP49sq+WvNOeNjjXwmdrl'
    passphrase = 'ML4czctKUzigEeuR'

    data = base64.b64decode(b64)

    # data è salted
    salt = data[8:16] 
    ciphertext = data[16:]

    # Derivazione key+iv 
    dtot = b''
    d = b''
    while len(dtot) < (48):  # key_len=32 (AES-256), iv_len=16
        d = hashlib.md5(d + passphrase.encode('utf-8') + salt).digest()
        dtot += d

    key = dtot[:32]
    iv = dtot[32:48]

    # Decrypt con CryptoCipher
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)

    print(decrypted.decode('utf-8'))
"""