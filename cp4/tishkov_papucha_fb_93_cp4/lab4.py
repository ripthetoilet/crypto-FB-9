import random
from math import gcd
from cp3.tishkov_papucha_fb_93_cp3.lab3 import gcd_ext
from cp3.tishkov_papucha_fb_93_cp3.lab3 import calc_reverse_by_mod

default_interval_pair = [2**255+1, 2**256-1]


def prime_gen(min_interval=default_interval_pair[0], max_interval=default_interval_pair[1]):
    while True:
        random_num = random.randint(min_interval, max_interval)
        print(random_num)


def is_prime(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return 0
    else:
        return millera_rabina(num)


def millera_rabina(num):
    d, s = p - 1, 0
    while (d % 2 == 0):
        d = d // 2
        s += 1
    a = randrange(2, num-1)
    x = pow(a, d, num)
    if x == 1 or x == num-1:
        return True
    while r > 1:
        x = pow(x, x, num)
        if x == 1:
            return False
        if x == -1:
            return True
        r -= 1
    return False

