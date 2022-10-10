#!/bin/sh
echo "# BinWalk #"
binwalk anime.jpg 
echo "# Extract Image #"
foremost anime.jpg
mv output/jpg/00000000.jpg ./original_image.jpg
ls -la
echo "\n# Extract ZipFile #"
dd ibs=1 obs=1 skip=506732 if=anime.jpg of=flag.zip
echo "\n# Check The Extracted File #"
file flag.zip
echo "\n# Edit File Header FF4B -> 504B #"
#echo -ne 50 | dd conv=notrunc bs=1 count=1 of=flag.zip
bless flag.zip
echo "\n# Bruteforce Zipfile Password #"
zip2john flag.zip >> crackZip
john crackZip --wordlist=/usr/share/wordlists/rockyou.txt
echo "# Unzip File #"
unzip flag.zip
echo "# Check The Extracted File #"
file flag.txt
echo "# Bruteforce pdf Password #"
perl /usr/share/john/pdf2john.pl flag.txt > pdfCracker
john pdfCracker --wordlist=/usr/share/wordlists/rockyou.txt
