from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Cipher import ChaCha20


def x923_pad(b: bytes, block_size: int = 8) -> bytes:
    pad_len = block_size - (len(b) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return b + b'\x00' * (pad_len - 1) + bytes([pad_len])

 # PRIMA DOMANDA----------------------------- #

key_hex = '8682fb3f2d986d71'
key = bytes.fromhex(key_hex)
iv = b'\x00' * 8

plaintext = "La lunghezza di questa frase non è divisibile per 8"
p = plaintext.encode('utf-8')

p_padded = x923_pad(p, 8)

cipher = DES.new(key, DES.MODE_CBC, iv)
ct = cipher.encrypt(p_padded)
print("Prima domanda:\n" + ct.hex())
print("IV utilizzato: 00000000")

 # SECONDA DOMANDA ----------------------------- #

plaintext = "Mi chiedo cosa significhi il numero nel nome di questo algoritmo."
key_hex = "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
key = bytes.fromhex(key_hex)
iv = b'\x00' * 16  # IV = 16 byte a zero 

# Padding PKCS7 con block_size = 16
padded = pad(plaintext.encode('utf-8'), 16, style='pkcs7')

# AES IN CFB
cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=24)
ciphertext = cipher.encrypt(padded)

print("Seconda domanda:\n" + "Chiave (hex):", key_hex)
print("IV (hex):", iv.hex())
print("Ciphertext (hex):", ciphertext.hex())

 # TERZA DOMANDA----------------------------- #

key = bytes.fromhex("4ad31923f4df2f94b8771c40b8a3ef8e9031f4699cd294c35bc97a2296b6ac9f")
nonce = bytes.fromhex("4fc2f53953de67e4")
ciphertext = bytes.fromhex("0e5e1ec5d7359576e61b95413253adcbc056ea73b99adad269003845")

cipher = ChaCha20.new(key=key, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

print("Terza domanda:\n" + plaintext.decode('ascii'))