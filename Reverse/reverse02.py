a =[
    0x32,0x67,0x31,0x3b,
    0x61,0x32,0x67,0x3e,
    0x3d,0x3f,0x6c,0x3f,
    0x35,0x68,0x37,0x3e,
    0x26,0x22,0x77,0x26,
    0x27,0x74,0x74,0x76,
    0x7b,0x7d,0x7c,0x28,
    0x29,0x2b,0x2a,0x2c,
]
answer = ""
for i in range(32):
    answer += chr((a[i]) ^ i)
print(answer)
