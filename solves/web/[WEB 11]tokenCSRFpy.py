import requests

url_login = 'http://web-11.challs.olicyber.it/login'
url_flag  = 'http://web-11.challs.olicyber.it/flag_piece'
payload   = {"username": "admin", "password": "admin"}

s = requests.Session()  # inizia la sessione e mantiene i cookie
s.get(url_login)        

# login e ottieni il csrf 
r = s.post(url_login, json=payload)
j = r.json()
csrf = j.get("csrf") #valore relativo al token

vFlag = [] #vettore per ricostruire la flag

for i in range(4):
    # passa il token come parametro query "csrf"
    r = s.get(url_flag, params={'index': i, 'csrf': csrf})

    # legge JSON e prendere il pezzo
    j = r.json()
    pezzo = j.get("flag_piece")

    vFlag.append(pezzo) #riempio il vettore

    # aggiorna il CSRF per il prossimo ciclo
    csrf = j.get("csrf")
    print("Pezzo numero ["+str(i)+"]: ", vFlag[-1])

    

print("flag: ", ''.join(vFlag))
