import re
from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
keys = ['ну', 'так', 'даже', 'очень', 'прикольнаялаба']
file = open('plaintext.txt', encoding='utf-8')
text = re.sub(r'[^а-яА-Я]', '', file.read()).lower()


def encrypt(plaintext, key):
    ciphertext = ''
    for num, letter in enumerate(plaintext):
        ciphertext += alphabet[(alphabet.index(letter) + alphabet.index(key[num % len(key)])) % len(alphabet)]
    return ciphertext


def compliance_index(text_block):
    quantity = Counter(text_block)
    compliance = 0
    for el in quantity:
        compliance += quantity[el] * (quantity[el] - 1)
    compliance /= len(text_block) * (len(text_block) - 1)
    return compliance


def output(_text):
    for num, key in enumerate(keys):
        encrypted_text = encrypt(text, key)
        open(f'key{num}.txt', 'w').write(f'Compliance index: {compliance_index(encrypted_text)}\n\n{encrypted_text}')


output(text)
