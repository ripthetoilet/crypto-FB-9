from random import randint

def get_ds(p):
    p -= 1
    s = 0
    while p % 2 == 0:
        p /= 2
        s += 1
    return (int(p), s)

def strongly_prime(p, a, d):
    return pow(a, d, p) == 1

def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    print(f"gcd {a + b}")
    return a + b

def Millera_Rabina(p):
    ds = get_ds(p)
    d = ds[0]
    s = ds[1]
    if not(strongly_prime(p, 2, d)) or not(strongly_prime(p, 3, d)) or not(strongly_prime(p, 5, d)) or not(strongly_prime(p, 7, d)):
        #problem here
        return False
    k = 0
    while k < 5:
        x = randint(2, p - 1)
        if gcd(x, p) > 1:
            return False
        xd = pow(x, d, p)
        check_sp = False
        print(f"xd {xd}")
        if xd == 1 or xd == p - 1:
            check_sp = True
        else:
            for r in range(1, s):
                xr = pow(x, d * pow(2, r), p)
                if xr == p - 1:
                    check_sp = True
                    break
                if xr == 1:
                    return False
        if check_sp:
            k += 1
        else:
            return False
    return True

def generate_prime(length):
    p = randint(pow(2, length - 1), pow(2, length) - 1)
    while not(Millera_Rabina(p)):
        p = randint(pow(2, length - 1), pow(2, length) - 1)
    return p

def generate_pq(length):
    p0 = generate_prime(length)
    q0 = generate_prime(length)
    p1 = generate_prime(length)
    q1 = generate_prime(length)
    while p0 * q0 > p1 * q1:
        p0 = generate_prime(length)
        q0 = generate_prime(length)
        p1 = generate_prime(length)
        q1 = generate_prime(length)
    return ((p0, q0), (p1, q1))

def generate_e(fn):
    e = randint(2, fn - 1)
    while gcd(e, fn) > 1:
       e = randint(2, fn - 1)
    return e

def get_q(a, b):
    q = []
    while a > 0 and b > 0:
        if a > b:
            q.append(int(a / b))
            a %= b
        else:
            q.append(int(b / a))
            b %= a
    return q

def generate_d(e, fn):
    q = get_q(e, fn)
    result = []
    result.append(0)
    result.append(1)
    for i in range(0, len(q)):
        qi = -q[i]
        if qi < 0:
            qi += fn
        result.append(((qi * result[i + 1]) + result[i]) % fn)
    return result[len(q)]

def generate_key_pair(length):
    pq = generate_pq(length)
    p0 = pq[0][0]
    q0 = pq[0][1]
    p1 = pq[1][0]
    q1 = pq[1][1]
    n0 = p0 * q0
    n1 = p1 * q1
    fn0 = (pq[0][0] - 1) * (pq[0][1] - 1)
    fn1 = (pq[1][0] - 1) * (pq[1][1] - 1)
    #e = pow(2, 16) + 1
    e0 = generate_e(fn0)
    e1 = generate_e(fn1)
    d0 = generate_d(e0, fn0)
    d1 = generate_d(e1, fn1)
    return ((d0, p0, q0, e0, n0), (d1, p1, q1, e1, n1))

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)
    
def sign(k, e1, n1, d0, n0):
    k1 = encrypt(k, e1, n1)
    s = decrypt(k, d0, n0)
    s1 = encrypt(s, e1, n1)
    return (k1, s1)

def verify(k1, s1, d0, n0, e1, n1):
    k = decrypt(k1, d0, n0)
    s = decrypt(s1, d0, n0)
    return k == encrypt(s, e1, n1)

class Abonent():
    def __init__(self, d, n, e):
        self.d = d
        self.n = n
        self.e = e
        self.n1 = None
        self.e1 = None
    
    def send_key(self):
        return (self.n, self.e)
        
    def receive_key(self, n, e):
        self.n1 = n
        self.e1 = e
    
    def sign(self, k):
        return sign(k, self.e1, self.n1, self.d, self.n)
    
    def verify(self, k1, s1):
        return verify(k1, s1, self.d, self.n, self.e1, self.n1)
    
    def encrypt(self, m):
        return encrypt(m, self.e1, self.n1)
    
    def decrypt(self, c):
        return decrypt(c, self.d, self.n)

'''n0 = 21353
n1 = 24797
e0 = 11737
e1 = 14681
d0 = 253
d1 = 23081'''

'''n0 = 55807 * 52453
n1 = 57881 * 37967
e0 = 65537
e1 = 65537
d0 = 1134194417
d1 = 1832294113'''

n0 = 52622220475598969490721398935974048775681853730182318303247844914006010162651
n1 = 57197323623783137744185393797014637108026306442881434994537357193565601285027
e0 = 65537
e1 = 65537
d0 = 3871772390151185298140875927632739722509480193588874348521533747554806976097
d1 = 20760070449348146810518302062187576069655310060164135683291734538113638779833

user1 = Abonent(d0, n0, e0)
user2 = Abonent(d1, n1, e1)

keys = user2.send_key()
user1.receive_key(keys[0], keys[1])
keys = user1.send_key()
user2.receive_key(keys[0], keys[1])

k = 7
ks = user1.sign(k)
print(user2.verify(ks[0], ks[1]))

print(user1.decrypt(user2.encrypt(123456789012345678901234567890)))