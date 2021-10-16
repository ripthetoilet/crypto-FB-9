import random

with open('firstText.txt','r',encoding='utf-8') as file:
    text1 = file.read()

alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']

#функція шифрування
def encode (text,key):
    encryptedText = ""

    keysIndex=[]
    for i in key :
        keysIndex.append(alphabet.index(i))

    for i in range(len(text)):
        letterToEncrypt = alphabet.index(text[i])
        keyIndex = keysIndex[i%len(keysIndex)]
        encryptedLetter = (keyIndex+letterToEncrypt)%len(alphabet)
        encryptedText+=alphabet[encryptedLetter]
    return encryptedText

#функція розшифрування
def dencode (text,key):
    encryptedText = ""

    keysIndex=[]
    for i in key :
        keysIndex.append(alphabet.index(i))

    for i in range(len(text)):
        letterToEncrypt = alphabet.index(text[i])
        keyIndex = keysIndex[i%len(keysIndex)]
        encryptedLetter = (letterToEncrypt-keyIndex+len(alphabet))%len(alphabet)
        encryptedText+=alphabet[encryptedLetter]
    return encryptedText

def keyGen(lenght):
    key=""
    for i in range(lenght):
        key+=alphabet[random.randint(0,len(alphabet)-1)]
    print("key:",key)
    return key

#функція пошуку індексу відповідності
def complianceIndex(text):
    sum = 0;
    for i in range(len(alphabet)):
        letterCount=text.count(alphabet[i])
        sum+=(letterCount*(letterCount-1))

    index = sum / (len(text)*(len(text)-1))
    return index

def task1(text):
    print("Compilance index start= ",complianceIndex(text))
    print(" ")

    for i in range(2,6):
        print("Key len = ",i)
        key=keyGen(i)
        enc=encode(text,key)
        print("Encoded text: ",enc)
        print("Decoded text: ",dencode(enc,key))
        print("Compilance index: ",complianceIndex(enc))
        print(" ")
    for i in range(10,21):
        print("Key len = ", i)
        key = keyGen(i)
        enc = encode(text, key)
        print("Encoded text: ", enc)
        print("Decoded text: ", dencode(enc, key))
        print("Compilance index: ", complianceIndex(enc))
        print(" ")

task1(text1)
