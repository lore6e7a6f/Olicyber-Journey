from Crypto.Cipher import AES
import hashlib
import base64

# dati del JS
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