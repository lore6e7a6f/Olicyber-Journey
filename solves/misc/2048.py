from pwn import remote, context
import re

r = remote("2048.challs.olicyber.it", 10007)
context.timeout = 1
input = r.recv()
context.log_level = 'debug'

for i in range(2049):
    print(str(input))
    
    if "DIVISIONE_INTERA" in str(input):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(input))]
        t = s[0] // s[1]
        r.sendline(str(t))

    elif "DIFFERENZA" in str(input):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(input))]
        t = s[0] - s[1]
        r.sendline(str(t))

    elif "PRODOTTO" in str(input):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(input))]
        t = s[0] * s[1]
        r.sendline(str(t))

    elif "POTENZA" in str(input):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(input))]
        t = s[0] ** s[1]
        r.sendline(str(t))

    elif "SOMMA" in str(input):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(input))]
        t = sum(s)
        r.sendline(str(t))
    
    
    
    input = r.recv()    
print(str(input))