import random

def find_simple_num(n0, n1):
    x = random.randint(n0, n1)
    if x%2 == 0: m0 = x+1
    else: m0 = x
    for i in range(0, int((n1-m0)/2)+1):
        if(is_simple(m0+2*i)) == 1: return m0+2*i
    return find_simple_num(n0, n1)

def is_simple(p):
    if(p%3 == 0 or p%5 == 0 or p%7 == 0): return 0
    else:
        d = 1
        while (True):
            s = is_step2((p - 1) // d, 0)
            if ((p - 1) % d == 0 and s != -1): break
            d += 2
        return miller_rabin(p,d,s,0)

def miller_rabin(p,d,s,counter):
    simp = 0
    x = random.randint(1,p)
    if gcd(x,p) != 1: return 0
    if x**d%p == 1 or (x**d%p)-p == -1: simp = 1
    else:
        for r in range(1, s):
            xr = (x**(d*2**r))%p
            if xr - p == -1:
                simp = 1
                break
            elif xr == 1: return 0
    if simp == 0: return 0
    counter += 1
    if(counter < 10):
        return miller_rabin(p,d,s,counter)
    return 1

def is_step2(n, s):
    if(n == 1): return s
    if(n == 2): return s+1
    elif(n%2 == 0): return is_step2(n/2, s+1)
    return -1

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b: a = a % b
        else: b = b % a
    return a + b


def generate_pairs():
    interval = [265,1000]
    x = [0]*4
    for i in range(4):
        x[i] = find_simple_num(interval[0],interval[1])
    if (x[0]*x[1] > x[2]*x[3]): return generate_pairs()
    return x

print(generate_pairs())


