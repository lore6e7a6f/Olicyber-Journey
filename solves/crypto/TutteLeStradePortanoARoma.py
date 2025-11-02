import string

def cesare(testo, chiave):
    alfabeto = string.ascii_lowercase
    risultato = ""
    for c in testo.lower():
        if c in alfabeto:
            indice = (alfabeto.index(c) + chiave) % 26
            risultato += alfabeto[indice]
        else:
            risultato += c
    return risultato

flag = "cixd{xsb_zxbpxo_jlofqrof_qb_pxirqxkq}"

possibili = []

for i in range(26):
    possibili.append(cesare(flag, i))

for line in possibili:
    if "flag{" in line.lower():
        print("flag: ", line)
