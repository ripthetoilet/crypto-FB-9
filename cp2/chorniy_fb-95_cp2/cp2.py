al = 'йцукенгшщзхэждлорпавыфячсмитьбю'
f = open('text.txt',"r",encoding = "utf-8")
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

e = open("r2.txt", "w", encoding='utf-8')
encoded = encrypt(text1, 'да')
e.write(encoded)
e.close()
e = open("r3.txt", "w", encoding='utf-8')
encoded = encrypt(text1, 'кот')
e.write(encoded)
e.close()
e = open("r4.txt", "w", encoding='utf-8')
encoded = encrypt(text1, 'маша')
e.write(encoded)
e.close()
e = open("r5.txt", "w", encoding='utf-8')
encoded = encrypt(text1, 'толик')
e.write(encoded)
e.close()