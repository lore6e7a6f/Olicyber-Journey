ct_hex = "27893459dc8772d66261ff8633ba1e5097c10fba257293872fd2664690e975d2015fc4fd3c"
ct = bytes.fromhex(ct_hex)

iniziale = b"flag{"
ks_part = bytes([c ^ p for c, p in zip(ct[:len(iniziale)], iniziale)])


key_len = 6
key = bytearray(key_len)

for i in range(key_len):
    if i < len(iniziale):
        key[i] = ct[i] ^ iniziale[i % len(iniziale)]
    else:
        key[i] = ks_part[i % len(iniziale)]

pt = bytes([c ^ key[i % key_len] for i, c in enumerate(ct)])


print("Plaintext:", pt.decode(errors="replace"))
