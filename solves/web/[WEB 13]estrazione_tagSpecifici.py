import requests 
from bs4 import BeautifulSoup 
url = 'http://web-13.challs.olicyber.it/' 
r = requests.get(url) 

soup = BeautifulSoup(r.text, features='lxml') 

#flag=[] se si volesse creare un vettore e poi stampare char per char

tag_b = soup.find_all(class_="red") #filtra per char in rosso
flag = "".join(tag.get_text() for tag in tag_b)  #unisce i singoli char
    
print("output: flag{"+ flag +"}")