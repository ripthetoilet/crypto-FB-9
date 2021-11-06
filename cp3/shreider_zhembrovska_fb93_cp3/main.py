from collections import Counter
import math

alph = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
m = len(alph)

with open('ciphertext.txt', 'r', encoding = 'utf-8') as f:
     text = f.read()
ciphertext = ''.join(i for i in text if i in alph)

def gcd(a,b):
     while a != 0 and b != 0:
          if a > b: a = a % b
          else: b = b % a
     return a+b

def inverted(a,n):
     q = [0,1]
     while a != 0 and n != 0:
          if a > n: q.append(a // n); a = a % n
          else: q.append(n // a); n = n % a
     for i in range(2,len(q)): q[i] = q[i-2] - q[i]*q[i-1]
     return q[-2]

def equation(a,b,n): # ax=b modn
     a, b = a%n, b%n
     d = gcd(a,n)
     x = []
     if d < 1: return x
     elif d == 1: x.append((inverted(a,n)*b)%n)
     else:
          if b%d == 0:
               a, b, n = a//d, b//d, n//d
               x.append((equation(a, b, n)[0]))
               for i in range(1,d):
                    x.append(x[-1] + n)
     return x

def decryption(text,key):
     plaintext = []
     a, b = key[0], key[1]
     for i in range(0, len(text)-1, 2):
          x = (inverted(a,m**2)*(bvalue(text[i:i+2])-b))%(m**2)
          plaintext.append(alph[x//m]+alph[x%m])
     return ''.join(i for i in plaintext)

def bvalue(bigram):
     return alph.index(bigram[0])*m + alph.index(bigram[1])

def findkeys(text):
     keys = []
     bsys = systems(text)
     for i in bsys:
          k = ikey(i)
          if len(k) != 0:
               for j in range(len(k)): keys.append(k[j])
     return keys

def ikey(system):
     x1, x2, y1, y2 = bvalue(system[0][0]), bvalue(system[1][0]), bvalue(system[0][1]), bvalue(system[1][1])
     keys = []
     a = equation(x1 - x2, y1 - y2, m**2)
     for i in a:
          if gcd(i, m) != 1: continue
          b = (y1 - i * x1) % m**2
          keys.append((i,b))
     return keys

def systems(text):
     toplang = ['ст', 'но', 'ен', 'то', 'на']
     toptext = bigramsfreq(text)
     pairs, systems = [], []
     for i in toplang:
          for j in toptext: pairs.append((i,j))
     for i in pairs:
          for j in pairs:
               if i == j or (j, i) in systems: continue
               systems.append((i,j))
     return systems

def bigramsfreq(text):
     bigrams = []
     for i in range(0, len(text) - 1, 2):
          bigrams.append(text[i:i+2])
     return list(dict(sorted(Counter(bigrams).items(), key=lambda item: item[1], reverse = True)).keys())[:5]

def entropy(text):
    length = len(text)
    freq = Counter(text)
    for i in freq:
        freq[i] /= length
    result = -1 * sum(freq[k] * math.log(freq[k], 2) for k in freq)
    return result

def ok(keys):
     for i in keys:
          top = list(dict(sorted(Counter(decryption(ciphertext, i)).items(), key=lambda item: item[1], reverse=True)).keys())
          if top[0] != 'о': continue
          e = entropy(decryption(ciphertext,i))
          if 4.4 < e and 4.5 > e: return i
     return False

print(ok(findkeys(ciphertext)))