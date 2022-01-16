import operator
from collections import Counter
from math import log, log2

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
        'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']


def get_ngram_freq(string, n, step=1):
    grams = Counter([string[i:i + n] for i in range(0, len(string) - n + 1, step)])
    size = sum(grams.values())
    grams = dict(((gram, grams[gram] / size) for gram in grams))
    return dict(sorted(grams.items(), key=operator.itemgetter(1), reverse=True))


def get_entropy(grams):
    n = len(list(grams.keys())[0])
    entropy = 0
    for freq in grams.values():
        entropy += - freq * log(freq, 2)
    entropy *= 1 / n
    return entropy


def get_redundancy(entropy, n):
    return 1 - entropy / log2(n)


def get_text():
    with \
            open('text.txt', 'r', encoding='utf-8') as f, \
            open('text_clean1.txt', 'w', encoding='utf-8') as text_clean1, \
            open('text_clean2.txt', 'w', encoding='utf-8') as text_clean2:
        lowercase = f.read().lower().replace('ё', 'е').replace('ъ', 'ь')
        last_char = ' '
        for ch in lowercase:
            if ch in alph:
                text_clean1.write(ch)
                text_clean2.write(ch)
            elif ch == ' ' and last_char != ' ':
                text_clean2.write(ch)
            last_char = ch
    with \
            open('text_clean1.txt', 'r', encoding='utf-8') as text_clean1, \
            open('text_clean2.txt', 'r', encoding='utf-8') as text_clean2:
        return text_clean1.read(), text_clean2.read()


if __name__ == '__main__':
    no_spaces, spaces = get_text()

    no_spaces_n1 = get_ngram_freq(no_spaces, 1)
    spaces_n1 = get_ngram_freq(spaces, 1)

    no_spaces_n2_intersection = get_ngram_freq(no_spaces, 2)
    spaces_n2_intersection = get_ngram_freq(spaces, 2)

    no_spaces_n2 = get_ngram_freq(no_spaces, 2, 2)
    spaces_n2 = get_ngram_freq(spaces, 2, 2)

    no_spaces_n1_ent = get_entropy(no_spaces_n1)
    spaces_n1_ent = get_entropy(spaces_n1)
    no_spaces_n2_ent_intersection = get_entropy(no_spaces_n2_intersection)
    spaces_n2_ent_intersection = get_entropy(spaces_n2_intersection)
    no_spaces_n2_ent = get_entropy(no_spaces_n2)
    spaces_n2_ent = get_entropy(spaces_n2)

    no_spaces_n1_red = get_redundancy(no_spaces_n1_ent, 31)
    spaces_n1_red = get_redundancy(spaces_n1_ent, 32)
    no_spaces_n2_red_intersection = get_redundancy(no_spaces_n2_ent_intersection, 31)
    spaces_n2_red_intersection = get_redundancy(spaces_n2_ent_intersection, 32)
    no_spaces_n2_red = get_redundancy(no_spaces_n2_ent, 31)
    spaces_n2_red = get_redundancy(spaces_n2_ent, 32)

    print("Monograms no spaces: ", no_spaces_n1)
    print("Monograms with spaces: ", spaces_n1)
    print("Bigrams with intersection no spaces: ", no_spaces_n2)
    print("Bigrams with intersection with spaces: ", spaces_n2)
    print("Bigrams without intersection no spaces: ", no_spaces_n2)
    print("Bigrams without intersection with spaces: ", spaces_n2)

    print("H1 no spaces: ", no_spaces_n1_ent)
    print("H1 with spaces: ", spaces_n1_ent)
    print("H2 with intersection no spaces: ", no_spaces_n2_ent_intersection)
    print("H2 with intersection with spaces: ", spaces_n2_ent_intersection)
    print("H2 without intersection no spaces: ", no_spaces_n2_ent)
    print("H2 without intersection with spaces: ", spaces_n2_ent)

    print("H1 redundancy no spaces: ", no_spaces_n1_red)
    print("H1 redundancy with spaces: ", spaces_n1_red)
    print("H2 with intersection redundancy no spaces: ", no_spaces_n2_red_intersection)
    print("H2 with intersection redundancy with spaces: ", spaces_n2_red_intersection)
    print("H2 without intersection redundancy no spaces: ", no_spaces_n2_red_intersection)
    print("H2 without intersection redundancy with spaces: ", spaces_n2_red_intersection)


