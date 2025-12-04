from pwn import *

r = remote("nt-master.challs.olicyber.it", 11001)
for i in range(10):
    r.recvuntil(b"N = ")
    input = r.recvline().decode().replace("\n","")
    res = int(input, 10)
    print(i)
    r.sendline(f"{res-1} 1".encode())
    
print(r.recv(1000).decode())