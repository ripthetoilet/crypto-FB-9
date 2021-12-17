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

def inverted(a, n):
    q = [0, 1]
    while a != 0 and n != 0:
        if a > n:
            q.append(a // n); a = a % n
        else:
            q.append(n // a); n = n % a
    for i in range(2, len(q)): q[i] = q[i - 2] - q[i] * q[i - 1]
    return q[-2]

def generate_pairs():
    interval = [265,1000]
    pq, pq1 = [], []
    for i in range(2):
        pq.append(find_simple_num(interval[0],interval[1]))
        pq1.append(find_simple_num(interval[0],interval[1]))
    if (pq[0]*pq[1] > pq1[0]*pq1[1]): return generate_pairs()
    return [pq, pq1]

def generate_keys():
    pq = generate_pairs()
    n,fi,e,d = [],[],[],[]
    for i in range(2):
        n.append(pq[i][0]*pq[i][1])
        fi.append((pq[i][0]-1)*(pq[i][1]-1))
        e.append(random.randint(2, fi[i]-1))
        while (gcd(e[i], fi[i]) != 1):
            e[i] = random.randint(2, fi[i]-1)
        d.append(inverted(e[i],fi[i]))
    return 0


print(generate_keys())


