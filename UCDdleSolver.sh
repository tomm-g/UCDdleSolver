#!/bin/bash

wget https://ucddle.tk/script.js

echo "Script Downloaded!"

mv script.js script.txt

echo "Script Converted to Text File!"


echo "Executing Python Script..."

python3 ~/Code/Bash/solverAssist.py

echo "Deleting Uneeded Text Files..."

rm encodedAns.txt script.txt
