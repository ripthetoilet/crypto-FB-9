# # This is the 4th lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92
import random


# from lab3
def gcd(a, b):
    p = [0, 1]
    gcd_val = b
    a, b = max(a, b), min(a, b)
    while b != 0:
        q = a // b
        gcd_val = b
        a, b = b, a % b
        p.append(p[-1]*(-q)+p[-2])
    return gcd_val, p[-2]

# http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
# Miller-Rabin primality test
def miller(p: int):
    counter = 0
    while counter < p:
        pass
    x = random.randint(1, p)
    if gcd(x, p) == 1:

    pass
