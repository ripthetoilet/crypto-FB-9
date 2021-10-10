import sys
sys.path.insert(0, '../../cp1/Denysiuk_fb-93_tovstonojenko_fb-93_cp1')
import re
import my_lib
import random

# LETTERS = sorted(list('абвгдежзийклмнопрстуфхцчшщыьэюя'))
LETTERS = sorted('qwertyuiopasdfghjklzxcvbnm')
DICT_OF_INDEXES = {LETTERS[b]: b for b in range(len(LETTERS))}

def filter_text(file_name: str, with_whitespace: bool) -> str:
    with open(file_name, mode='rt', encoding='UTF-8') as f:
        filtered = f.read().lower().replace("ё", "е")
    return re.sub("[^а-я]+", '', filtered) if not with_whitespace else re.sub("[^а-я]+", ' ', filtered)


def generate_key(length: int) -> str:
    rand_string = ''.join(random.choice(LETTERS) for i in range(length))
    return rand_string


def encrypt(text: str, key: str) -> str:
    cyphered_text = ''
    for char in enumerate(text):
        cyphered_text += LETTERS[(DICT_OF_INDEXES[char[1]] + DICT_OF_INDEXES[key[char[0] % len(key)]]) % len(LETTERS)]
    return cyphered_text


def decrypt(cyphered_text: str, key: str) -> str:
    original_text = ''
    for char in enumerate(cyphered_text):
        original_text += LETTERS[(len(LETTERS) + DICT_OF_INDEXES[char[1]]
                                  - DICT_OF_INDEXES[key[char[0] % len(key)]]) % len(LETTERS)]
    return original_text


def count_index_of_coincidence(text):
    index_of_coincidence = 0
    for i in my_lib.make_dict_of_frequency_of_chars().values():
        index_of_coincidence += i * (i - 1)
    n = len(text)
    return index_of_coincidence/(n*(n-1))
