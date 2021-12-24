import math
import pandas as pd

rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
                'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']

rus_most_freq_bigramms = ['ст', 'но', 'то', 'ен', 'на']


def gcd_ext(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_ext(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def calc_reverse_by_mod(a, mod):
    gcd, x, y = gcd_ext(a, mod)
    if gcd == 1:
        return (x % mod + mod) % mod
    else:
        return -1


def calc_linear_comparison(a, b, mod):
    gcd = math.gcd(a, mod)
    if gcd == 1:
        x = (calc_reverse_by_mod(a, mod) * b) % mod
        return x
    elif gcd > 1:
        a1 = a / gcd
        b1 = b / gcd
        n1 = mod / gcd
        x = calc_linear_comparison(a1, b1, n1)
        return x
    else:
        return None


def calc_all_bigramm_freq(alphabet, text, is_space_allowed=False, is_intersec_allowed=False, log_file_name=None):
    bigramm_freq_dict = {}
    bigramm_num_dict = {}

    # Reduce text size if its length is odd
    if is_space_allowed:
        alphabet.append(' ')
    text_len = 0
    if len(text) % 2 == 0:
        text_len = len(text)
    else:
        text_len = len(text) - 1

    # Combine all letters for creating bigramms
    for sym1 in alphabet:
        for sym2 in alphabet:
            new_bigramm = sym1 + sym2
            bigramm_freq_dict.update({new_bigramm: 0})
            bigramm_num_dict.update({new_bigramm: 0})

    # Counting bigramm frequency
    index = 0
    while index < text_len - 1:
        sym1 = text[index]
        sym2 = text[index + 1]
        cur_bigramm = sym1 + sym2
        bigramm_num_dict[cur_bigramm] = bigramm_num_dict[cur_bigramm] + 1
        if is_intersec_allowed:
            index = index + 1
        else:
            index = index + 2
    for bigramm in bigramm_num_dict:
        divider = 0
        if is_intersec_allowed:
            divider = text_len - 1
        else:
            divider = text_len / 2
        bigramm_freq_dict.update({bigramm: bigramm_num_dict[bigramm]/divider})

    sorted_bigramm_freq_dict = dict(sorted(bigramm_freq_dict.items(), key=lambda item: item[1], reverse=True))
    if log_file_name is not None:
        out_df = pd.DataFrame.from_dict(sorted_bigramm_freq_dict, orient='index', columns=['Frequency'])
        out_df.to_excel(log_file_name + '.xlsx')
    return sorted_bigramm_freq_dict


def get_most_freq_bigramms(bigramm_freq_dict, size):
    most_freq_dict = dict(list(bigramm_freq_dict.items())[:size])
    return most_freq_dict


def get_bigramm_num(bigramm, alphabet):
    bigramm_num = alphabet.index(bigramm[0]) * len(alphabet) + alphabet.index(bigramm[1])
    return bigramm_num


def bigramm_by_num(bigramm_num, alphabet):
    return alphabet[bigramm_num//len(alphabet)] + alphabet[bigramm_num % len(alphabet)]

