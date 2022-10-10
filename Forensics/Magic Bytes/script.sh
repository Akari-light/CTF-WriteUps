#!/bin/sh
zip -re anime.zip flag.txt
echo -ne \\xFF | dd conv=notrunc bs=1 count=1 of=anime.zip
cat image.jpg anime.zip > anime.jpg
