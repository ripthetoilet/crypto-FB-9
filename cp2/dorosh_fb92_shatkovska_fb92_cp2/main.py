# # This is the 2nd lab on Cryptology done by Dorosh and Shatkovska FB-92
from collections import Counter
import random
from itertools import chain
import pandas as pd

keys_list = ['мэ', 'фуж', 'хшлъ', 'етгуз', 'илиъглкяоф', 'йпфъчнвэови', 'щзрхдъыэрглф', 'нблзчсхкмшпня', 'сучвнюоъптяамю', 'ъеьяюжхээфъэыью', 'гакыыхрвбчлючицы', 'рнътдцаоицкшлжьни', 'ьищэксьтчбещйархря', 'увэояихшцхерхкпхнфы', 'яоьдэузэцяеьобмэхруы']


# getting the alphabet
def get_dict():
    a = ord('а')
    alphabet = [chr(i) for i in range(a,a+32)]
    return alphabet


# used for generating keys
def gen_keys():
    keys = []
    for i in chain(range(2,6), range(10, 21)):
        keys.append(''.join(random.choices(alphabet, k=i)))
    return keys


def open_file(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    return text


# Cleaning example text to match the criteria before doing the task
def clean_text(txt):
    chars = '.71()-«5d?[“!93286”…—4;»0:],na'

    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    for ch in chars:
        text = text.replace(ch, '')

    text = ''.join([word.strip('\n') for word in text.split()])

    with open('example_prepared.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def encode(text, key):
    encrypted = []
    key_indexes = [alphabet.index(k) for k in key]

    for idx, ch in enumerate(text):
        p_idx = alphabet.index(ch)
        k_idx = key_indexes[idx % len(key)]
        c_idx = (p_idx + k_idx) % len(alphabet)

        encrypted.append(alphabet[c_idx])
    return encrypted


def decode(text, key):
    decrypted = []
    key_idx = [alphabet.index(k) for k in key]

    for idx, ch in enumerate(text):
        c_idx = alphabet.index(ch)
        k_idx = key_idx[idx % len(key)]
        p_idx = (c_idx - k_idx + len(alphabet)) % len(alphabet)

        decrypted.append(alphabet[p_idx])
    return ''.join(decrypted)


# func from lab1
# used in text_coincidence_idx()
def freq_data(text):
    res = Counter(text[idx] for idx in range(len(text)))
    return dict(res)


def text_coincidence_idx(text):
    res = 0
    n = len(text)

    for freq in freq_data(text).values():
        res += freq * (freq - 1)

    res *= 1/(n * (n - 1))

    return res


def create_blocks(text, size):
    blocks = []

    for start in range(0, size):
        blocks.append(text[start::size])

    return blocks


def find_key_len(text):
    indexes = {}
    for len_key in range(1, 31):
        coincidence_idx = 0

        blocks = create_blocks(text, len_key)

        for block in blocks:
            coincidence_idx += text_coincidence_idx(block)
        coincidence_idx /= len_key
        indexes[len_key] = coincidence_idx

    return indexes


def find_key(text, key_len):
    results = {}
    blocks = create_blocks(text, key_len)

    # results from lab1
    top_letters = "оаетни"

    for letter in top_letters:
        res = ""
        for block in blocks:
            block_freq = freq_data(block)
            most_f = max(block_freq, key=block_freq.get)
            res += alphabet[(alphabet.index(most_f) - alphabet.index(letter)) % len(alphabet)]

        results[letter] = res

    return results


alphabet = get_dict()

# prepare text
clean_text("example.txt")
text_sample = open_file("example_prepared.txt")


print("Plain text")
print("Індекс відповідності: ", text_coincidence_idx(text_sample))

data_t1 = {}
data_t2 = {}

for key in keys_list:
    c_text = encode(text_sample, key)
    # task 1
    data_t1[len(key)] = [key, ''.join(c_text)]
    # task 2
    data_t2[len(key)] = [key, text_coincidence_idx(c_text)]

df_t1 = pd.DataFrame.from_dict(data_t1, orient='index', columns=['Key', 'Encoded'])
df_t2 = pd.DataFrame.from_dict(data_t2, orient='index', columns=['Key', 'Coincidence Index'])

df_t1.to_csv('task1.csv')
df_t2.to_csv('task2.csv')


# task 3
text_t3 = open_file('task3.txt')
key_len_data = find_key_len(text_t3)
df_t3 = pd.DataFrame.from_dict(key_len_data, orient='index', columns=['Coincidence Index'])
df_t3.to_csv('task3.csv')

key_len = max(key_len_data, key=key_len_data.get)

print(find_key(text_t3, key_len))

key_final = "вшекспирбуря"
print(decode(text_t3, key_final))
