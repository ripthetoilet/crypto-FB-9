import random 
LOW = pow(2, 255) + 1
HIGH = pow(2, 256) - 1
msg = 'hello, my name is tolik its pleasure for me to meet you'

gcd = lambda a, b: a if b == 0 else not a % b and b or gcd(b , a % b)
encode = lambda msg: int(msg.encode('utf-8').hex(), 16)
decode = lambda msg: bytes.fromhex(hex(msg)[2:]).decode('ASCII')
encrypt = lambda msg, e, n: pow(encode(msg), e, n)
decrypt = lambda msg, d, n: decode(pow(msg, d, n))
sign = lambda msg, d, n: pow(encode(msg), d, n)
verify = lambda msg, sign, e, n: True if encode(msg) == pow(sign, e, n) else False

def milrab(num, r = 100):
    m = num - 1
    k = 0
    while not m & 1:
        k += 1
        m >>= 1
    a = random.randrange(2, num - 1)
    res = pow(a, m, num)
    if res == 1 or res == num - 1:
        return True
    else:
        for i in range(r):
            res = pow(res, 2, num)
            if res == num - 1: return True
            else: return False

def getran():
    num = random.randrange(LOW, HIGH)
    if num % 2 == 0: num += 1
    for i in range(num, HIGH, 2):
        if not milrab(i): continue
        else: return i

def genkey():
    pair = (getran(), getran())
    n = pair[0] * pair[1]
    phi = (pair[0] - 1) * (pair[1] - 1)
    e = random.randrange(2, phi)
    while(gcd(e,phi) != 1): e = random.randrange(2, phi)
    d = pow(e, -1, phi)
    openkey = (n, e)
    return (openkey, d)

keysA  = genkey()
NA, EA = keysA[0]
da = keysA[1]
print('na = ', NA)
print('ea = ', EA)
print('da = ', da)
keysB  = genkey()
NB, EB = keysB[0]
db = keysB[1]
print('\nnb = ', NB)
print('eb = ', EB)
print('db = ', db)
while NA < NB: 
    print('generate new keys for A')
    keysA  = genkey()
    NA, EA = keysA[0]
    da = keysA[1]
    print('na = ', NA)
    print('ea = ', EA)
    print('da = ', da)
print('----------------------------------------------------')