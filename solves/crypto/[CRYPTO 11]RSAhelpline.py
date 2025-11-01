import math

#sostituire con i dati ricevuti
p = 3
q = 17
n = p * q
phi_n = (p - 1) * (q - 1)

# messaggio e chiave pubblica
m = 10
e = 3

# cifratura
c = pow(m, e, n)

print(f"n = {n}")
print(f"(n) = {phi_n}")
print(f"Messaggio m = {m}")
print(f"Esponente pubblico e = {e}")
print(f"Testo cifrato c = {c}")