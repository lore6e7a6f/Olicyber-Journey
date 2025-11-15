import string

alphabet = string.ascii_lowercase

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            plaintext += char
    return plaintext


def brute_force_linear(ciphertext, max_len=2):
    for c1 in alphabet:
        yield c1, vigenere_decrypt(ciphertext, c1)

    if max_len >= 2:
        for c1 in alphabet:
            for c2 in alphabet:
                key = c1 + c2
                yield key, vigenere_decrypt(ciphertext, key)


# 🔍 Esempio d’uso
cipher = "fzau{ncn_isors_cviovw_pwcqoze}"

for key, result in brute_force_linear(cipher, max_len=2):
    print(f"{key} -> {result}")
