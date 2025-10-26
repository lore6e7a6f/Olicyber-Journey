import requests
from bs4 import BeautifulSoup

url_base = "http://web-16.challs.olicyber.it/"
da_visitare = [url_base]      # pagine da visitare
visitate = set()              # per evitare loop

while da_visitare:

    url = da_visitare.pop(0)

    if url in visitate:
        continue #skippo il ciclo

    visitate.add(url) #aggiorno ad ogni pagina già controllata

    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.text, "lxml")

    # controlla se nel h1 c’è la flag
    h1 = soup.find("h1")
    if h1 and "flag{" in h1.text:
        print("Trovata flag in:", url)
        print(h1.text.strip())
        break

    # aggiunge nuovi link da visitare
    for tag in soup.find_all("a"):
        link = tag.get("href")
        if link:
            # normalizza link relativo se contiene href
            if not link.startswith("http"):
                link = url_base + link.lstrip("/")
            if link not in visitate:
                da_visitare.append(link) 
