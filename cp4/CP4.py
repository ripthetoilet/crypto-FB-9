from random import randrange
from math import gcd

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def euclid_ext(a, n):
    if n == 0:
        return a, 1, 0
    else:
        gcd1, x, y = euclid_ext(n, a % n)
        return gcd1, y, x - y * (a // n)


def miller_rabin(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    d = num - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s += 1
    x = randrange(2, num)
    if gcd(x, num) > 1:
        return False
    x = pow(x, d, num)
    if x == 1 or x == num-1:
        return True
    for r in range(1, s-1):
        x = pow(x, 2, num)
        if x == num-1:
            return True
        if x == 1:
            return False
    return False


def gen_number(bit):
    num = (randrange(1 << bit - 1, 1 << bit) << 1) + 1
    if miller_rabin(num):
        return num
    else:
        num = gen_number(bit)
        return num


def gen_pairs():
    p, q, p1, q1 = gen_number(256), gen_number(256), gen_number(256), gen_number(256)
    while p*q > p1*q1:
        p, q, p1, q1 = gen_number(256), gen_number(256), gen_number(256), gen_number(256)
    return p, q, p1, q1


def GenerateKeyPairs(p, q):
    n = p * q
    fi = (p - 1) * (q - 1)
    e = randrange(2, fi)
    while gcd(e, fi) != 1:
        e = randrange(2, fi)
    gcd1, x, y = euclid_ext(e, fi)
    d = (x % n + n) % n
    return [n, e], [d, p, q]


def Encrypt(m, e, n):
    return pow(m, e, n)


def Decrypt(c, d, n):
    return pow(c, d, n)


def Sign(m, d, n):
    return pow(m, d, n)


def Verify(s, m, e, n):
    return pow(s, e, n) == m


def SendKey(k, e1, d, n1, n):
    print(f'{k  }')
    k1 = Encrypt(k, e1, n1)
    S = Sign(k, d, n)
    print(f'{S  }')
    S1 = Encrypt(S, e1, n1)
    print(f'{k1  }\n{S1  }')
    print('---------------------------------------------------------------------------')
    return k1, S1


def ReceiveKey(k1, S1, e, d1, n1, n):
    k = Decrypt(k1, d1, n1)
    S = Decrypt(S1, d1, n1)
    print(f'{k  }\n{S  }')
    if Verify(S, k, e, n):
        print('message =', k)
        print('True')
    else:
        print('False')


def answer(arr):
    ans = []
    for i in arr:
        msg = alphabet[i]
        ans.append(msg)
    print(''.join(ans))


def Abonent(p,q,p1,q1):
    # A
    public_key, secret_key = GenerateKeyPairs(p, q)
    # B
    public_key1, secret_key1 = GenerateKeyPairs(p1, q1)
    message = 3
    # k, e1, d, n1, n
    k1, S1 = SendKey(message, public_key1[1], secret_key[0], public_key1[0], public_key[0])
    # k1, S1, e, d1, n1, n
    ReceiveKey(k1, S1, public_key[1], secret_key1[0], public_key1[0], public_key[0])


if __name__ == '__main__':
    # p, q, p1, q1 = gen_pairs()
    p = 118519898386396925580866644265646709411476813074947440768634343361227583399179
    q = 183776059903844037852150709588989510915607449636688686937026563848273040875981
    p1 = 159886764155242934076714005673887187650580266149464530109018018325707074573291
    q1 = 185561463084369408990683643333967730321139973978061567005525763288250979345187
    # print(f'{p = }\n{q = }\n{p1 = }\n{q1 = }')
    Abonent(p,q,p1,q1)
