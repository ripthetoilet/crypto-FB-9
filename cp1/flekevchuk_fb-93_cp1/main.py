from collections import Counter, OrderedDict
from math import log2
from os import write 


file = open("my.txt", encoding="utf8")

f2 = open('test_gap.txt', 'w' ,encoding="utf8")
alphabet = "_абвгдеёжзийклмнопрстуфхцчшщыьэюя"
my_str = file.read().replace("ъ","ь").lower()
#f2 = open('test.txt', 'w' ,encoding="utf8")
#my_str = file.read().replace("ъ","ь").replace("_", "").lower()
#alphabet = "абвгдеёжзийклмнопрстуфхцчшщыьэюя"



def Entr(counter, l):
    entr = 0
    for i in counter:
        p = counter[i] / l
        entr += -p*log2(p)
    return entr

def printTable(counter, alphabet, name):
  f2.write(name+"\n")
  f2.write("  ")
  Sum = sum(counter.values())
  for letter in alphabet:
    f2.write('       '+letter+" ")
  f2.write("\n")
  for i in alphabet:
    f2.write(i+" ")
    for j in alphabet:
      f = counter[i + j]/Sum
      f2.write(str('%.6f' % f)+" ")
    f2.write("\n")
  f2.write("\n")



l = len(my_str)
if l % 2 :
  my_str += 'а'
l = l + (l % 2)


arr = []
j = 0
while j <= l-1:
  arr.append(my_str[j] + my_str[j+1])
  j += 2


arr1 = []
k = 0
while k < (l - 1):
  arr1.append(my_str[k] + my_str[k+1])
  k += 1


letters = OrderedDict(Counter(my_str).most_common()) 
cK = Counter(arr)
cS = Counter(arr1)



print("ЛIТЕРИ")
print("ЕНТРОПIЯ:", Entr(letters, sum(letters.values())))
for letter in letters.keys():
  print(letter + " :", letters[letter], end=", ")
print()
print()



print("ПРОСТI БIГРАМИ")
print("ЕНТРОПIЯ:", Entr(cK, sum(cK.values())))
printTable(cK, alphabet, "ПРОСТI БIГРАМИ")
print()

print("ПЕРЕХРЕСТНI БIГРАМИ")
print("ЕНТРОПIЯ:", Entr(cS, sum(cS.values())))
printTable(cS, alphabet, "ПЕРЕХРЕСТНI БIГРАМИ")







