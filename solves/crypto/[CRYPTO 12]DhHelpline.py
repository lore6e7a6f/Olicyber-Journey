# --------------- #

prima = "p-1"

# --------------- #

# sostituire con i valori ricevuti

M = 290662986355414286148939006020581203673
target = 4096
base = 2

cur = 1
for k in range(0, 1000000):  # limite abbondante
    if cur == target:
        print(k)
        break
    cur = (cur * base) % M
else:
    print("Not found")

# ----------------- # 

base = 3
target = 30
mod = 79

cur = 1
for k in range(mod):  # prova tutti k da 0 a 78
    if cur == target:
        print(k)
        break
    cur = (cur * base) % mod

# ------------------ # 
print(pow(2, 15, 131)) 
print(pow(111, 15, 131))