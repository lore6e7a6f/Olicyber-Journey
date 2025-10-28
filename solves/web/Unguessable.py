import requests

url ='http://unguessable.challs.olicyber.it'

string_inSourceCode ='/vjfYkHzyZGJ4A7cPNutFeM/flag'
r = requests.get(url + string_inSourceCode)
print(r.text)