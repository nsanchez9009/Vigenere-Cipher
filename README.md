# Vigenère cipher encoder

Encrypt the alphabetic letters in a file using the Vigenère cipher. pa01.py receives input through two command line parameters containing, first, the name of the encryption key file, and second, the name of the plaintext file to be encrypted. The max length of the plaintext is 512 characters. All non alphabetic characters are ignored, including white spaces. You may input text longer than 512 characters but whatever is exceeding the limit, after removing white spaces and non alphabetic characters, will be removed. Output is displayed in the terminal.

<h4>run with command:</h4>

<code>python pa01.py [key filename].txt [plaintext filename].txt</code>

or

<code>python3 pa01.py [key filename].txt [plaintext filename].txt</code>

---

<h4>Example using included text files; keyTest.txt and plaintextTest.txt</h4>

<h5>Key:</h5>
I think and think for months and years. Ninety-nine times, the conclusion is false. The hundredth time I am right. - Albert Einstein Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution. - Albert Einstein

<h5>Plaintext:</h5>
"Fall in love with some activity, and do it! Nobody ever figures out what life is all about, and it doesn't matter. Explore the world. Nearly everything is really interesting if you go into it deeply enough. Work as hard and as much as you want to on the things you like to do the best. Don't think about what you want to be, but what you want to do. Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all." - Richard Feynman

<h5>Output:</h5>
```
Vigenere Key:

ithinkandthinkformonthsandyearsninetyninetimestheconclusionisfalsethehundredthti
meiamrightalberteinsteinimaginationismoreimportantthanknowledgeforknowledgeislim
itedwhereasimaginationembracestheentireworldstimulatingprogressgivingbirthtoevol
utionalberteinstein


Plaintext:

fallinlovewithsomeactivityanddoitnobodyeverfiguresoutwhatlifeisallaboutanditdoes
ntmatterexploretheworldnearlyeverythingisreallyinterestingifyougointoitdeeplyeno
ughworkashardandasmuchasyouwanttoonthethingsyouliketodothebestdontthinkaboutwhat
youwanttobebutwhatyouwanttodokeepupsomekindofaminimumwithotherthingssothatsociet
ydoesntstopyoufromdoinganythingatallrichardfeynmanxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Ciphertext:

ntstvxlbyxdqgrxcdqopmpnigbyrdugvbasumqgrzxzrmynyiuchvhbsbzvnwnsldptisbnnqumwwvxa
zxuafkmxlqpwpvvmlmjgkplammrrgrvxzmgpazuzwzqpzcriamxyefdvbctjbuylczxgceehhkttqpva
czlzkyorwhszpatlnsfcqueezfuyefmassampvxdwervqhcxcvemwquiyshvwlvuvobuoosruvnhacoe
shcknneussxfcgoaeblwndiadtbghrmrzzdjaardpfdbiyqieazczabruwglxzflagnwucgjlnkwqvml
ddzwwgawaicbfyikvflamvgmegzobnrbxrepzvuaezqnqytunnqflkfpjlobfjmloqxkqqexkhkltiba
dbclohkltibadbfpifjfqbatebobxpfjxdfkxqflkbjyoxzbpqebbkqfobtloiapqfjrixqfkdmoldob
ppdfsfkdyfoqeqlbslirqflkxiyboqbf
```