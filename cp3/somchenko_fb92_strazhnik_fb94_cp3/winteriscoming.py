from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
mod = len(alphabet)
frequent_bigrams = 'ст', 'но', 'то', 'на', 'ен'
ciphertext = (open('ciphertext_v4.txt', 'r')).read()


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def inverted_a(a):
    gcd, x, y = extended_gcd(a, mod)
    if gcd != 1:
        pass
    else:
        return x % mod


def solve_linear_comparisons():
    return 0


def bigrams_frequency(text):
    frequency = Counter(text[bi: bi + 2] for bi in range(len(text) - 1))
    frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    return dict(list(frequency.items())[:5])


def decrypt(_a, _b, text):
    plaintext = open('decrypted.txt', 'w')
    for char in text:
        plaintext.write(alphabet[(inverted_a * (alphabet.index(char) + mod - b)) % mod])
    return 0
