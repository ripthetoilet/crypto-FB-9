from collections import Counter

alph = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
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
     d = gcd(a,n)
     if d < 1: return 0
     elif d == 1: return (inverted(a,n)*b)%n
     else:
          if b%d == 0:
               a, b, n = a//d, b//d, n//d
               x = []
               x1 = equation(a, b, n)
               for i in range(d):
                    x.append(x1 + i*n)
               return x
     return 0

def bigramsfreq(text):
     bigrams = []
     for i in range(0, len(text) - 1, 2):
          bigrams.append(text[i:i+2])
     return list(dict(sorted(Counter(bigrams).items(), key=lambda item: item[1], reverse = True)).keys())[:5]

print(bigramsfreq(ciphertext))