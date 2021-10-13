from collections import Counter
from math import log, log2

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
        'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']


def get_ngram_freq(string, n):
    grams = Counter([string[i:i + n] for i in range(len(string) - n + 1)])
    size = sum(grams.values())
    grams = dict(((gram, grams[gram] / size) for gram in grams))
    return grams


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
        lowercase = f.read().lower()
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

    no_spaces_n2 = get_ngram_freq(no_spaces, 2)
    spaces_n2 = get_ngram_freq(spaces, 2)

    no_spaces_n1_ent = get_entropy(no_spaces_n1)
    spaces_n1_ent = get_entropy(spaces_n1)
    no_spaces_n2_ent = get_entropy(no_spaces_n2)
    spaces_n2_ent = get_entropy(spaces_n2)

    no_spaces_n1_red = get_redundancy(no_spaces_n1_ent, 33)
    spaces_n1_red = get_redundancy(spaces_n1_ent, 34)
    no_spaces_n2_red = get_redundancy(no_spaces_n2_ent, 33)
    spaces_n2_red = get_redundancy(spaces_n2_ent, 34)

    print("Monograms no spaces: ", no_spaces_n1)
    print("Monograms with spaces: ", spaces_n1)
    print("Bigrams no spaces: ", no_spaces_n2)
    print("Bigrams with spaces: ", spaces_n2)

    print("H1 no spaces: ", no_spaces_n1_ent)
    print("H1 with spaces: ", spaces_n1_ent)
    print("H2 no spaces: ", no_spaces_n2_ent)
    print("H2 with spaces: ", spaces_n2_ent)

    print("H1 redundancy no spaces: ", no_spaces_n1_red)
    print("H1 redundancy with spaces: ", spaces_n1_red)
    print("H2 redundancy no spaces: ", no_spaces_n2_red)
    print("H2 redundancy with spaces: ", spaces_n2_red)


