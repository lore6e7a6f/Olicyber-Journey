import pyshark
from collections import defaultdict

v = defaultdict(str)

cap = pyshark.FileCapture('flag-interceptor.pcap')

for i in cap:
    if 'data' in i:
        ip = i.ip.src
        data = i.data.data
        v[ip] += bytes.fromhex(data).decode()[:-1]

for i in v:
    stream = v[i]
    if stream.startswith('flag{') and stream.endswith('}'):
        print(stream)
    else:
        continue