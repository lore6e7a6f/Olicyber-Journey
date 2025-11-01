from pwn import *
from Crypto.Hash import SHA3_384, SHA224, HMAC
from Crypto.Random import *
from Crypto.Util.number import *
from cryptography.hazmat.primitives import serialization
from Crypto.Util import number

# --------------------- #
msg = b"hash_me_pls"
h = SHA3_384.new(msg)
print(str(h.hexdigest()).encode())

# --------------------- #
h = HMAC.new(bytes.fromhex("7c289cc9d8a32a0a4f202d51cd71a97363e9916b226a133ed294b33c68c189a9"), digestmod=SHA224)
msg = "La mia integrità è importante!".encode()
h.update(msg)
print(str(h.hexdigest()).encode())

# --------------------- #
chiave = "3082025c0201003082023506072a8648ce380401308202280282010100da065ecd76effd932825503727232bef5caf54a199f2dbdb3ab62049c7df2777ff8fd7f776b09e67491a7cfba00eead5df983af449a2630649a7bf7b8f9ca0415d5de1a232e63645616a50c8bd679b422c0ac5fcd64b3fd27fbc4be62a2cc020df062136f267522b0068e76c8913f3e521ebf7876a5f63218fa48c0019e64b9013949d2be45865345bafdc182fe97cb7241502e975e002b7261ca757f943014b0f0d1d98db58e0bdc592246307d4b86f8fac59509d5086f1845d889265aa74986fc4c8362880334929f392cfc14bf35f65b53a02c446fba165e11f1f704bdc992ce9345796ef6e75f88478a27ced5e1422ddc72d31d6d96a62868fb59aee5c49021d0092580a706cf031641e435cec52aa77499df88c360c04cf7529a3e6950282010007a1b960b2b288ae4158c7ba395cc5826e16f45130d5144eb61bd0377be746b9987d3d245f1c117c469c501204916449c5fa2ddc5c35655716768ef91fa64b45e1d268a86d3471e0b9daccef0481811537b8e3663f7ca20376cb26e3711ff4aadf20cfbbc9b95bd8d85b213dc76fc9f728f6c1a25d00fd8752960eb4a3d7f2f596205710afbef088b8247b005a4514b7eed98ce42739fb9711c5510873616625aed0035210ae598393bd2034f18120e20b6f3043c89c1a3f075efe85fd4d5b6d16258fbd85c9072d696beb263b9af6b31ce364261a05363c6f92d861a35a2f9d207f3fface01ffd90f374259ccffc955a3d64a3301425459dc946c6f9a39dcd5041e021c078bc0f3923e05e098164b4c9f94849e7d8c6ff36192f3d1d2477fb7"
key_der = binascii.unhexlify(chiave)

private_key = serialization.load_der_private_key(key_der, password=None)
numbers = private_key.private_numbers()

p = numbers.public_numbers.parameter_numbers.p
q = numbers.public_numbers.parameter_numbers.q
g = numbers.public_numbers.parameter_numbers.g
y = numbers.public_numbers.y
x = numbers.x

print("p =", p)
print("q =", q)
print("g =", g)
print("y =", y)
print("x =", x)

# --------------------- #

primo = number.getPrime(1162) #cambiare in base al numero richiesto
print("Primo: "+ str(primo))

# --------------------- #

prime = 40939895829132005759187754980239660409570841510765086799713825945673865425601052884630512226132191747812987758393941967575249704888241910619243643360207196579878813116528863741002587678853573821456170906050209183063943117361857350031789094953470302784590907312186649099258810729826043886878578981611426923874
if isPrime(prime):
    print("si")
else:
    print("no")