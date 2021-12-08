import math
import re
import codecs
import random

file = codecs.open("1.txt", "r","utf_8_sig")
text = file.read()
text1 = re.sub(r"[^а-я+ё]+", " ", text.lower()).replace("ё","е").replace(" ", "")

FILE = codecs.open("2.txt", "r","utf_8_sig")
TEXT = FILE.read()
TEXT1 = re.sub(r"[^а-я+ё]+", " ", TEXT.lower()).replace("ё","е").replace(" ", "")
#print(text1)
alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

mass=[]
mass1=[]


def max_leter(text):
    kilkist = []
    for i in alphabet:
        letter = text.count(i)
        kilkist.append(letter)
    #print(max(kilkist))
    index_letter=kilkist.index(max(kilkist))
    return index_letter

def rand_key():
    print('Enter length of key:')
    len=int(input())
    i=0
    while i<len:
        a=random.randint(0,32)
        symbol=alphabet[a]
        mass.append(symbol)
        i+=1
    key = ''.join(mass)
    print(key)
    return key


def encrypt (text, key):
    keyindexes = []
    ciphertext = []
    for i in range(len(key)):
        keyindex = alphabet.index(key[i])
        keyindexes.append(keyindex)

    for i in range(len(text)):
        EnterTextIndes = alphabet.index(text[i])
        KeyIndex = keyindexes[i % len(keyindexes)]
        EncodLeter = (KeyIndex + EnterTextIndes) % len(alphabet)
        ciphertext.append(alphabet[EncodLeter])

    cipheredtext = ''.join(ciphertext)
    print("\nEncrypted text:" , cipheredtext)
    return cipheredtext

def decrypt (text, key):
    keyindexes = []
    entrancetext = []
    for i in range(len(key)):
        keyindex = alphabet.index(key[i])
        keyindexes.append(keyindex)

    for i in range(len(text)):
        CipherTextIndex = alphabet.index(text[i])
        KeyIndex = keyindexes[i % len(keyindexes)]
        DecodLeter = (CipherTextIndex - KeyIndex + len(alphabet)) % len(alphabet)
        entrancetext.append(alphabet[DecodLeter])

    entrancedtext = ''.join(entrancetext)
    print("\nDecrypted text:", entrancedtext)
    return entrancedtext


def compliance_index(text):
    Kilkist=[]

    for i in alphabet:
        N=text.count(i)
        n=N-1
        Kilkist.append(N*n)
    summ=sum(Kilkist)
    ind=summ/(len(text)*(len(text)-1))
    return ind

def makeBlocks(text, r):              
    blocks = []
    comp_index_blocks = []
    for i in range(r):
        blocks.append(text[i::r])
        comp = compliance_index(blocks[i])
        comp_index_blocks.append(comp)
    print("Len of key:", r,"Compliance index for all bloсks:",sum(comp_index_blocks)/r)
    
    return blocks 

def MakeKey (text, r, letter):
    keys = []
    blocks = makeBlocks(text, r)
    for i in range(len(blocks)):
        maxcount = max_leter(blocks[i])
        key = (maxcount - alphabet.index(letter)) % len(alphabet)
        keys.append(alphabet[key])
    key = ''.join(keys)
    return key

# main part
def main():
#key1 = rand_key()
#makeBlocks(TEXT,len(key1))
#en = encrypt(text1, key1)
#dec = decrypt(en, key1)
#print("\nCompliance index for our random text:",compliance_index(en))
#print("\nCompliance index for our variant:",compliance_index(TEXT1))
    print("\nCompliance index for open text:",compliance_index(text1))
    for r in range(1,len(alphabet)):
        makeBlocks(TEXT1, r)
#print("\nНайчастіше зустрічається у зашифрованому тексті:",alphabet[max_leter(TEXT1)])
    print("\nНаш ключ:",MakeKey(TEXT1,12,'о'))
    print("\nЗашифрований текст:", TEXT1)
    decrypt(TEXT1,'вшекспирбуря')
#decoded_file=codecs.open('3.txt',"w","utf_8_sig")
#decoded_file.write(decrypt(TEXT1,'вшекспирбуря'))

if __name__ = "__main__":
    main()
