# # This is the 4th lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92
import random
rand = random.SystemRandom()

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
def miller_rabin(p, k):
    # part 0
    d = (p - 1) % 2
    s = (p - 1) // 2
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


print(miller_rabin(97, 10))         # needs to return True

