from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes

# p usato anche da https://github.com/AlBovo/Olicyber-WriteUps/blob/main/Introduzione/Crittografia%20%F0%9F%94%90/Crypto%2013%20-%20A%20Diffiecult%20communication.py
p = 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624225795083
g = 5
b = 20

A_hex = "3c7781edda9492f04a20fd139cac72d53e15162c96713161dd0246c9433662921e2b0cf45e2ad3d771cc4aa3005dc8b10eba681ce832dbeaaa3b7fff754c54269a2fcf565108e82e37db26805b2e05fb6723f894d165b674d283d0109dba29c848e6e879690a504b434183075d067b38f7a0c74047429105a5304e1a422d979e"
IV_hex = "ba4e6003b7a1470fe18a3292f316e019"
msg_hex = "58cb88acae36e247bf482e2d77f686378e457171b148f4f923d01fe05f1776d30837afdab921b9178c0190bc8784eb593cf4f0d04449a89b5e6efb1d610b93a5"

# conversione
A = int(A_hex, 16)
IV = bytes.fromhex(IV_hex)
msg = bytes.fromhex(msg_hex)

# calcola shared e chiave (PRIMI 16 BYTE di long_to_bytes(shared))
shared = pow(A, b, p)
shared_bytes = long_to_bytes(shared)
key = shared_bytes[:16]

# decrittazione AES-CBC e unpad
cipher = AES.new(key, AES.MODE_CBC, IV)
decrypted = cipher.decrypt(msg)
plaintext = unpad(decrypted, AES.block_size)

print(plaintext.decode("utf-8"))
    
