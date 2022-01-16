from text_processing import process_text
from math import log2
import pandas as pd

ru_alphabet = [chr(code) for code in range(ord("а"), ord("а") + 32)]
ru_alphabet.remove("ъ")
char_freq_dict_whitespaces = {}
bigram_dict_whitespaces = {}
char_freq_dict = {}
bigram_dict = {}


def bigram_dict_prettifier(some_dict: dict) -> dict:
    new_dict = {char: {char_2: 0 for char_2 in ru_alphabet} for char in ru_alphabet}
    for key, value in some_dict.items():
        new_key = key[0]
        new_subkey = key[1]
        new_dict[new_key][new_subkey] = value
    return new_dict


def char_frequency(some_text: str, freq_dict: dict, whitespaces=True) -> dict:
    for char in ru_alphabet:
        char_count = some_text.count(char)
        freq_dict[char] = char_count / (len(some_text) if whitespaces else
                                        len("".join(some_text.split())))
    return dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))


def bigram_frequency(some_text: str, freq_dict: dict, whitespaces=True) -> dict:
    for index, value in enumerate(some_text):
        try:
            if some_text[index] != " " and some_text[index + 1] != " ":
                bigram = some_text[index] + some_text[index + 1]
                if bigram not in freq_dict.keys():
                    bigram_count = some_text.count(bigram)
                    freq_dict[bigram] = bigram_count / (len(some_text) if whitespaces else
                                                        len("".join(some_text.split())))
                if some_text[index + 2] != " ":
                    shifted_bigram = some_text[index] + some_text[index + 2]
                    if shifted_bigram not in freq_dict.keys():
                        bigram_count = some_text.count(shifted_bigram)
                        freq_dict[shifted_bigram] = bigram_count / (len(some_text) if whitespaces else
                                                                    len("".join(some_text.split())))
        except IndexError:
            pass
    return dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))


def entropy(freq: dict, n: int) -> float:
    entropy_sum = 0
    for key, value in freq.items():
        if value != 0:
            entropy_sum += value * log2(value)
    return 1 / n * -entropy_sum


text = process_text(ru_alphabet)

ru_alphabet.append(" ")
char_freq_dict_whitespaces = char_frequency(text, char_freq_dict_whitespaces)
bigram_dict_whitespaces = bigram_frequency(text, bigram_dict_whitespaces)
# print(char_freq_dict_whitespaces)
# print(bigram_dict_whitespaces)
with open("results.txt", "w") as file:
    file.write(f"H1 with whitespaces: {entropy(char_freq_dict_whitespaces, 1)}\n"
               f"H2 with whitespaces: {entropy(bigram_dict_whitespaces, 2)}\n\n")
df = pd.DataFrame(char_freq_dict_whitespaces.values(), index=char_freq_dict_whitespaces.keys())
bigram_dict_whitespaces = bigram_dict_prettifier(bigram_dict_whitespaces)
df2 = pd.DataFrame(bigram_dict_whitespaces.values(), index=bigram_dict_whitespaces.keys())
df.columns = ['Frequency']
df.to_excel("character_frequency_with_whitespaces.xlsx")
df2.to_excel("bigram_frequency_with_whitespaces.xlsx")

ru_alphabet.remove(" ")
char_freq_dict = char_frequency(text, char_freq_dict, whitespaces=False)
bigram_dict = bigram_frequency(text, bigram_dict, whitespaces=False)
with open("results.txt", "a") as file:
    file.write(f"H1 without whitespaces: {entropy(char_freq_dict, 1)}\n"
               f"H2 without whitespaces: {entropy(bigram_dict, 2)}")
# print(char_freq_dict)
# print(bigram_dict)
df = pd.DataFrame(char_freq_dict.values(), index=char_freq_dict.keys())
bigram_dict = bigram_dict_prettifier(bigram_dict)
df2 = pd.DataFrame(bigram_dict.values(), index=bigram_dict.keys())
df.columns = ['Frequency']
df.to_excel("character_frequency.xlsx")
df2.to_excel("bigram_frequency.xlsx")
