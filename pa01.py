import sys
import string

def readInput(number):
    with open(sys.argv[number]) as file:
        return file.read();

def initInput(string):
    string = "".join(i for i in string if i.isalpha());
    string = string.lower();
    return string[:512];

def cipher(keyChar, textChar):
    textIndex = alphabet.index(textChar);
    keyIndex = alphabet.index(keyChar);
    return (keyIndex + textIndex) % 26;

def printFormat(text):
    for i in range(0, int(len(text)), 80):
        print(text[i:i + 80]);

def fillString(key):
    multiple = int(512/len(key) + 1);
    res = key * multiple;
    return res[:512];
    
key = initInput(readInput(1));
plainText = initInput(readInput(2));
alphabet = list(string.ascii_lowercase);

for i in range(int(len(plainText)), 512):
    plainText += "x";

keyStream = fillString(key);

cipherText = "";
for i in range(0, 512):
    cipherText += alphabet[cipher(keyStream[i], plainText[i])];

print("\n\nVigenere Key:\n");
printFormat(key);

print("\n\nPlaintext:\n");
#print(plainText);
printFormat(plainText);

print("\n\nCiphertext:\n");
printFormat(cipherText);