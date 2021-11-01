from collections import Counter

def VishenerDecode(text, key): 
  j = 0
  size = len(text) - len(key)
  arr=[]
  while j < size:
    i = 0
    while i < len(key):
        arr.append(chr((((ord(text[i+j])-ord(key[i])) ) % 32) + 1072))
        i+=1
    j+=len(key)
  return ''.join([str(elem) for elem in arr])

def VishenerEncode(text, key): 
  j = 0
  size = len(text) - len(key)
  arr=[]
  while j < size:
    i = 0
    while i < len(key):
        arr.append(chr((((ord(text[i+j]) + ord(key[i])) - 1072 * 2) % 32) + 1072))
        i+=1
    j+=len(key)
  return ''.join([str(elem) for elem in arr])


def IndexCounter(text, key_len): 
  I = 0
  i = 0
  arr = []
  size = len(text) - key_len
  n = size / key_len
  while i < key_len:
    j=0
    s = ''
    while j < size:
      s+=text[j+i]
      j+=key_len
    x = Counter(s)
    arr.append(x.most_common(1)[0][0])
    for a in x:
      I += x[a] * (x[a] - 1)
    i+=1
  arr.append(I / (n-1) / n / key_len)
  return arr

def kroneker(text, key_len): 
  D = 0
  i = 0
  n = len(text)
  while i < (n - key_len):
    D+=text[i] == text[i+key_len]
    i+=1
  return D

def PrintKroneker(text):
  start = 10
  while start <= 20:
    print(kroneker(text,start), ' - key length=' ,start)
    start+=1

def parsKey(s, string = 'оеоооеооооооао'): # Параметр string- найчатстіший символ в ВТ.
  key = ''
  h = len(s) - 1
  i = 0
  while i < h: 
    f = (ord(s[i]) - ord(string[i]))%32 + 1072 
    key+=chr(f)
    i+=1
  return key

name = 'main'

if name == 'main':
  arr = ['рв','узс','зслу','вшувз','флфлцхювге','аопретиоенк','аопренлскгек','аопренлскгеки','аопренксокекик','ащпренксбкекокв','рщпленксйкефоква','роплжнксйкпфокваз','ьрплжнксйюпфоквазр','ьрплжнксйюпфоявалщо','ьрплжносйюмфоявалщро']

  file1 = open("test.txt", encoding="utf8")
  text1 = file1.read().lower().replace('_','')
  i = 0 

  print('Методом Індексів')
  while i<4:
    stext = VishenerEncode(text1, arr[i])
    j = 2
    print('key=', arr[i], ' len=', len(arr[i]))
    while j < 6:
      print(j,IndexCounter(stext, j)[j])
      j+=1
    i+=1

  print('Методом кронекера')
  while i<len(arr):
    stext = VishenerEncode(text1, arr[i])
    print('key=', arr[i], ' len=', len(arr[i]))
    PrintKroneker(stext)
    i+=1

  print('\n\n')
  print('Результати аналізу наданого ШТ')
  file = open("text.txt", encoding="utf8")
  text = file.read()
  print('Методом кронекера')
  PrintKroneker(text)
  analis = IndexCounter(text, 14)
  print(analis)
  print('key=',parsKey(analis))
  print(VishenerDecode(text, parsKey(analis)))


