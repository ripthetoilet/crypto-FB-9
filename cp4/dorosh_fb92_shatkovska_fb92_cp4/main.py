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
        p.append(p[-1] * (-q) + p[-2])
    return gcd_val, p[-2]  # returns gdc and a^-1


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
            if pow(x, d, p) in [1, -1]:
                return True
            else:
                xr = pow(x, 2 * d, p)  # if r == 1
                for r in range(2, s - 1):
                    xr = pow(xr, d * (2 ** r), p)
                    if xr == -1:
                        return True
                    elif xr == 1:
                        return False
                    else:
                        continue
        counter += 1
    return True


# print(miller_rabin(97, 10))             # prime
# print(miller_rabin(21881, 10))          # prime
# print(miller_rabin(11, 10000))


def generate_prime(bits):
    while True:
        a = (rand.randrange(1 << bits - 1, 1 << bits) << 1) + 1  # making sure its odd
        if miller_rabin20(a, 1000):
            return a


#for b in range(1, 10):
#    a = generate_prime(256)
#    print(a)
#    print(miller_rabin(a, 10000))


def generate_pq_pair(bits):
    pair0 = (generate_prime(bits), generate_prime(bits))
    return pair0

    # while True:
    #     pair1 = (generate_prime(bits), generate_prime(bits))
    #     if pair0[0]*pair0[1] <= pair1[0]*pair1[1]:
    #         return pair0, pair1


#print(generate_pq_pair(256))


def generate_e(phin):
    while True:
        e = rand.randrange(2, phin)
        if gcd(e, phin)[0] == 1:
            return e


def decode(message):
    message = int(message.encode('utf-8').hex(), 16)
    return message


def encode(message):
    message = bytes.fromhex(hex(message)[2:]).decode('ASCII')
    return message


class User:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.e = 0
        self.d = 0
        self.other_e = 0
        self.other_n = 0

    def generate_keys(self):
        bits = 256
        self.p, self.q = generate_pq_pair(bits)
        print("p: ", self.p)
        print("q: ", self.q)
        self.n = self.p * self.q
        print("n: ", hex(self.n))
        print("n: ", self.n)
        phin = (self.p - 1) * (self.q - 1)
        print("phin ", phin)
        self.e = generate_e(phin)
        print("e: ", hex(self.e))
        print("e: ", self.e)
        self.d = gcd(self.e, phin)[1]
        print("d: ", self.d)
        return self.n, self.e

    # !!!may be combined with generate_keys() later
    def generate_correct_keys(self):  # for user A to choose correct keys (other.n <= n)
        while self.other_n > self.generate_keys()[0]:
            continue

    def encrypt(self, message):  # message needs to be decoded from utf-8
        encrypted = pow(message, self.other_e, self.other_n)
        return encrypted

    def decrypt(self, message):
        decrypted = pow(message, self.d, self.n)
        return decrypted  # message needs to be encoded as utf-8

    def sign(self, message):
        signed = pow(message, self.d, self.n)
        return signed

    def verify(self, signed, decrypted_message):
        return self.encrypt(signed) == decrypted_message

    def send_keys(self):
        return self.e, self.n

    def receive_keys(self, ne):
        other_e, other_n = ne
        self.other_e = other_e
        self.other_n = other_n

    def send_message(self, text):
        message = decode(text)
        encrypted = self.encrypt(message)
        signed = self.sign(message)
        encrypted_signed = self.encrypt(signed)

        return encrypted, encrypted_signed

    def receive_message(self, mess):
        encrypted, encrypted_signed = mess
        decrypted_message = self.decrypt(encrypted)
        signed = self.decrypt(encrypted_signed)

        if self.verify(signed, decrypted_message):
            return encode(decrypted_message)
        else:
            return -1


# full process of A sending a message to B
# B creates its keys and shares open keys (eb, nb) with A
B = User()
print('----B(receiver)----')
#B.p, B.q = 103835454004010444475409003854210074261052797710727434506730740994576540292549, 107183942186644795663013170513487322474709650968506496840759600348701209297809
print(B.generate_keys())

# A receives keys
A = User()
A.receive_keys(B.send_keys())

# A creates its keys (nb < na) and shares its keys (ea, na) with B
# B receives A's keys and message
print('----A(sender)----')
# A.p, A.q = 70317581449694745210302262109675257694763094290943582629081758774713756924661, 111474892525671121441034990722997074779401637226860425603805600209559178723349
# print(A.q*A.p<=B.p*B.q)
# print()
print(A.generate_correct_keys())
B.receive_keys(A.send_keys())

# A sends signed message and encrypted message to B
# B receives A's message, decrypts signed message and encrypted message and verifies signed message
M = "Hi there!"
received = B.receive_message(A.send_message(M))
print("Message: ", received)


# testing at the site
def test(mod, sig):
    C = User()
    C.other_n = int(mod, 16)  # n
    C.other_e = int(sig, 16)  # e

    print(C.generate_correct_keys())

    C.send_message("Hi there!")


receiver_n = "C6FF016AD331C3A925B12B36AD00A332F3E72C9E714B8B87C51D5D4CC8DD352EEE1511447858260FA29876A2B642E711496BDAAE491E43612A71EF1FFD246757"
receiver_e = "10001"
# test(receiver_n, receiver_e)
# test(receiver_n, receiver_e)
