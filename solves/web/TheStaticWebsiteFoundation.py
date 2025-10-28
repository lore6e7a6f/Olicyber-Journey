import requests 

url = "http://staticwebfoundation.challs.olicyber.it"

r = requests.head(url)
#print(r.headers) #link nascosto
r = requests.get(url + "/o1SfuSXpptIk1p8U0qISobkrYwXSILflr6ZxTsmF?p=banana")
print(r.text, end="")