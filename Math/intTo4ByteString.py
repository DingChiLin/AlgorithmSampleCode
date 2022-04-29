# intuition
def int2str(x):
    code = ""
    for _ in range(4):
        code += chr(x & 255) # 255 = 0xff
        x >>= 8
    return code[::-1]

def str2int(s):
    res = 0
    for ch in s:
        res = res * 256 + ord(ch)
    return res

print(str2int(int2str(8024745)))