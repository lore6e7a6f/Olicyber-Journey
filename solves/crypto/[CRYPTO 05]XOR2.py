c = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")

for k in range(256):
    p = bytes(b ^ k for b in c)
    s = p.decode()

    # solo stringhe stampabili
    if all(32 <= ord(ch) <= 126 for ch in s):     
        print("flag{" + s + "}")