# This is the 1st lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92
import math
from collections import Counter
import tabulate


def open_file(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    return text


# Cleaning example text to match the criteria before doing the task
def clean_text(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    #uniqueChars = ''.join(set(text))

    chars = '.71()-«5d?[“!93286”…—4;»0:],'
    for ch in chars:
        text = text.replace(ch, '')

    text = ' '.join([word.strip('\n') for word in text.split()])
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
    return res


# counting bigrams with intersection
def count_bi_intersect(text):
    res = Counter(text[idx: idx + 2] for idx in range(len(text)))
    return dict(res)


# counting bigrams with intersection
def count_bi_nointersect(text):
    res = Counter(text[idx: idx + 2] for idx in range(0, (len(text)), 2))
    return dict(res)


def find_entropy(freq_dict, n):
    entropy = sum(list(map(lambda x: -x * math.log2(x), freq_dict.values())))
    entropy *= 1/n
    return entropy


clean_text('exmpl_unformatted.txt')
text_with_spaces = open_file('exmpl_spaces.txt')
text_nospaces = open_file('exmpl_nospaces.txt')

# test and debug


#print(count_mono(text_with_spaces))
mono = count_mono(text_with_spaces)
print(mono)
#print(find_entropy(mono, 1))

#print(count_bi_intersect(text_with_spaces))
#print(count_bi_nointersect(text_with_spaces))

#print(count_bi_intersect(text_nospaces))
#print(count_bi_nointersect(text_nospaces))

#print(tabulate(mono, headers='keys', tablefmt='fancy_grid'))
