import random
from math import gcd
from cp3.tishkov_papucha_fb_93_cp3.lab3 import gcd_ext
from cp3.tishkov_papucha_fb_93_cp3.lab3 import calc_reverse_by_mod
from cp2.Tishkov_Papucha_FB_93_cp2.Lab2 import VigenereCypherModule

rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
                'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']

default_interval_pair = [(2**255)+1, (2**256)-1]


def gen_random_prime_num(min_interval=default_interval_pair[0], max_interval=default_interval_pair[1]):
    while True:
        random_num = random.randint(min_interval, max_interval)
        if is_prime(random_num):
            return random_num


def is_prime(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    else:
        return miller_rabin(num)


def miller_rabin(num):
    d, s = num - 1, 0
    while d % 2 == 0:
        d = d // 2
        s += 1
    a = random.randint(2, num-1)
    x = pow(a, d, num)
    if x == 1 or x == num-1:
        return True
    while s > 1:
        x = pow(x, x, num)
        if x == 1:
            return False
        if x == -1:
            return True
        s -= 1
    return False


class RSA:
    def __init__(self):
        self.vigenere = VigenereCypherModule(rus_alphabet)
        self.private_keys = dict()
        self.public_keys = dict()
        self.encryption_key = None

    def f_n(self):
        p = self.private_keys['p']
        q = self.private_keys['q']
        res = (p - 1) * (q - 1)
        return res

    def generate_keys(self):
        p = gen_random_prime_num()
        q = gen_random_prime_num()
        self.private_keys.update({'p': p, 'q': q})
        n = p * q
        self.public_keys.update({'n': n})
        phi = self.f_n()
        e = gen_random_prime_num(2, phi - 1)
        d = calc_reverse_by_mod(e, phi)
        self.public_keys.update({'e': e})
        self.private_keys.update({'d', d})
        return self.public_keys

    def set_encryption_key(self, new_key):
        self.encryption_key = new_key

    def get_encryption_key(self):
        return self.encryption_key

    def generate_auth_msg(self, e1, n1):
        key = self.get_encryption_key()
        d = self.private_keys['d']
        n = self.public_keys['n']
        k1 = (key**e1) % n1
        s = (key**d) % n
        s1 = (s**e1) % n1
        return s1, k1

    def generate_auth_response(self, s1, k1):
        d = self.private_keys['d']
        n = self.public_keys['n']
        check_s = (s1**d) % n
        check_key = (k1**d) % n
        return check_s, check_key

    def check_auth_response(self, check_s, check_k):
        key = self.get_encryption_key()
        d = self.private_keys['d']
        n = self.public_keys['n']
        s = (key ** d) % n
        if s != check_s:
            print("Authentication failed!")
            return False
        return s

    def generate_key_by_response(self, s, e, n):
        key = (s**e) % n
        self.set_encryption_key(key)


def main():
    print(gen_random_prime_num())


if __name__ == '__main__':
    main()