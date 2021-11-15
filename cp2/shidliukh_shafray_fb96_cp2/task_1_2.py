from collections import Counter
import matplotlib.pyplot as plt
letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

file = open("open", encoding="utf-8")
VT = file.read().lower().replace("ё", "е").replace(" ", "").replace("!", "").replace(",", "").replace(".", "")\
    .replace("—","").replace(";","").replace(":","").replace("\n","").replace("-","")

keys = ['фб', 'нос', 'макс', 'илюша', 'яиграювдотудва']

def encryption(text, key):
    encrypt = []
    index_key = [letters.index(i) for i in key]
    for index, char in enumerate(text):
        encrypt.append(letters[(letters.index(char)+index_key[index % len(key)]) % len(letters)])
    return "".join(encrypt)


def index_vidpovidnosti(text):
    dictionary=Counter(text)
    index_Vidp=0
    for i in dictionary:
        index_Vidp+=dictionary[i]*(dictionary[i]-1)
    return index_Vidp/(len(text)*(len(text)-1))


def get_blocks(text, kol):
    b = []
    for i in range(0, kol):
        s = ''
        for j in range(i, len(text), kol):
            s += text[j]
        b.append(s)
    return b


def len_index(text):
    d = {}
    for blocklen in range(2, 32):
        temp = 0
        blocks = get_blocks(text, blocklen)
        for block in blocks:
            temp += index_vidpovidnosti(block)
        d[blocklen] = temp/blocklen
    return d

print(VT,"\n","bez wifra",index_vidpovidnosti(VT),"\n")

for key in keys:
    print('Key= '+key,len(key),"\n"+encryption(VT, key)+"\n"+"index vidpovidnosti:")
    print(len_index(encryption(VT, key)).values())
    y = list(len_index(encryption(VT, key)).values())
    x=list(len_index(encryption(VT, key)).keys())
    fig, ax = plt.subplots()
    ax.plot(x ,y)
    plt.title(key)
    ax.set_xlabel('довжина ключа')
    ax.set_ylabel('індекс відповідності')
    plt.grid(which='major')
    plt.minorticks_on()
    fig.set_figwidth(10)
    fig.set_figheight(6)
    plt.grid(which='minor', color = 'gray', linestyle = ':')
    plt.show()
