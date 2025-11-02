# zizionario del cifrario di Bacon
dizionario = {
    'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D',
    'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H',
    'ABAAA': 'I', 'ABAAB': 'J', 'ABABA': 'K', 'ABABB': 'L',
    'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O', 'ABBBB': 'P',
    'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
    'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X',
    'BBAAA': 'Y', 'BBAAB': 'Z'
}

stringa = "AAAABAAAAAAAABAABBBAABBABABAAABAABABAABAABBBABAABBAAAAABAABABAABBBBAAA"

i = 0
decodificato = ""

while i < len(stringa):
    gruppo = stringa[i:i+5]
    lettera = dizionario.get(gruppo, '?')  # usa '?' se il gruppo non esiste nel dizionario
    decodificato += lettera
    i += 5

print(f"flag{{{decodificato.lower()}}}")
