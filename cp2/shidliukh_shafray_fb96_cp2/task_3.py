from collections import Counter
import matplotlib.pyplot as plt

letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
file = open("wifr", encoding="utf-8")
VT = file.read().replace("\n", "").replace(" ", "")


def index_vidpovidnosti(text):
    dictionary = Counter(text)
    index_vidp = 0
    for i in dictionary:
        index_vidp += dictionary[i]*(dictionary[i]-1)
    return index_vidp/(len(text)*(len(text)-1))


def decryption(text, k):
    decr = []
    index_key = [letters.index(i) for i in k]
    for index, char in enumerate(text):
        decr.append(letters[(letters.index(char)-index_key[index % len(k)])%len(letters)])
    return "".join(decr)


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


def popular(text, key_len):
    l = []
    blocks = get_blocks(text, key_len)
    for block in blocks:
        l.append(Counter(block).most_common(1)[0][0])
    return l


def key_find(s):
    k = ''
    for i in range(len(s)):
        k += letters[(letters.index(s[i])-14) % 32]
    return k


y = list(len_index(VT).values())
x=list(len_index(VT).keys())
fig, ax = plt.subplots()
ax.plot(x ,y)
plt.title('Пошук довжини ключа')
ax.set_xlabel('довжина ключа')
ax.set_ylabel('індекс відповідності')
plt.grid(which='major')
plt.minorticks_on()
fig.set_figwidth(10)
fig.set_figheight(6)
plt.grid(which='minor', color = 'gray', linestyle = ':')
plt.show()
print(max(len_index(VT).values()), ":", max(len_index(VT), key=len_index(VT).get))
print(popular(VT, max(len_index(VT), key=len_index(VT).get)))
print(key_find(popular(VT, max(len_index(VT), key=len_index(VT).get))))
key = input()
print(decryption(VT, key))
