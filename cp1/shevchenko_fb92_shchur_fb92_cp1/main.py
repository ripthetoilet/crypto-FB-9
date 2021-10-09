import math
from nltk import everygrams
from collections import Counter
import re


def read_file(filename):
    with open(filename, 'r') as fin:
        return fin.read()


def write_file(filename, text):
    with open(filename, 'w') as fout:
        for key, val in text.items():
            fout.write('{}:{}\n'.format(key, val))



def clear_text(text, space):
    cleared_text = text.replace("\n", " ").replace("\r", "").replace("ё", "е").replace("ъ", "ь").lower()
    if space:
        cleared_text = re.sub('[^а-я ]', '', cleared_text)
        cleared_text = re.sub(r'\s+', ' ', cleared_text)
        print("Текст з пробілами:")
    else:
        cleared_text = re.sub('[^а-я]', '', cleared_text)
        print("Текст без пробілів:")
    print(cleared_text + "\n")
    return cleared_text


def get_absfreq(text):
    return dict(Counter(text).most_common())


def get_relfreq(text, filename):
    abs_freq = get_absfreq(text)
    rel_freq = {k: v / len(text) for k, v in abs_freq.items()}
    write_file(filename, rel_freq)
    return rel_freq


def get_bigrams(text, intersection):
    if intersection:
        return list(everygrams(text, 2, 2))
    else:
        return [tuple(i) for i in re.findall('..', text)]


def get_h1(relfreq, space):
    entropy = 0
    for i in relfreq.values():
        entropy += - i * math.log2(i)
    entropy = entropy
    list = []
    list.append(entropy)
    if space:
        list.append(1 - entropy / math.log2(32))
    else:
        list.append(1 - entropy / math.log2(31))
    return list


def get_h2(relfreq, space):
    entropy = 0
    for i in relfreq.values():
        entropy += - i * math.log2(i)
    entropy = entropy / 2
    list = []
    list.append(entropy)
    if space:
        list.append(1 - entropy / math.log2(32))
    else:
        list.append(1 - entropy / math.log2(31))
    return list


# ШЛЯХИ
FILE_DEF = "texts\\file_def.txt"

FILE_RELFREQ_MONO___SPACES = "tables\\FILE_RELFREQ_MONO___SPACES.txt"
FILE_RELFREQ_MONO___NOSPACES = "tables\FILE_RELFREQ_MONO___NOSPACES.txt"

FILE_RELFREQ_INTERSECT___SPACES = "tables\\FILE_RELFREQ_INTERSECT___SPACES.txt"
FILE_RELFREQ_INTERSECT___NOSPACES = "tables\\FILE_RELFREQ_INTERSECT___NOSPACES.txt"

FILE_RELFREQ_NOINTERSECT___SPACES = "tables\\FILE_RELFREQ_NOINTERSECT___SPACES.txt"
FILE_RELFREQ_NOINTERSECT___NOSPACES = "tables\\FILE_RELFREQ_NOINTERSECT___NOSPACES.txt"
# ШЛЯХИ


# ОЧИСТКА ТЕКСТА
default = read_file(FILE_DEF)

spaces = clear_text(default, True)

nospaces = clear_text(default, False)
# ОЧИСТКА ТЕКСТА


# АБСОЛЮТНІ ЧАСТОТИ МОНОГРАМ
absfreq_mono___spaces = get_absfreq(spaces)
print("Абсолютна частота монограм для тексту з пробілами:\n" + str(absfreq_mono___spaces) + "\n")

absfreq_mono___nospaces = get_absfreq(nospaces)
print("Абсолютна частота монограм для тексту без пробілів:\n" + str(absfreq_mono___nospaces) + "\n")
# АБСОЛЮТНІ ЧАСТОТИ МОНОГРАМ


# ВІДНОСНІ ЧАСТОТИ МОНОГРАМ
relfreq_mono___spaces = get_relfreq(spaces, FILE_RELFREQ_MONO___SPACES)
print("Відносна частота монограм для тексту з пробілами:\n" + str(relfreq_mono___spaces) + "\n")

relfreq_mono___nospaces = get_relfreq(nospaces, FILE_RELFREQ_MONO___NOSPACES)
print("Відносна частота монограм для тексту без пробілів:\n" + str(relfreq_mono___nospaces) + "\n")
# ВІДНОСНІ ЧАСТОТИ МОНОГРАМ

print("------------------------------------------------------------\n")

# БІГРАМИ З ПЕРЕТИНОМ
intersect___spaces = get_bigrams(spaces, True)
print("Біграми, які перетинаються для тексту з пробілами:\n" + str(intersect___spaces) + "\n")

intersect___nospaces = get_bigrams(nospaces, True)
print("Біграми, які перетинаються для тексту без пробілів:\n" + str(intersect___nospaces) + "\n")
# БІГРАМИ З ПЕРЕТИНОМ


# АБСОЛЮТНІ ЧАСТОТИ БІГРАМ З ПЕРЕТИНОМ
absfreq_intersect___spaces = get_absfreq(intersect___spaces)
print("Абсолютна частота біграм, що перетинаються, для тексту з пробілами:\n" + str(absfreq_intersect___spaces) + "\n")

absfreq_intersect___nospaces = get_absfreq(intersect___nospaces)
print("Абсолютна частота біграм, що перетинаються, для тексту без пробілів:\n" + str(absfreq_intersect___nospaces) + "\n")
# АБСОЛЮТНІ ЧАСТОТИ БІГРАМ З ПЕРЕТИНОМ


