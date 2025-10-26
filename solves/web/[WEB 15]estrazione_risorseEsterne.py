import requests
from bs4 import BeautifulSoup

url_base = "http://web-15.challs.olicyber.it/"

soup = BeautifulSoup(requests.get(url_base).text, "lxml")

risorse = []

for tag in soup.find_all("link"):
    if tag.get("href"):
        risorse.append(url_base + tag.get("href").lstrip("/")) #togliendo eventuali doppi /

for tag in soup.find_all("script"):
    if tag.get("src"):
        risorse.append(url_base + tag.get("src").lstrip("/"))

for r in risorse:
    body = requests.get(r).text
    if "flag{" in body:
        print("flag in:", r)
        inizio = body.find("flag{")
        fine = body.find("}", inizio)
        print(body[inizio:fine+1])
        #break
