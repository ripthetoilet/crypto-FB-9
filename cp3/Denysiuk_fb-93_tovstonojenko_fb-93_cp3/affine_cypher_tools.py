import sys

sys.path.insert(0, '../../cp1/Denysiuk_fb-93_tovstonojenko_fb-93_cp1')
import my_lib

LETTERS = sorted(list('абвгдежзийклмнопрстуфхцчшщыьэюя'))


def bigrams_to_values(bigrams: list[str]) -> list[int]:
    values = []
    n_letters = len(LETTERS)
    for i in bigrams:
        values.append(LETTERS.index(i[0]) * n_letters + LETTERS.index(i[1]))
    return values


def values_to_bigrams(values: list[int]) -> list[str]:
    bigrams = []
    n_letters = len(LETTERS)
    for i in values:
        bigrams.append(LETTERS[i // n_letters ** 2] + LETTERS[i % n_letters])
    return bigrams


def encrypt_bigram(bigrams: list[str], key: tuple) -> list:
    n_letters = len(LETTERS)
    encoded_bigrams = []
    values = bigrams_to_values(bigrams)
    for v in values:
        encoded_bigrams.append((key[0] * v + key[1]) % n_letters ** 2)
    return values_to_bigrams(encoded_bigrams)


def decrypt_bigram(encoded_bigrams: list[str], key: tuple) -> str:
    n_letters = len(LETTERS)
    decrypted_bigram = []
    encoded_bigrams = bigrams_to_values(encoded_bigrams)
    for bigram in encoded_bigrams:
        a = ((n_letters ** 2 + bigram - key[1]) * (reverse_element(key[0], n_letters ** 2))) % (
                n_letters ** 2)
        decrypted_bigram.append(LETTERS[a // n_letters] + LETTERS[a % n_letters])
    return decrypted_bigram


def decrypt_text(text: str, key: tuple) -> str:
    list_of_bigrams = my_lib.make_list_of_bigram(text, 2)
    decrypted_list = decrypt_bigram(list_of_bigrams, key)
    return ''.join(decrypted_list)


def encrypt_text(text: str, key: tuple) -> str:
    list_of_bigrams = my_lib.make_list_of_bigram(text, 2)
    encrypted_list = encrypt_bigram(list_of_bigrams, key)
    return ''.join(encrypted_list)


def reverse_element(a:int, b:int) :
    return euclid_ext(a, b)[1]


def euclid_ext(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclid_ext(b, a % b)
        return d, y, x - y * (a // b)
