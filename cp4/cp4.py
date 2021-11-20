import random 
LOW = pow(2, 255) + 1
HIGH = pow(2, 256) - 1

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

pair1 = (getran(), getran())
pair2 = (getran(), getran())
if pair1[0] * pair1[1] > pair2[0] * pair2[1]: pair1, pair2 = pair2, pair1
print(pair1)
print(pair2)