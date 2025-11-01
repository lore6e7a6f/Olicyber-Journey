import math

def egcd(a, b):
    if b == 0:
        return (1, 0, a)
    x1, y1, d = egcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return (x, y, d)

# ------------------ #

#sostituire con i dati ricevuti

a, b = 118, 186 
x, y, g = egcd(a, b)

print(f"x = {x}, y = {y}, gcd = {g}")

# ------------------ #
a = 118
n = 186

if math.gcd(a, n) == 1:
    print("si")
else:
    print("no")

# ------------------ #
a, n = 65, 72
x, y, g = egcd(a, n)
if g != 1:
    print("Nessun inverso")
else:
    inv = x % n
    print(inv)