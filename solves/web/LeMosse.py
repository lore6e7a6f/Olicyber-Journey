import requests

url = "http://lemosse.challs.olicyber.it/"  
session = requests.Session()

r1 = session.get(f"{url}/step1")
print("GET /step1  ->", r1.text)

data_step2 = {
    "hello": "world",
    "dead": "beef"
}
r2 = session.post(f"{url}/step2", data=data_step2)
print("POST /step2 ->", r2.text)

r3 = session.put(f"{url}/step3")
print("PUT /step3  ->", r3.text)

r4 = session.delete(f"{url}/step4")
print("DELETE /step4 ->", r4.text)
