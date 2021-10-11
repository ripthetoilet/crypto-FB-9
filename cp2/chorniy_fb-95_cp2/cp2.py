from collections import Counter

al = 'йцукенгшщзхэждлорпавыфячсмитьбю'
with open('text.txt',"r",encoding = "utf-8") as f:
    text = f.read()
text = text.lower()
text1 = ''.join([i for i in text if i in al]) 

def encrypt(text, key):
    ct = []
    for pos, char in enumerate(text):
        mi = al.index(char)
        ki = al.index(key[pos % len(key)])
        ct.append(al[(mi + ki) % len(al)])
    return ''.join(ct)


def decrypt(ct, key):
    mt = []
    for pos, char in enumerate(ct):
        ci = al.index(ct[pos % len(ct)])
        ki = al.index(key[pos % len(key)])
        mt.append(al[(ci - ki + len(al)) % len(al)])
    return ''.join(mt)

def acrdindx(text):
    dic = Counter(text)
    ind = 0
    for i in dic:
        ind += dic[i] * (dic[i] - 1)
    ind /= (len(text) * (len(text) - 1))
    return ind

with open("r2.txt", "w", encoding='utf-8') as e:
    e.write(encrypt(text1, 'да'))

print("accordence index with keu length of 2: ", acrdindx(encrypt(text1, 'да')))

with open("r3.txt", "w", encoding='utf-8') as e:
    e.write(encrypt(text1, 'кот'))

print("accordence index with keu length of 3: ", acrdindx(encrypt(text1, 'кот')))

with open("r4.txt", "w", encoding='utf-8') as e:
    e.write(encrypt(text1, 'маша'))

print("accordence index with keu length of 4: ", acrdindx(encrypt(text1, 'маша')))

with open("r5.txt", "w", encoding='utf-8') as e:
    e.write(encrypt(text1, 'толик'))

print("accordence index with keu length of 5: ", acrdindx(encrypt(text1, 'толик')))

with open("r15.txt", "w", encoding='utf-8') as e:
    e.write(encrypt(text1, 'япишулабуночью'))

print("accordence index with keu length of 14: ", acrdindx(encrypt(text1, 'япишулабуночью')))