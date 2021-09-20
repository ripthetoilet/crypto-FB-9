# This is the 1st lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92
import math
from collections import Counter
from tabulate import tabulate


def open_file(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    return text


# Cleaning example text to match the criteria before doing the task
def clean_text(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    #uniqueChars = ''.join(set(text))

    #-----------------------------------------------------
    chars = '.71()-«5d?[“!93286”…—4;»0:],na'
    # -----------------------------------------------------
    for ch in chars:
        text = text.replace(ch, '')

    text = '_'.join([word.strip('\n') for word in text.split()])
    #print(text[:1000])

    with open('exmpl_spaces.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    text = ''.join([word.strip('\n') for word in text.split()])
    # print(text[:1000])

    with open('exmpl_nospaces.txt', 'w', encoding='utf-8') as file:
        file.write(text)


# counting monograms
def count_mono(text):
    res = Counter(text[idx] for idx in range(len(text)))
    res = {x: round(res[x]/len(text), 6) for x in res}
    return dict(res)


# counting bigrams with intersection
def count_bi_intersect(text):
    res = Counter(text[idx: idx + 2] for idx in range(len(text)))
    total_bi = sum(res.values())
    res = {x: round(res[x]/total_bi, 6) for x in res}
    return dict(res)


# counting bigrams with intersection
def count_bi_nointersect(text):
    res = Counter(text[idx: idx + 2] for idx in range(0, (len(text)), 2))
    total_bi = sum(res.values())
    res = {x: round(res[x]/total_bi, 10) for x in res}
    return dict(res)


def find_entropy(freq):
    entropy = 0
    for f in freq.values():
        entropy += - f * math.log(f, 2)

    return entropy


clean_text('exmpl_unformatted.txt')
text_with_spaces = open_file('exmpl_spaces.txt')
text_nospaces = open_file('exmpl_nospaces.txt')

# test and debug

#print(count_mono(text_with_spaces))
mono = count_mono(text_with_spaces)
print("Monograms:")
for key, val in mono.items():
    print(key, ' |', val)
    print('---+-----------')
print('\n')

#print(count_bi_intersect(text_with_spaces))
count_bi_intersect_spaces = count_bi_intersect(text_with_spaces)
print("Bigrams(intersected, with spaces):")
for key, val in count_bi_intersect_spaces.items():
    print(key, '|', val)
    print('---+-----------')
print('\n')

#print(count_bi_nointersect(text_with_spaces))
count_bi_nointersect_spaces = count_bi_nointersect(text_with_spaces)
print("Bigrams(not intersected, with spaces):")
for key, val in count_bi_nointersect_spaces.items():
    print(key, '|', val)
    print('---+-----------')
print('\n')

#print(count_bi_intersect(text_nospaces))
count_bi_intersect_nospaces = count_bi_intersect(text_nospaces)
print("Bigrams(intersected, without spaces):")
for key, val in count_bi_intersect_nospaces.items():
    print(key, '|', val)
    print('---+-----------')
print('\n')

#print(count_bi_nointersect(text_nospaces))
count_bi_nointersect_nospaces = count_bi_nointersect(text_nospaces)
print("Bigrams(not intersected, without spaces):")
for key, val in count_bi_nointersect_nospaces.items():
    print(key, '|', val)
    print('---+-----------')
print('\n')

#entropy
print(find_entropy(mono))