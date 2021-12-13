from collections import Counter
from itertools import combinations
import re


def Read_text(filename):
    with open(filename, 'r', encoding = 'utf-8') as fin:
        return fin.read()


def Write_text(filename, text):
    with open(filename, 'w', encoding = 'utf-8') as fout:
        fout.write(text)


def Clear_text(text):
    cleared_text = text.replace('\n', ' ').replace('\r', ' ').replace('ё', 'е').replace('ъ', 'ь').lower()
    cleared_text = re.sub('[^а-я]', '', cleared_text)
    return cleared_text


def Get_freq(text):
    return dict(Counter(text).most_common())


def Char_int(char):
    int = ord(char) - 1072
    if (char >= 'ъ'):
        int = int - 1
    return int


def Int_char(int):
    if (int >= 26):
        int = int + 1
    char = chr(int + 1072)
    return char


def Bigram_int(bigram):
    return Char_int(bigram[0]) * 31 + Char_int(bigram[1])


def Int_bigram(int):
    return Int_char(int // 31) + Int_char(int % 31)


def Get_bigrams(text):
    if len(text) % 2 != 0:
        text = text + 'ф'
    return re.findall('..', text)


def Get_gcd(num, mod):
    if num == 0:
        return (mod, 0, 1)
    else:
        g, u, v = Get_gcd(mod % num, num)
        return (g, v - (mod // num) * u, u)


def Get_reverse(num, mod):
    g, u, _ = Get_gcd(num, mod)
    if g == 1:
        return (u % mod + mod) % mod
    else:
        return -1


def Decrypt(text, a, b):
    bigrams = Get_bigrams(text)
    decrypted = ''
    for bigram in bigrams:
        Y = Bigram_int(bigram)
        X = (Get_reverse(a, 31 * 31) * (Y - b)) % (31 * 31)
        decrypted = decrypted + Int_bigram(X)
    return decrypted


def Get_top5(bigrams):
    freq = Get_freq(bigrams)
    top5 = list(freq)[:5]
    top5_encrypted = []
    for item in top5:
        top5_encrypted.append(item)
    return top5_encrypted


def Lenguage_check(text):
    if (text.count('о') / len(text)) < 0.1 or (text.count('а') / len(text)) < 0.07:
        return -1
    else:
        return 1


def Solve_equation(XXX, YYY, mod):
    gcd, _, _ = Get_gcd(XXX, mod)
    if gcd == 1:
        XXX_reversed = Get_reverse(XXX, mod)
        a = (XXX_reversed * YYY) % mod
        return a
    elif (YYY % gcd != 0):
        return -1
    else:
        a = Solve_equation(int(XXX / gcd), int(YYY / gcd), int(mod / gcd))
        return a


def Attack(text):
    bigrams = Get_bigrams(text)

    top5_theoretical = []
    for bigram in ['ст', 'но', 'то', 'на', 'ен']:
        top5_theoretical.append(Bigram_int(bigram))

    top5_encrypted = []
    for bigram in Get_top5(bigrams):
        top5_encrypted.append(Bigram_int(bigram))

    xp = list(combinations(top5_theoretical, 2))
    yp = list(combinations(top5_encrypted, 2))

    for Y_pair in yp:
        Y = Y_pair[0]
        YY = Y_pair[1]
        YYY = (Y - YY) % (31 * 31)
        for X_pair in xp:
            X = X_pair[0]
            XX = X_pair[1]
            XXX = (X - XX) % (31 * 31)

            a = Solve_equation(XXX, YYY, 31 * 31)
            if a != -1:
                b = (Y - a * X) % (31 * 31)
                if (Lenguage_check(Decrypt(text, a, b)) == 1):
                    return [a, b]


# ШЛЯХИ
TEXT_ENCRYPTED = 'encrypted\\var3.txt'
TEXT_DECRYPTED = 'decrypted\\var3.txt'
# ШЛЯХИ

encrypted = Clear_text(Read_text(TEXT_ENCRYPTED))
print('Шифрований текст:\n' + encrypted)

key = Attack(encrypted)
if len(key) == 2:
    print('\nКлюч: а = ' + str(key[0]) + ', b = ' + str(key[1]))
    decrypted = Decrypt(encrypted, key[0], key[1])
    print('\nДешифрований текст:\n' + decrypted)
    Write_text(TEXT_DECRYPTED, decrypted)
else:
    print('\nНа жаль, знайти ключ не вдалось.')
