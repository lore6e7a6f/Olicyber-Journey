import re

data = """
0010115f  c6 85 f0 fe           MOV            byte ptr [RBP + local_118],0x66
00101166  c6 85 f1 fe           MOV            byte ptr [RBP + local_117],0x6c
0010116d  c6 85 f2 fe           MOV            byte ptr [RBP + local_116],0x61
00101174  c6 85 f3 fe           MOV            byte ptr [RBP + local_115],0x67
0010117b  c6 85 f4 fe           MOV            byte ptr [RBP + local_114],0x7b
00101182  c6 85 f5 fe           MOV            byte ptr [RBP + local_113],0x66
00101189  c6 85 f6 fe           MOV            byte ptr [RBP + local_112],0x63
00101190  c6 85 f7 fe           MOV            byte ptr [RBP + local_111],0x32
00101197  c6 85 f8 fe           MOV            byte ptr [RBP + local_110],0x66
0010119e  c6 85 f9 fe           MOV            byte ptr [RBP + local_10f],0x34
001011a5  c6 85 fa fe           MOV            byte ptr [RBP + local_10e],0x34
001011ac  c6 85 fb fe           MOV            byte ptr [RBP + local_10d],0x39
001011b3  c6 85 fc fe           MOV            byte ptr [RBP + local_10c],0x62
001011ba  c6 85 fd fe           MOV            byte ptr [RBP + local_10b],0x7d
001011c1  c6 85 fe fe           MOV            byte ptr [RBP + local_10a],0x0
"""

hex_values = re.findall(r'0x[0-9a-fA-F]+', data)
bytes_list = [int(x, 16) for x in hex_values if x != '0x0']


decoded = ''.join(chr(b) for b in bytes_list)
print(decoded)
