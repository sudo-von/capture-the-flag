import socketserver
import random
import base64
import string
import secrets
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from itertools import combinations_with_replacement as comb

def encrypt(iv,key,msg):
    cipher = AES.new(bytes(key,"utf-8"),AES.MODE_CBC,bytes(iv,"utf-8"))
    los_bytes = cipher.encrypt(pad(bytes(msg,"utf-8"),AES.block_size,style="pkcs7"))
    return base64.b64encode(los_bytes)

def decrypt(iv,key,msg):
    try:
        ciphertext = base64.b64decode(msg)
        cipher = AES.new(bytes(key,"utf-8"),AES.MODE_CBC,iv.encode("utf8"))
        el_string = unpad(cipher.decrypt(ciphertext),AES.block_size,style="pkcs7")
        return str(el_string,"ascii")
    except:
        return "Padding Error"

def xor(a,b):
    xored = []
    for i in range(max(len(a), len(b))):
        xored_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        xored.append(hex(xored_value)[2:])
    return ''.join(xored)

if __name__ == "__main__":
    chars = string.ascii_uppercase + string.digits
    key = "AAAAAAAAAAAAAAAA"
    msg = "flipid=6"
    iv = "\x41"*16 #A*16
    for id in range(7):
        m = msg[:7]+str(id)
        c = encrypt(iv,key,m)
        print(c,m)
        for pos in range(16):
            b = list(base64.b64decode(c))
            for i in range(256):
                #b[pos] = i
                #r = base64.b64encode(bytes(b))
                try:
                    iv = bytearray(iv,'utf-8')
                    iv[pos] = i
                    iv = iv.decode("utf-8")
                    d = decrypt(iv,key,b)
                    if d != "Padding Error" and d != m:
                        print(d, pos, i, iv)
                        break
                except Exception as e:
                    pass
    """chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
    cipher = "JBBceKLgirsuFkLqg3AOXQ=="
    for i in range(256):
        base = base64.b64decode(cipher)
        base = base[:5]+bytes([i])+base[6:]
        base = base64.b64encode(base)
        #print(base)
        d = decrypt(iv,key,base)
        if d != "Padding Error":
            print(d, i)"""