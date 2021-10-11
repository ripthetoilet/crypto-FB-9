from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
al=dict((alphabet[i], i) for i in range(len(alphabet)))
dic = {}
for i in range(len(alphabet)):
    dic[i] = alphabet[i]
cid = dict((v, k) for k, v in dic.items())

with open('text.txt', "r", encoding = "utf-8") as f:
    text = f.read()
text = text.lower()
text1 = "".join([i for i in text if i in alphabet])

with open('etext.txt', "r", encoding = "utf-8") as f:
    etext = f.read()
etext = etext.replace('\n', '')

mean = lambda x: sum(x) / len(x)

def acrdindx(al, text):                                                #calculating the accordance index
    ind = 0
    for i in al:
        ind += al[i] * (al[i] - 1)
    ind /= (len(text) * (len(text) - 1))
    return ind

def crack(etext, text, al):
    expvl = 0
    dct = {}
    for i in text:
        if (i in alphabet):
            al[i] += 1                                                  #calculating letter frequency
    for i in alphabet:
        al[i] /= len(text)                                              #calculating letter probability
        expvl += pow(al[i], 2)                                          #calculating the expected value of accordance index
    for r in range(2, 33):
        lst = []
        for j in range(r):
            tmp = ""
            for i in range(j, len(etext), r):
                tmp += etext[i]                                         #creating blocks to find closest accordance index
            tmpfrq = Counter(tmp)
            lst.append(acrdindx(tmpfrq, tmp))                           #adding accordance index of every possible block
        dct[r] = mean(lst)                                              #mean value of accordance indexes
    for key in dct.keys():
        dct[key] = abs(dct[key] - expvl)                                #finding closest accordance index
    keylen = min(dct, key=dct.get)                                      #getting key length
    key = ''
    for k in range(keylen):
        tmp = []
        for i in range(k, len(etext), keylen):
            tmp.append(etext[i])                                        #splitting ciphertext in certain number of blocks
        lets = Counter(tmp)
        popular = max(lets, key=lets.get)                               #finding most common letter in block
        key += dic[(cid[popular] - 14) % 32]                            #using most common letter in language
    print(key)
    return key

def clean(key):                                                         #if some letters do not fit in key
    stop = 0
    poplet = ['е', 'а', 'н', 'т', 'и']                                  #top common letters in language
    print("is key ok? (y/n)")
    if (input() == "y"):
        print("ok!")
        return key
    else:
        keya = list(key)
        print("which letter is not correct?")
        letter = input()
        tmp = keya.index(letter)
        i = 0
        while stop == 0:
            keya[tmp] = dic[(cid[letter] + 14 - cid[poplet[i]]) % 32]   #inversing to most common in block and using less common letter
            print(''.join(keya))
            print("correct now? (y/n)")
            if input() == 'y': return ''.join(keya)
            else: i += 1
            if i == 5: 
                print("someting went wrong :(")
                return ''.join(keya)

def decode(ct, key):
    mt = []
    for pos, char in enumerate(ct):
        ci = alphabet.index(ct[pos % len(ct)])
        ki = alphabet.index(key[pos % len(key)])
        mt.append(alphabet[(ci - ki + len(alphabet)) % len(alphabet)])
    return ''.join(mt)

key = crack(etext, text1, al)

key = clean(key)

print(key)

print(decode(etext, key))