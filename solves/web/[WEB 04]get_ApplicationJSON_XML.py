import requests

url="http://web-04.challs.olicyber.it/users"

payload_xml={'Accept':'application/xml'}
payload_JSON={'Accept':'application/JSON'}

r1=requests.get(url, headers=payload_xml)
r2=requests.get(url, headers=payload_JSON)

print(r1.text)
print(r2.text)