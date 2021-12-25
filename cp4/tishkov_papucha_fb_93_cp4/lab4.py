import random
from math import gcd

interval = [2**255+1, 2**256-1]

def gcd_ext(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_ext(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def calc_reverse_by_mod(a, mod):
    gcd, x, y = gcd_ext(a, mod)
    if gcd == 1:
        return (x % mod + mod) % mod
    else:
        return -1

def prime_gen():
    while True:
        random_num = random.randint(interval[0], interval[1])
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