# ВІДНОСНІ ЧАСТОТИ БІГРАМ З ПЕРЕТИНОМ
relfreq_intersect___spaces = get_relfreq(intersect___spaces, FILE_RELFREQ_INTERSECT___SPACES)
print("Відносна частота біграм, що перетинаються, для тексту з пробілами:\n" + str(relfreq_intersect___spaces) + "\n")

relfreq_intersect___nospaces = get_relfreq(intersect___nospaces, FILE_RELFREQ_INTERSECT___NOSPACES)
print("Відносна частота біграм, що перетинаються, для тексту без пробілів:\n" + str(relfreq_intersect___nospaces) + "\n")
# ВІДНОСНІ ЧАСТОТИ БІГРАМ З ПЕРЕТИНОМ

print("------------------------------------------------------------\n")

# БІГРАМИ БЕЗ ПЕРЕТИНУ
nointersect___spaces = get_bigrams(spaces, False)
print("Біграми, які не перетинаються для тексту з пробілами:\n" + str(nointersect___spaces) + "\n")

nointersect___nospaces = get_bigrams(nospaces, False)
print("Біграми, які не перетинаються для тексту без пробілів:\n" + str(nointersect___nospaces) + "\n")
# БІГРАМИ БЕЗ ПЕРЕТИНУ


# АБСОЛЮТНІ ЧАСТОТИ БІГРАМ БЕЗ ПЕРЕТИНУ
absfreq_nointersect___spaces = get_absfreq(nointersect___spaces)
print("Абсолютна частота біграм, що перетинаються, для тексту з пробілами:\n" + str(absfreq_nointersect___spaces) + "\n")

absfreq_nointersect___nospaces = get_absfreq(nointersect___nospaces)
print("Frequencies of all nonintersecting bigrams for text without spaces:\n" + str(absfreq_nointersect___nospaces) + "\n")
# АБСОЛЮТНІ ЧАСТОТИ БІГРАМ БЕЗ ПЕРЕТИНУ


# ВІДНОСНІ ЧАСТОТИ БІГРАМ БЕЗ ПЕРЕТИНУ
relfreq_nointersect___spaces = get_relfreq(nointersect___spaces, FILE_RELFREQ_NOINTERSECT___SPACES)
print("Відносна частота біграм, що не перетинаються, для тексту з пробілами:\n" + str(relfreq_nointersect___spaces) + "\n")

relfreq_nointersect___nospaces = get_relfreq(nointersect___nospaces, FILE_RELFREQ_NOINTERSECT___NOSPACES)
print("Відносна частота біграм, що не перетинаються, для тексту без пробілів:\n" + str(relfreq_nointersect___nospaces) + "\n")
# ВІДНОСНІ ЧАСТОТИ БІГРАМ БЕЗ ПЕРЕТИНУ


print("------------------------------------------------------------\n")

# ЕНТРОПІЯ І НАДЛИШКОВІСТЬ ДЛЯ МОНОГРАМ
H1_mono___spaces = get_h1(relfreq_mono___spaces, True)
print("Ентропія Н1 для тексту з пробілами: " + str(H1_mono___spaces[0]))
print("Надлишковість Н1 для тексту з пробілами: " + str(H1_mono___spaces[1]) + "\n")

H1_mono___nospaces = get_h1(relfreq_mono___nospaces, False)
print("Ентропія Н1 для тексту без пробілів: " + str(H1_mono___nospaces[0]))
print("Надлишковість Н1 для тексту без пробілів: " + str(H1_mono___nospaces[1]) + "\n")
# ЕНТРОПІЯ І НАДЛИШКОВІСТЬ ДЛЯ МОНОГРАМ


# ЕНТРОПІЯ І НАДЛИШКОВІСТЬ ДЛЯ БІГРАМ З ПЕРЕТИНАМИ
H2_intersect___spaces = get_h2(relfreq_intersect___spaces, True)
print("Ентропія Н2 біграм, що перетинаються, для тексту з пробілами: " + str(H2_intersect___spaces[0]))
print("Надлишковість Н2 біграм, що перетинаються, для тексту з пробілами: " + str(H2_intersect___spaces[1]) + "\n")

H2_intersect___nospaces = get_h2(relfreq_intersect___nospaces, False)
print("Ентропія Н2 біграм, що перетинаються, для тексту без пробілів: " + str(H2_intersect___nospaces[0]))
print("Надлишковість Н2 біграм, що перетинаються, для тексту без пробілів: " + str(H2_intersect___nospaces[1]) + "\n")
# ЕНТРОПІЯ І НАДЛИШКОВІСТЬ ДЛЯ БІГРАМ З ПЕРЕТИНАМИ


# ЕНТРОПІЯ І НАДЛИШКОВІСТЬ ДЛЯ БІГРАМ БЕЗ ПЕРЕТИНІВ
H2_nointersect___spaces = get_h2(relfreq_nointersect___spaces, True)
print("Ентропія Н2 біграм, що не перетинаються, для тексту з пробілами: " + str(H2_nointersect___spaces[0]))
print("Надлишковість Н2 біграм, що не перетинаються, для тексту з пробілами: " + str(H2_nointersect___spaces[1]) + "\n")

H2_nointersect___nospaces = get_h2(relfreq_nointersect___nospaces, False)
print("Ентропія Н2 біграм, що не перетинаються, для тексту без пробілів: " + str(H2_nointersect___nospaces[0]))
print("Надлишковість Н2 біграм, що не перетинаються, для тексту без пробілів: " + str(H2_nointersect___nospaces[1]) + "\n")
# ЕНТРОПІЯ І НАДЛИШКОВІСТЬ ДЛЯ БІГРАМ БЕЗ ПЕРЕТИНІВ
