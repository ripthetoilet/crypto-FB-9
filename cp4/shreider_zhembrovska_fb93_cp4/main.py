import random
interval = [2**256, 2**257-2]

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b: a = a % b
        else: b = b % a
    return a + b

def inverse(a, n):
    q = [0, 1]
    while a != 0 and n != 0:
        if a > n:
            q.append(a // n); a = a % n
        else:
            q.append(n // a); n = n % a
    for i in range(2, len(q)): q[i] = q[i - 2] - q[i] * q[i - 1]
    return q[-2]

def gorner(x,e,m):
    e, y  = bin(e), 1
    for i in e[2:]:
        y = (y**2)%m
        if int(i) == 1: y = (y*x)%m
    return y

def get_prime():
    x = random.randint(interval[0], interval[1])
    m0 = x if x%2 != 0 else x+1
    for i in range(m0, interval[1], 2):
        if(is_prime(i)) == 1: return i
    return get_prime()

def is_prime(p):
    if(p%3 == 0 or p%5 == 0 or p%7 == 0): return 0
    else: return miller_rabin(p)

def ds(p):
    d,s = p-1,0
    while(d%2 == 0):
        d = d//2
        s +=1
    return d,s

def miller_rabin(p):
    d,s = ds(p)
    for i in range(10):
        prime = 0
        x = random.randint(1,p)
        if gcd(x,p) != 1: return 0
        num = gorner(x,d,p)
        if num == 1 or num-p == -1: prime = 1
        else:
            for r in range(1, s):
                num = gorner(num,2,p)
                if num - p == -1:
                    prime = 1
                    break
                elif num == 1: return 0
        if not prime: return 0
    return 1

def gen_keys():
    p, q = get_prime(), get_prime()
    while p == q: p = get_prime()
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randint(2,phi-1)
    while(gcd(e,phi) != 1): e = random.randint(2,phi-1)
    d = inverse(e,phi)%phi
    return (e,n,d)

class Node():
    def __init__(self):
        self.e = 0
        self.n = 0
        self.d = 0

    def GenerateKeyPair(self,n):
        self.e, self.n, self.d = gen_keys()
        while self.n < n:
            self.e, self.n, self.d = gen_keys()

    def Encrypt(self, data, e, n):
        return gorner(data, e, n)

    def Decrypt(self, data, d, n):
        return gorner(data, d, n)

    def Sign(self, data):
        return gorner(data, self.d, self.n)

    def Verify(self,data,sign,e,n):
        return gorner(sign,e,n) == data

    def SendKey(self,data,e,n):
        data1 = self.Encrypt(data,e,n)
        sign = self.Sign(data)
        sign1 = self.Encrypt(sign,e,n)
        return (data1,sign1)

    def ReceiveKey(self,pack,e,n):
        data = self.Encrypt(pack[0],self.d,self.n)
        sign = self.Decrypt(pack[1],self.d,self.n)
        return self.Verify(data,sign,e,n)

    def Print(self):
        print('e', self.e)
        print('n', self.n)
        print('d', self.d)

A = Node()
B = Node()
B.GenerateKeyPair(0)
A.GenerateKeyPair(B.n)
A.Print()

k = random.randint(1, 2**256-1)
print(k)
ks = A.SendKey(k,B.e,B.n)
result = B.ReceiveKey(ks,A.e,A.n)
print(result)

