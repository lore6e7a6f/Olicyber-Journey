import requests
from bs4 import BeautifulSoup

url = 'http://web-12.challs.olicyber.it/'
r = requests.get(url)

html_doc=r.text #salvo l'html
soup = BeautifulSoup(html_doc, features="lxml")

#cerco in <pre>
tag_interessante = soup.find_all('pre')
print(tag_interessante)