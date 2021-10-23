import sys

sys.path.insert(0, '../../cp1/Denysiuk_fb-93_tovstonojenko_fb-93_cp1')

LETTERS = sorted(list('абвгдежзийклмнопрстуфхцчшщыьэюя'))


def encrypt_bigram(bigram: str, key: tuple) -> int:
    l = len(LETTERS)
    x = LETTERS.index(bigram[0]) * l + LETTERS.index(bigram[1])
    y = (key[0] * x + key[1]) % l ** 2
    
    
#repairing repositiry
