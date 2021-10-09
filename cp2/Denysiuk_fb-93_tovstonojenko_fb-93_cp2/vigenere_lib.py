import random

# LETTERS = sorted(list('абвгдежзийклмнопрстуфхцчшщыьэюя'))
LETTERS = sorted('qwertyuiopasdfghjklzxcvbnm')
DICT_OF_INDEXES = {LETTERS[b]: b for b in range(len(LETTERS))}


def generate_key(length: int) -> str:
    rand_string = ''.join(random.choice(LETTERS) for i in range(length))
    return rand_string


def encrypt(text: str, key: str) -> str:
    cyphered_text = ''
    for char in enumerate(text):
        cyphered_text += LETTERS[(DICT_OF_INDEXES[char[1]] + DICT_OF_INDEXES[key[char[0] % len(key)]]) % len(LETTERS)]
    return cyphered_text


def decrypt(cyphered_text: str, key: str) -> str:
    original_text=''
    for char in enumerate(cyphered_text):
        original_text += LETTERS[(len(LETTERS)+DICT_OF_INDEXES[char[1]]
                                  - DICT_OF_INDEXES[key[char[0] % len(key)]]) % len(LETTERS)]
    return original_text

