import itertools
from typing import Union
from text_processing import process_text

ru_alphabet = [chr(x) for x in range(ord('а'), ord('а') + 32)]
ru_alphabet.remove('ъ')

bigram_frequency_cipher = {}
most_frequent_bigrams = ['ст', 'но', 'то', 'на', 'ен']


def bigram_to_number(bigram: str) -> int:
    return ru_alphabet.index(bigram[0]) * len(ru_alphabet) + ru_alphabet.index(bigram[1])


def bigram_frequency(some_text: str, freq_dict: dict) -> dict:  # from cp1
    for index, value in enumerate(some_text):
        try:
            if some_text[index] != " " and some_text[index + 1] != " ":
                bigram = some_text[index] + some_text[index + 1]
                if bigram not in freq_dict.keys():
                    bigram_count = some_text.count(bigram)
                    freq_dict[bigram] = bigram_count / len(some_text)
                if some_text[index + 2] != " ":
                    shifted_bigram = some_text[index] + some_text[index + 2]
                    if shifted_bigram not in freq_dict.keys():
                        bigram_count = some_text.count(shifted_bigram)
                        freq_dict[shifted_bigram] = bigram_count / len(some_text)
        except IndexError:
            pass
    return dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))


def extended_euclidean_algorithm(a: int, b: int) -> list:
    original_b = b
    u, uu, v, vv = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        u, uu = uu, u - q * uu
        v, vv = vv, v - q * vv
    return [a, u % original_b]  # a - gcd, u - a^-1


def solve_linear_comparison(a: int, b: int, n: int) -> Union[int, None, list]:
    gcd = extended_euclidean_algorithm(a, n)
    if gcd[0] == 1:
        return (gcd[1] * b) % n
    else:
        if b % gcd[0] != 0:
            return None
        else:
            a1, b1, n1 = a / gcd[0], b / gcd[0], n / gcd[0]
            x0_gcd = extended_euclidean_algorithm(a1, n1)
            x0 = (b1 * x0_gcd[1]) % n1
            all_results = [x0 + d * n1 for d in range(0, gcd[0])]
            return all_results  # all possible a`s


def find_possible_keys(most_frequent_bigrams_cipher: list, most_frequent_bigrams_ru: list) -> list:
    # find all possible combinations (amount of combinations = (n-1)*(n-1)*n*n, n = len(list))
    cartesian_combinations = list(
        itertools.product(most_frequent_bigrams_ru, most_frequent_bigrams_cipher))  # Cartesian product of 2 lists
    cartesian_combinations_split = []
    for i in range(0, len(cartesian_combinations),
                   5):  # split combinations into lists of length 5 (just to make things easier in the future)
        cartesian_combinations_split.append(cartesian_combinations[i:i + 5])
    all_possible_combinations = []
    for i in range(0, len(most_frequent_bigrams_ru)):
        all_variants = [x for x in range(0, len(most_frequent_bigrams_ru))]
        all_variants.remove(i)  # there can`t be combinations like (('ст', 'бц'), ('ст', 'бц'))
        for j in all_variants:
            all_possible_combinations.append(
                list(itertools.product(cartesian_combinations_split[i], cartesian_combinations_split[j])))
    for index, list_ in enumerate(all_possible_combinations):
        for combination in list_:
            if combination[0][1] == combination[1][1]:  # there can`t be combinations like (('ст', 'бц'), ('но', 'бц'))
                all_possible_combinations[index].remove(combination)
    all_possible_keys = []
    for list_ in all_possible_combinations:
        for combination in list_:
            combination_bigram_number = [bigram_to_number(bigram) for tuple_ in combination for bigram in
                                         tuple_]  # [X*, Y*, X**, Y**]
            # a = X* - X**, b = Y* - Y**
            result = solve_linear_comparison(combination_bigram_number[0] - combination_bigram_number[2],
                                             combination_bigram_number[1] - combination_bigram_number[3],
                                             len(ru_alphabet) ** 2)
            if result:
                if type(result) == list:
                    for possible_a in result:
                        if extended_euclidean_algorithm(possible_a, len(ru_alphabet))[0] == 1:
                            a = possible_a
                            b = (combination_bigram_number[1] - combination_bigram_number[0] * possible_a) % (
                                    len(ru_alphabet) ** 2)
                            all_possible_keys.append((a, b))
                        else:
                            pass
                else:
                    a = result
                    if extended_euclidean_algorithm(a, len(ru_alphabet))[0] == 1:
                        b = (combination_bigram_number[1] - combination_bigram_number[0] * a) % (len(ru_alphabet) ** 2)
                        all_possible_keys.append((a, b))
                    else:
                        pass
    return all_possible_keys  # (a, b)


text = process_text(ru_alphabet, 'text.txt')
bigram_frequency_cipher = bigram_frequency(text, bigram_frequency_cipher)
most_frequent_bigrams_cipher = list(bigram_frequency_cipher.keys())[:5]
print(f"The most frequent bigrams in cipher text: {most_frequent_bigrams_cipher}")
keys = find_possible_keys(most_frequent_bigrams_cipher, most_frequent_bigrams)

deciphered_texts = []
for key in keys:
    deciphered_text = ""
    for i in range(0, len(text), 2):
        a_reversed = extended_euclidean_algorithm(key[0], len(ru_alphabet) ** 2)[1]
        deciphered_bigram_index = a_reversed * (bigram_to_number(text[i] + text[i + 1]) - key[1]) % len(
            ru_alphabet) ** 2
        deciphered_second_letter_index = deciphered_bigram_index % len(ru_alphabet)
        deciphered_first_letter_index = (deciphered_bigram_index - deciphered_second_letter_index) / len(
            ru_alphabet)
        deciphered_bigram = ru_alphabet[int(deciphered_first_letter_index)] + ru_alphabet[
            int(deciphered_second_letter_index)]
        deciphered_text += deciphered_bigram
    deciphered_texts.append((key, deciphered_text))

deciphered_texts = list(set(deciphered_texts))  # remove duplicates
for deciphered_text in deciphered_texts[:]:
    for bigram in most_frequent_bigrams:
        if deciphered_text[1].count(bigram) / len(deciphered_text[1]) < 0.005:
            deciphered_texts.remove(deciphered_text)
            break
print(text)
print(deciphered_texts)
