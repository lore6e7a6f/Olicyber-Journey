import requests
from bs4 import BeautifulSoup, Comment

url = 'http://web-14.challs.olicyber.it/' 

r = requests.get(url)
soup = BeautifulSoup(r.text, features='lxml')

# Trova tutti i commenti HTML controllando siano istanze di 'comment'
commenti = soup.find_all(string=lambda text: isinstance(text, Comment))

flag = "".join(commenti).strip()

print("output: " + flag )
