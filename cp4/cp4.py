import random 
LOW = pow(2, 255) + 1
HIGH = pow(2, 256) - 1

gcd = lambda a, b: a if b == 0 else not a % b and b or gcd(b , a % b)
encode = lambda msg: int(msg.encode('utf-8').hex(), 16)
decode = lambda msg: bytes.fromhex(hex(msg)[2:]).decode('ASCII')
encrypt = lambda msg, e, n: pow(msg, e, n)
decrypt = lambda msg, d, n: decode(pow(msg, d, n))
sign = lambda msg, d, n: pow(msg, d, n)
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

class abonent():

    def __init__(self):
        self.n = 0
        self.e = 0
        self.d = 0

    def GenerateKeyPairSender(self, n):
        key = genkey()
        self.n = key[0][0]
        self.e = key[0][1]
        self.d = key[1]       
        while n < self.n:
            key = genkey()
            self.n = key[0][0]
            self.e = key[0][1]
            self.d = key[1]

    def GenerateKeyPairReceiver(self):
        key = genkey()
        self.n = key[0][0]
        self.e = key[0][1]
        self.d = key[1]          
        
    def Encrypt(self, msg, e, n):
        if isinstance(msg, str): return encrypt(encode(msg), e, n)
        else: return encrypt(msg, e, n)

    def Decrypt(self, msg):
        return decrypt(msg, self.d, self.n)

    def Sign(self, msg):
        return sign(encode(msg), self.d, self.n)

    def Verify(self, msg, signature, e, n):
        return verify(msg, signature, e, n)

    def SendKey(self, msg, e, n):
        signature = self.Encrypt(self.Sign(msg), e, n)
        msg = self.Encrypt(msg, e, n)
        return (msg, signature)

    def ReceiveKey(self, packet, e, n):
        msg = self.Decrypt(packet[0])
        if self.Verify(msg, packet[1], e, n): print('authentication failed')
        return msg

Alice = abonent()
Bob = abonent()

msg = 'hello, my name is tolya its pleasure for me to meet you'

Bob.GenerateKeyPairReceiver()
Alice.GenerateKeyPairSender(Bob.n)

packet = Alice.SendKey(msg, Bob.e, Bob.n)
output = Bob.ReceiveKey(packet, Alice.e, Alice.n)

print(output)