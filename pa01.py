#input with command: python3 pa01.py <key filename>.txt <plaintext filename>.txt

import sys
import string

def readInput(number):
    with open(sys.argv[number]) as file:
        return file.read();

def initInput(string):
    string = "".join(i for i in string if i.isalpha());
    return string.lower();

def cipher(keyChar, textChar):
    textIndex = alphabet.index(textChar);
    keyIndex = alphabet.index(keyChar);
    return (keyIndex + textIndex) % 26;

def printFormat(text):
    for i in range(0, int(len(text)), 80):
        print(text[i:i + 80]);
    print("");
    

key = initInput(readInput(1));
plainText = initInput(readInput(2));
alphabet = list(string.ascii_lowercase);

for i in range(int(len(plainText)), 512):
    plainText += "x";

i = 0;
keyStream = key;
while int(len(keyStream)) < 512:
    if key[i] == None:
        i = 0;
    keyStream += key[i];
    i += 1;

cipherText = "";
for i in range(0, int(len(plainText))):
    cipherText += alphabet[cipher(keyStream[i], plainText[i])];

print("\n\nVigenere Key:\n");
printFormat(key);
print("\nPlaintext:\n");
printFormat(plainText);
print("\nCiphertext:\n");
printFormat(cipherText);