#Imports
import sys
import string

#Opens the specified file, with the argument number, and returns its contents.
def readInput(number):
    with open(sys.argv[number]) as file:
        return file.read();

#Goes through string and checks for alphabetic chars.
def initInput(string):

    #If i is alphabetic, join and replace string.
    string = "".join(i for i in string if i.isalpha());

    #Set all chars in string to lowercase.
    string = string.lower();

    #Return string with a character limit of 512.
    return string[:512];

#Encode the plaintext character with the key character.
def cipher(keyChar, textChar):

    #Get the alphabetical index of each character.
    textIndex = alphabet.index(textChar);
    keyIndex = alphabet.index(keyChar);

    #Return encoded chars index in the alphabet.
    return (keyIndex + textIndex) % 26;

#Print text with 80 chars per line.
def printFormat(text):

    #Loop from 0 - length of the text with a step after 80 increments.
    for i in range(0, int(len(text)), 80):

        #At 0 and after every 80 increments, print the segment of text that comes after the ith char.
        print(text[i:i + 80]);

#Extend the key's length to fill 512 chars.
def fillString(key):

    #Find how many times the key needs to be repeated in order to fill 512 chars.
    multiple = int(512/len(key) + 1);

    #Multiply the key that amount of times.
    res = key * multiple;

    #Return the result with a limit of 512 chars.
    return res[:512];
    
#Get key from command parameter and initialize it.
key = initInput(readInput(1));

#Get plaintext from command parameter and initialize it.
plainText = initInput(readInput(2));

#Create a list of every lowercase letter in the alphabet.
alphabet = list(string.ascii_lowercase);

#Fill the plaintext to 512 chars with x for padding.
for i in range(int(len(plainText)), 512):
    plainText += "x";

#Fill key to 512 chars.
keyStream = fillString(key);

#Encode the plaintext.
cipherText = "";
for i in range(0, 512):
    
    #Pass 1 character at a time. cipher() returns the encoded characters index in the alphabet.
    cipherText += alphabet[cipher(keyStream[i], plainText[i])];

#Print results.
print("\n\nVigenere Key:\n");
printFormat(key);

print("\n\nPlaintext:\n");
printFormat(plainText);

print("\n\nCiphertext:\n");
printFormat(cipherText);