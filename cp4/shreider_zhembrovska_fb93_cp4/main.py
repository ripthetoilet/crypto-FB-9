import random

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

def gorner(x,e,m):
    e = bin(e)
    y = 1
    for i in e[2:]:
        y = (y**2)%m
        if int(i) == 1:
            y = (y*x)%m
    return y

def find_simple(interval):
    x = random.randint(interval[0], interval[1])
    m0 = x if x%2 != 0 else x+1
    for i in range(0, int((interval[1]-m0)/2)+1, 2):
        if(is_simple(m0+i)) == 1: return m0+i
    return find_simple(interval)

def is_simple(p):
    if(p%3 == 0 or p%5 == 0 or p%7 == 0): return 0
    else: return miller_rabin(p)

def ds(p):
    d = p-1
    s = 0
    while(d%2 == 0):
        d = d//2
        s +=1
    return d,s

def miller_rabin(p):
    d,s = ds(p)
    for i in range(10):
        simp = 0
        x = random.randint(1,p)
        if gcd(x,p) != 1: return 0
        num = gorner(x,d,p)
        if num == 1 or num-p == -1: simp = 1
        else:
            for r in range(1, s):
                num = gorner(num,2,p)
                if num - p == -1:
                    simp = 1
                    break
                elif num == 1: return 0
        if not simp: return 0
    return 1

def generate_pairs():
    interval = [2**255,2**256]
    pq, pq1 = [], []
    for i in range(2):
        pq.append(find_simple(interval))
        pq1.append(find_simple(interval))
    if (pq[0]*pq[1] > pq1[0]*pq1[1]): return generate_pairs()
    return [pq, pq1]

def GenerateKeyPair():
    pq = generate_pairs()
    n,fi,e,d = [],[],[],[]
    for i in range(2):
        n.append(pq[i][0]*pq[i][1])
        fi.append((pq[i][0]-1)*(pq[i][1]-1))
        e.append(random.randint(2, fi[i]-1))
        while (gcd(e[i], fi[i]) != 1):
            e[i] = random.randint(2, fi[i]-1)
        d.append((inverted(e[i],fi[i]))%fi[i])
    open_keys = [(e[0],n[0]),(e[1],n[1])]
    secret_key = d
    return open_keys, secret_key

def Encrypt():
    return 0


print(GenerateKeyPair())

