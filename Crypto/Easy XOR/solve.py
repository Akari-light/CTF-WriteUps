#!/usr/bin/python3
ascii_lst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

with open("ciphertext.txt","r") as fr:
	ciphertext = fr.read()
	for i in ascii_lst: 
		flag = i
		
		#-1 as the last character is xor-ed with the 1st character to form N
		for i in range(len(ciphertext) - 1): 
			decrypted_char = chr(ord(ciphertext[i]) ^ ord(flag[i]))
			flag += decrypted_char

		print(flag)