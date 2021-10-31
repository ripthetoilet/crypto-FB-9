from collections import Counter

lulz = ['аы','аь','еэ','жф','жч','жш','жщ','зп','зщ','йь','оы','уы','уь','фц','хщ','цщ','цэ','чщ','чэ','шщ','ьы',]
lang5 = ['ст', 'но', 'ен', 'то', 'на']
AL = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
LE = len(AL)
SQ = LE ** 2

gcd = lambda a, b: a if b == 0 else not a % b and b or gcd(b , a % b)
bisval = lambda bis: (AL.index(bis[0]) * LE + AL.index(bis[1])) % SQ
valbis = lambda val: AL[val // LE] + AL[val % LE]
linequ = lambda x, y, m: x * pow(y, -1, m) % m
encode = lambda bis, key: valbis((key[0] * bisval(bis) + key[1]) % SQ)
decode = lambda bis, key: valbis(((bisval(bis) - key[1]) * pow(key[0], -1, SQ)) % SQ)
bigrams = lambda text: list(dict(sorted(Counter([text[i:i+2] for i in range(0, len(text), 2)]).items(), key=lambda item: item[1], reverse=True)).keys())

with open('01.txt', "r", encoding = "utf-8") as f:
    text = f.read()
text = text.lower()
text1 = "".join([i for i in text if i in AL])
top5 = bigrams(text1)[:5]

def solver(a, b, m):
    a, b = a % SQ, b % SQ
    res = []
    divider = gcd(a, m)
    if gcd(a, m) == 1: 
        if gcd(b, m) != 1: return res
        res.append(linequ(a, b, m))
    else:
        if b % divider == 0:
            a, b, m = int(a / divider), int(b / divider), int(m / divider)
            res.append(linequ(a, b, m))
            while res[-1] + m < m * divider: res.append(res[-1] + m)
    return res

def decrypt(text, keys, lulz):
    for key in keys:
        print(key)
        if key == (789, 372): a = input()
        plain = ''
        for i in range(0, len(text), 2):
            bi = decode(text[i:i+2], key)
            if bi in lulz: break
            plain += bi
            if len(plain) == len(text): return plain
    return 'whoops'

def combos(lst1, lst2):
    keys1 = []
    keys2 = []
    for i in lst1:
        for j in lst2: keys1.append((i, j))
    for i in keys1:
        for j in keys1: keys2.append((i, j))
    return keys2

def getkey(pair):
    x1 = bisval(pair[0][0])
    y1 = bisval(pair[0][1])
    x2 = bisval(pair[1][0])
    y2 = bisval(pair[1][1])
    key = []
    a = solver((y1 - y2) % SQ, (x1 - x2) % SQ, SQ)
    for i in a:
        key.append((i, (y1 - i * x1) % SQ))
    return list(set(key))
    
def allkeys(pairs):
    keys = []
    for i in pairs:
        key = getkey(i)
        if len(key) != 0: 
            if len(key) > 1:
                for j in key: 
                    if gcd(j[0], SQ) == 1: keys.append(j)
            else: 
                if gcd(key[0][0], SQ) == 1: keys.append(key[0])
    return list(set(keys))

print(decrypt(text1, allkeys(combos(lang5, top5)), lulz))