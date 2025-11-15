alphabet = "abcdefghijklmnopqrstuvwxyz"

def rotate_right(s):
    return s[-1] + s[:-1]

def rotate_left(s):
    return s[1:] + s[0]

def decrypt(cipher, key):
    plaintext = ""

    for c in cipher:
        if "A" <= c <= "Z":  # uppercase
            c_low = chr(ord(c) + 32)
            i = key.index(c_low)
            p = alphabet[i]
            plaintext += chr(ord(p) - 32)
            key = rotate_right(key)

        elif "a" <= c <= "z":  # lowercase
            i = key.index(c)
            p = alphabet[i]
            plaintext += p
            key = rotate_right(key)

        else:
            plaintext += c

    return plaintext

def all_keys():
    keys = []
    for start in range(1, 26):
        key = alphabet[start:] + alphabet[:start]
        keys.append(key)
    return keys

ciphertext = "xcqv{gvyavn_zvztv_etvtddlnxcgy}"

for key in all_keys():
    if(decrypt(ciphertext, key).startswith("flag{")):
        print(decrypt(ciphertext, key))
