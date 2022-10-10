#!/usr/bin/python3
import base64

base64_flag = 'TllQe1gwcl9pNV8zNHN5fQ=='
base64_bytes = base64_flag.encode('ascii')
flag_bytes = base64.b64decode(base64_bytes)
flag = flag_bytes.decode('ascii')

ciphertext = ""

for i in range(len(flag)):
    encrypted_char = chr(ord(flag[i]) ^ ord(flag[(i + 1) % len(flag)]))
    ciphertext += encrypted_char

f = open("ciphertext.txt","w+")
f.write(ciphertext)
f.close()