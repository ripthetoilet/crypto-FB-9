import itertools
from collections import Counter
import pandas as pd


# Alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#             'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
Alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
Alphabet = list(Alphabet)
with open("01.txt", 'r') as f1:
    text = f1.read().lower().replace("ъ", "ь").replace("ё", "е").replace("\n", "")
top_ru_birgams = ['ст', 'но', 'то', 'на', 'ен']

lenght = len(Alphabet)


# bigrams
def bigram(text):
    arr2 = []
    i = 0
    while i < len(text) - 1:
        arr2.append(text[i]+text[i+1])
        i += 2
    return arr2


bigram1 = Counter(bigram(text))


# bigram frequancy
def bigram_frequancy(bigram):
    bigramfreq=[]
    for i in bigram:
        bigramfreq.append(bigram[i]/sum(bigram.values()))
        # print(bigramfreq)
    return bigramfreq


# таблиця із топ5 біграм
def PrintBigramTop(bigram):
    dic=dict(list(zip(bigram, bigram_frequancy(bigram))))
    sorted_keys= sorted(dic, key=dic.get, reverse=True)[:5]
    sorted_dict = {}
    for i in sorted_keys:
        sorted_dict[i] = dic[i]
    data=pd.DataFrame.from_dict(sorted_dict, 'index')
    #print(sorted_dict)
    #print(tabulate(data, headers='keys', tablefmt='grid'))
    return sorted_dict


# gcd
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# обернений елемент
def modular_multiplicative_inverse(elem, mod):
    if gcd(elem, mod) == 1:
        for x in range(0, mod - 1):
            ans = (elem * x) % mod
            if ans == 1:
                return x
    else:
        return -1


#test
def linear_equation(a, b, n):
    d = gcd(a, n)
    rev_a = modular_multiplicative_inverse(a, n)
    x = []
    if d == 1:
        x.append((rev_a * b) % n)
        return x
    else:
        if b % d == 0:
            a1, b1, n1 = a/d, b/d, n/d
            x0 = linear_equation(a1, b1, n1)
            for i in range(0, d):
                x.append(x0[0] + i * n1)
            return x
        else:
            return -1


def bigram_num(bgrm):
    return len(Alphabet) * Alphabet.index(bgrm[0]) + Alphabet.index(bgrm[1])


def bigram_txt(num):
    return Alphabet[num // len(Alphabet)] + Alphabet[num % len(Alphabet)]


def decrypt(a, b, text):
    decrypted_text = ""
    rev_a = modular_multiplicative_inverse(a, len(Alphabet)**2)
    for i in range(0, len(text), 2):
        y = bigram_num(text[i] + text[i+1])
        x = (rev_a*(y-b)) % len(Alphabet)**2
        decrypted_text += bigram_txt(x)
    return decrypted_text


def check():
    pass


def find_key():
    pass

print(PrintBigramTop(bigram1))

