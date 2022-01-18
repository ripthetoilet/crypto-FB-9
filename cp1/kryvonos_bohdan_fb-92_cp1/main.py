import math
from collections import Counter
import re

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
            'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']


def TextFormater(fl):
    i = 0
    text = ""
    with open("text.txt", encoding='utf-8') as f:
        text = f.read().lower().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('ё', 'е').replace('ъ', 'ь')
        NewText = ""
        if ' ' in alphabet:
            alphabet.remove(' ')
        length = len(text)
        if fl:
            alphabet.append(' ')
        while i < length - 1:
            if text[i] in alphabet:
                NewText += text[i]
            i += 1
        if fl:
            NewText = re.sub(r'\s+', ' ', NewText)
    return NewText


def SetingBigrams(st, text):
    i = 0
    BigramDict = {}
    length = len(text)
    while i < length - st:
        if (text[i] + text[i + st]) not in BigramDict:
            BigramDict[text[i] + text[i + st]] = 1
        else:
            BigramDict[text[i] + text[i + st]] += 1
        i += st
    return BigramDict


def EntropyCount(x, length, n):
    entropy = 0
    for i in x:
        t = x[i] / length
        entropy -= t * math.log(t, 2)
    return entropy / n


letter = Counter(TextFormater(True))

bg_step1 = SetingBigrams(1, TextFormater(True))
bg_step2 = SetingBigrams(2, TextFormater(True))

print('Entropy for letters: ', EntropyCount(letter, sum(letter.values()), 1))
print('Entropy for bigrams with step 1: ', EntropyCount(bg_step1, sum(bg_step1.values()), 2))
print('Entropy for bigrams with step 2: ', EntropyCount(bg_step2, sum(bg_step2.values()), 2))

length = len(TextFormater(True))
f1 = open('letters_frequency.txt', 'w')
for i in alphabet:
    f1.write(i + ": " + str(letter[i] / length) + "\n")
f1.close()

f2 = open('frequency_step_1_without_spaces.txt', 'w')
length = len(TextFormater(False))
bg_step1 = SetingBigrams(1, TextFormater(False))
for i in alphabet:
    for j in alphabet:
        bg = i + j
        if bg in bg_step1:
            p = bg_step1[bg] / length
            f2.write(bg + ": " + (str('%.6f' % p) + " ") + "\n")
f2.close()

f3 = open('frequency_step_1_with_spaces.txt', 'w')
length = len(TextFormater(True))
bg_step1 = SetingBigrams(1, TextFormater(True))
for i in alphabet:
    for j in alphabet:
        bg = i + j
        if bg in bg_step1:
            p = bg_step1[bg] / length
            f3.write(bg + ": " + (str('%.6f' % p) + " ") + "\n")
f3.close()

bg_step2 = SetingBigrams(2, TextFormater(False))
f4 = open('frequency_step_2_without_spaces.txt', 'w')
length = len(TextFormater(False))
for i in alphabet:
    for j in alphabet:
        bg = i + j
        if bg in bg_step2:
            p = bg_step2[bg] / length
            f4.write(bg + ": " + (str('%.6f' % p) + " ") + "\n")
f4.close()

bg_step2 = SetingBigrams(2, TextFormater(True))
f5 = open('frequency_step_2_with_spaces.txt', 'w')
length = len(TextFormater(True))
for i in alphabet:
    for j in alphabet:
        bg = i + j
        if bg in bg_step2:
            p = bg_step2[bg] / length
            f5.write(bg + ": " + (str('%.6f' % p) + " ") + "\n")
f5.close()