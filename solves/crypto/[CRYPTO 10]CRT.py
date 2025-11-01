from sympy.ntheory.modular import crt

#sostituire con i dati ricevuti
moduli = [50, 41, 51, 71, 43]
resti = [9, 5, 33, 47, 24]

# risolve il sistema
x, _ = crt(moduli, resti)

# modulo di x
print(x % 319191150)
