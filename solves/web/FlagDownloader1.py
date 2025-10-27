import requests

url = 'http://flagdownloader.challs.olicyber.it'
flag = ''
n = '0'

#elimino il timeout
while n:
    r = requests.get(url+'/download/flag/'+n)
    j = r.json()
    n = j['n']
    flag += j['c']

print(flag)