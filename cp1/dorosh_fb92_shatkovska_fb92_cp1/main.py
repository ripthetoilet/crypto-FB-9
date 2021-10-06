# This is the 1st lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92
import math
from collections import Counter
import operator


def open_file(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    return text


# Cleaning example text to match the criteria before doing the task
def clean_text(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # uniqueChars = ''.join(set(text))

    # -----------------------------------------------------
    chars = '.71()-«5d?[“!93286”…—4;»0:],na'
    # -----------------------------------------------------
    for ch in chars:
        text = text.replace(ch, '')

    text = '_'.join([word.strip('\n') for word in text.split()])
    # print(text[:1000])

    with open('exmpl_spaces.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    text = ''.join([word.strip('\n') for word in text.split('_')])
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
    res = {x: round(res[x]/total_bi, 100) for x in res}
    return dict(res)


# counting bigrams with intersection
def count_bi_nointersect(text):
    res = Counter(text[idx: idx + 2] for idx in range(0, (len(text)), 2))
    total_bi = sum(res.values())
    res = {x: round(res[x]/total_bi, 10) for x in res}
    return dict(res)


def find_entropy(freq, n):
    entropy = 0
    for f in freq.values():
        entropy += - f * math.log(f, 2)
    entropy *= 1 / n
    return entropy


def redundant(h, alphabet):
    return 1 - (h/math.log2(alphabet))


clean_text('exmpl_unformatted.txt')
text_with_spaces = open_file('exmpl_spaces.txt')
text_nospaces = open_file('exmpl_nospaces.txt')

# monograms with spaces
mono_spaces = count_mono(text_with_spaces)
# sort
mono_spaces_sorted = dict(sorted(mono_spaces.items(), key=operator.itemgetter(1),reverse=True))
print("Monograms:")
for key, val in mono_spaces_sorted.items():
    print(key, ' |', val)
print('\n')

# monograms without spaces
mono_nospaces = count_mono(text_nospaces)
# sort
mono_nospaces_sorted = dict(sorted(mono_nospaces.items(), key=operator.itemgetter(1),reverse=True))
print("Monograms without spaces:")
for key, val in mono_nospaces_sorted.items():
    print(key, ' |', val)
print('\n')

# bigrams intersected without spaces
count_bi_intersect_nospaces = count_bi_intersect(text_nospaces)
# sort
count_bi_intersect_nospaces_sorted = dict(sorted(count_bi_intersect_nospaces.items(), key=operator.itemgetter(1),reverse=True))
print("Bigrams(intersected, without spaces):")
for key, val in count_bi_intersect_nospaces_sorted.items():
    print(key, '|', val)
print('\n')

# bigrams not intersected, without spaces
count_bi_nointersect_nospaces = count_bi_nointersect(text_nospaces)
# sort
count_bi_nointersect_nospaces_sorted = dict(sorted(count_bi_nointersect_nospaces.items(), key=operator.itemgetter(1),reverse=True))
print("Bigrams(not intersected, without spaces):")
for key, val in count_bi_nointersect_nospaces_sorted.items():
    print(key, '|', val)
print('\n')

# bigrams not intersected with spaces
count_bi_nointersect_spaces = count_bi_nointersect(text_with_spaces)
# sort
count_bi_nointersect_spaces_sorted = dict(sorted(count_bi_nointersect_spaces.items(), key=operator.itemgetter(1),reverse=True))
print("Bigrams(not intersected, with spaces):")
for key, val in count_bi_nointersect_spaces_sorted.items():
    print(key, '|', val)
print('\n')

# bigrams intersected with spaces
count_bi_intersect_spaces = count_bi_intersect(text_with_spaces)
# sort
count_bi_intersect_spaces_sorted = dict(sorted(count_bi_intersect_spaces.items(), key=operator.itemgetter(1),reverse=True))
print("Bigrams(intersected, with spaces):")
for key, val in count_bi_intersect_spaces_sorted.items():
    print(key, '|', val)
print('\n')

alphabet_nospace = 33
alphabet_space = 34

# entropy and redundancy for H1
h1_spaces_ent = find_entropy(mono_spaces, 1)
print("H1 text with spaces: ", h1_spaces_ent)
print("Redundancy for H1 with spaces: ", redundant(h1_spaces_ent, alphabet_space), '\n')

h1_nospaces_ent = find_entropy(mono_nospaces, 1)
print("H1 text without spaces: ", h1_nospaces_ent)
print("Redundancy for H1 without spaces: ", redundant(h1_nospaces_ent, alphabet_nospace), '\n')

# entropy and redundancy for H2
# without intersection
h2_nointersect_spaces_ent = find_entropy(count_bi_nointersect_spaces, 2)
print("H2 text with spaces without intersection: ", h2_nointersect_spaces_ent)
print("Redundancy for H2 with spaces without intersection: ", redundant(h2_nointersect_spaces_ent, alphabet_space), '\n')

h2_nointersect_nospaces_ent = find_entropy(count_bi_nointersect_nospaces, 2)
print("H2 text without spaces without intersection: ", h2_nointersect_nospaces_ent)
print("Redundancy for H2 without spaces without intersection: ", redundant(h2_nointersect_nospaces_ent, alphabet_nospace), '\n')

# with intersections
h2_intersect_spaces_ent = find_entropy(count_bi_intersect_spaces, 2)
print("H2 text with spaces with intersection: ", h2_intersect_spaces_ent)
print("Redundancy for H1 with spaces: ", redundant(h2_intersect_spaces_ent, alphabet_space), '\n')

h2_intersect_nospaces_ent = find_entropy(count_bi_intersect_nospaces, 2)
print("H2 text without spaces with intersection: ", h2_intersect_nospaces_ent)
print("Redundancy for H2 without spaces with intersection: ", redundant(h2_intersect_nospaces_ent, alphabet_nospace), '\n')