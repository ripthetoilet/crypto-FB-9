from collections import Counter
from itertools import permutations

popularBigramInLanguage = ['ст', 'но', 'ен', 'то', 'на', 'ов', 'ни', 'ра', 'во', 'ко']

def GCD(a,b):
  arr = []
  while a>0 and b>0:
    if a>b:
      arr.append(-(a//b))
      a %=b
    else :
      arr.append(-(b//a))
      b %=a
  return [arr, a + b]


def sum(arr):
  q1 = 0
  q2 = 1
  for q in arr:
    temp = q2
    q2 = q2 * q + q1
    q1 = temp
  return q1 

def revers(a, mod): 
  payload = GCD(a, mod) 
  rev = sum(payload[0])
  if rev > 0 :
    return [rev, payload[1]]
  return [rev+mod/payload[1], payload[1]]

def SolveEqution(a, b, mod):
  payload = revers(a, mod)
  if b % payload[1] == 0:
      i = 0
      arr = []
      x = ((b/payload[1]) * payload[0])%(mod/payload[1])
      while i < payload[1]:
        arr.append(i*(mod/payload[1]) + x)
        i+=1
      return arr

def getNumbe(leter):
  n = ord(leter)
  if n > ord('ъ'):
    return  n - 1073
  return n - 1072

def getChar(n):
  n += 1072
  if n >= ord('ъ'):
    n += 1
  return chr(int(n))

def ParsNumberFromBigram(bigram):
  n = getNumbe(bigram[0])
  n1 = getNumbe(bigram[1])
  return 31 * n + n1

def ParsBigramFromNumber(number):
  n = getChar(number//31)
  n1 = getChar(number % 31)
  return n + n1

def ParsKey(sb1,sb2, ub1,ub2):
  mod = 31**2
  X = ParsNumberFromBigram(ub1) - ParsNumberFromBigram(ub2)
  Y = ParsNumberFromBigram(sb1) - ParsNumberFromBigram(sb2)
  if X < 0:
    X += mod
  if Y < 0:
    Y += mod
  a = SolveEqution(X, Y, mod)
  if a:
    b = (ParsNumberFromBigram(sb1) - ParsNumberFromBigram(ub1) * a[0]) % mod
    if b < 0:
      b += mod
    return [a[0], b]

def CalcKeys(arr):
  i=0
  allA = []
  popular = ['ст', 'но', 'ен', 'ни', 'от'] 
  while i < 4 :
    res = ParsKey(arr[i],arr[i+1],popular[i],popular[i+1])
    allA.append(res)
    i+=1
  return allA

def deCode(key,bigram):
  num = ParsNumberFromBigram(bigram)
  rev = revers(key[0],31**2)[0]
  res = ((num-key[1])*int(rev))%(31**2)
  return ParsBigramFromNumber(res)


def PrintAllKeys(arr):
  perm = permutations(arr)
  arr = []
  for e in perm:
    arr += CalcKeys(e)
  return arr
    
def Analiz(text):
  arr1 = []
  f = 0
  while f < (l - 1):
    arr1.append(text[f:f+2])
    f += 1
  popular = [e[0] for e in Counter(arr1).most_common(5)] 
  print(popular)
  count = 0
  for bigram in popular:
    if bigram in popularBigramInLanguage:
      count+=1
  if count >= 3:
    return True
  return False 
    




    

file = open("text.txt", encoding="utf8")
my_str = file.read()


l = len(my_str)
arr1 = []
f = 0
while f < (l - 1):
  arr1.append(my_str[f:f+2])
  f += 1


cS = Counter(arr1).most_common(5)
popularS = [e[0] for e in cS]
print(popularS)

allKeys = PrintAllKeys(popularS)

for key in allKeys:
  newStr =''
  p = 0
  while p<len(my_str):
    newStr+=deCode([199,700],my_str[p:p+2])
    p+=2
  if Analiz(newStr):
    print(newStr[1]) 

 