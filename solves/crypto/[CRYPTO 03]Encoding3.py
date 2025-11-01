from base64 import b64decode

s = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
n = 664813035583918006462745898431981286737635929725

first_part = b64decode(s)

# numero minimo di byte necessari
nbytes = (n.bit_length() + 7) // 8     

second_part = n.to_bytes(nbytes, 'big')
print(first_part + second_part)