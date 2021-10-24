import random

with open('firstText.txt','r',encoding='utf-8') as file:
    text1 = file.read()
with open('TexttoDecrypt.txt','r',encoding='utf-8') as file2:
    toDecrypt = file2.read()
alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']


def encode(text, key):                              # функція кодування
    encryptedText = []

    keysIndex=[]
    for i in key :
        keysIndex.append(alphabet.index(i))

    for i in range(len(text)):
        letterToEncrypt = alphabet.index(text[i])
        keyIndex = keysIndex[i%len(keysIndex)]
        encryptedLetter = (keyIndex+letterToEncrypt)%len(alphabet)
        encryptedText.append(alphabet[encryptedLetter])
    return ''.join(encryptedText)


def decode (text,key):                              # функція декодування
    encryptedText = []

    keysIndex=[]
    for i in key :
        keysIndex.append(alphabet.index(i))

    for i in range(len(text)):
        letterToEncrypt = alphabet.index(text[i])
        keyIndex = keysIndex[i%len(keysIndex)]
        encryptedLetter = (letterToEncrypt-keyIndex)%len(alphabet)
        encryptedText.append(alphabet[encryptedLetter])
    return ''.join(encryptedText)

def keyGen(lenght):                                 # геренування ключів
    key=""                                          # різної довжини
    for i in range(lenght):
        key+=alphabet[random.randint(0,len(alphabet)-1)]
    print("key:",key)
    return key


def complianceIndex(text):                          # пошук індексу відповідності
    ind = 0;
    n=len(text)
    for i in range(len(alphabet)):
        letterCount=text.count(alphabet[i])
        ind+=letterCount*(letterCount-1)
    ind*=1/(n*(n-1))
    return ind


def task1(text):                                    # функція для завдання 1
    print("Compilance index start= ", complianceIndex(text))
    print(" ")

    for i in range(2,6):
        print("Key len = ",i)
        key=keyGen(i)
        enc=encode(text,key)
        print("Encoded text: ",enc)
        print("Decoded text: ",decode(enc,key))
        print("Compilance index: ",complianceIndex(enc))
        print(" ")
    for i in range(10,21):
        print("Key len = ", i)
        key = keyGen(i)
        enc = encode(text, key)
        print("Encoded text: ", enc)
        print("Decoded text: ", decode(enc, key))
        print("Compilance index: ", complianceIndex(enc))
        print(" ")


def makeBlocks(text, len):              # розбити текст на блоки
    blocks = []
    for i in range(len):
        blocks.append(text[i::len])
    return blocks


def indexForBlocks(text, size):         # порахувати для кожного блоку
    blocks = makeBlocks(text, size)     # cвій індекс відповідності
    index = 0
    for i in range(len(blocks)):
        index=index+complianceIndex(blocks[i])
    index=index/len(blocks)
    return index


def getIndexForBlocks ( ):              # вивести індекси відповідності
    for i in range (1,len(alphabet)):   # для ключів різних довжин
        print('Key len =',i,'index=',indexForBlocks(toDecrypt,i))


def MakeKey(text, size, letter):        # функція для знаходження ключа
    blocks=makeBlocks(text, size)       # на вхід дається текст,розмір блоку
    key = ""                            # та літера яка є серед частих
    for i in range(len(blocks)):
        mostFr = max(blocks[i], key=lambda c: blocks[i].count(c))
        key+=alphabet[(alphabet.index(mostFr)-alphabet.index(letter))%len(alphabet)]
    return key


if __name__ == "__main__":

    task1(text1)                        #перша частина
    print('')
    getIndexForBlocks()                 #індекси відповідностей для блоків
    print('')                           #різної довжини ШТ
    key = MakeKey(toDecrypt, 16, "о")   # пункт вище показав що ключ має довжину 16
    key = 'делолисоборотней'            # трішки підкоригувавши отриманий ключ отримали
    decoded = (decode(toDecrypt, key))  # його та декодували весь текст
    print(decoded)

    key = MakeKey(toDecrypt,16,"о")         # пункт вище показав що ключ має довжину 16
    key = 'делолисоборотней'                # трішки підкоригувавши отриманий ключ отримали
    decoded=(decode(toDecrypt,key))         # його та декодували весь текст
    print(decoded)
