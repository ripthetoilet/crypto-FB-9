# # This is the 4th lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92
import random
rand = random.SystemRandom()
import math

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


def decompose(p):
    # decomposes p to s and d values in p-1 = d* 2^s
    d = p - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    return s, d


# http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
# Miller-Rabin primality test
def miller_rabin(p, k):
    # part 0
    s, d = decompose(p)
    counter = 0
    while counter < k:
        # part 1
        x = rand.randint(1, p)
        if gcd(x, p)[0] > 1:
            return False
        elif gcd(x, p)[0] == 1:
            # part 2
            if abs(pow(x, d, p)) == 1:
                continue
            else:
                xr = pow(x, 2*d, p)         # if r == 1
                for r in range(2, s - 1):
                    xr = pow(xr, d * (2 ** r), p)
                    if xr == -1:
                        continue
                    elif xr == -1:
                        return False
        counter += 1
    return True


print(miller_rabin(97, 10))             # prime
print(miller_rabin(21881, 10))          # prime

