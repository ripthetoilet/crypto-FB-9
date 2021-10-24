import re
import collections
import math
from collections import Counter
from typing import Dict
import numpy as np
import pandas as pd
from tabulate import tabulate
from itertools import islice

text =open("text.txt",encoding="utf-8").read().lower().replace("ъ", "ь").replace("ё", "е")
text1= re.sub("[^а-я]","",text)
text2= re.sub("[^а-я]"," ",text)
text2.split()
text2 = ' '.join(text2.split())
Alphabet1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф','х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
Alphabet2 = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф','х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
letters1 = Counter(text1)
letters2=Counter(text2)
 
#для перехресних біграм 
def Bigram1(text):
    i =0
    arr1=[]
    for i in range(len(text)-1):
        arr1.append(text[i]+text[i+1])              
    return arr1

#для біграм що не перетинаються
def Bigram2(text):
    i =0
    arr2=[]
    for i in np.arange(0,len(text)-1,2):
        arr2.append(text[i]+text[i+1])     
    return arr2

#без пробелов
bigram1 = Counter(Bigram1(text1))
bigram2 = Counter(Bigram2(text1))
#с пробелами
bigram1s=Counter(Bigram1(text2))
bigram2s = Counter(Bigram2(text2))

#частота биграм
def BigramFrequancy(bigram):
    bigramfreq=[]
    for i in bigram:
        bigramfreq.append(bigram[i]/sum(bigram.values()))
        #print(bigramfreq)
    return bigramfreq

 #частота букв
def LetterFrequancy(letters,Alphabet,text):
    letterfreq=[]
    for i in Alphabet:
        letterfreq.append(letters[i]/len(text))
    return letterfreq

#H2
def EntropyBigram(bigramfreq):
    Entropy =0
    for i in bigramfreq:
        Entropy += -i*math.log(i,2)
    return Entropy/2

#H1
def EntropyLetters(letterfreq):
    Entropy =0
    for i in letterfreq:
        Entropy += -i*math.log(i,2)
    return Entropy

def redandancy1(letters,Alphabet,text):
    return 1 - EntropyLetters(LetterFrequancy(letters,Alphabet,text))/math.log(len(Alphabet),2)
def redandancy2(bigram,Alphabet):
    return 1 - EntropyBigram(BigramFrequancy(bigram))/math.log(len(Alphabet),2)

def PrintLetterTable(letters,Alphabet,text,name, filename):
    dic=dict(list(zip(letters,LetterFrequancy(letters,Alphabet,text))))
    dic={k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
    data=pd.DataFrame.from_dict(dic,'index', columns=[name])
    print(tabulate(data, headers='keys', tablefmt='grid'))
    file=open(filename,'w',encoding="utf-8")
    file.write(tabulate(data, headers='keys', tablefmt='grid'))

def PrintBigramTable(bigram,name,filename):
    dic=dict(list(zip(bigram,BigramFrequancy(bigram))))
    dic=dict(sorted(dic.items()))
    file=open(filename,'w',encoding="utf-8")
    data=pd.DataFrame.from_dict(dic,'index', columns=[name])
    file.write(tabulate(data, headers='keys', tablefmt='grid'))
    
def PrintBigramTop(bigram,name):
    dic=dict(list(zip(bigram,BigramFrequancy(bigram))))
    sorted_keys= sorted(dic, key=dic.get, reverse=True)[:20]
    sorted_dict = {}
    for i in sorted_keys:
        sorted_dict[i] = dic[i]
    data=pd.DataFrame.from_dict(sorted_dict,'index',columns=[name])
    print(tabulate(data, headers='keys', tablefmt='grid'))
    
PrintBigramTable(bigram1,"Перехресні біграми без пробілів","bigram1.txt")
PrintBigramTable(bigram2,"Прості біграми без пробілів","bigram2.txt")
PrintBigramTable(bigram1s,"Перехресні біграми з пробілами","bigram1s.txt")
PrintBigramTable(bigram2s,"Прості біграми з пробілами","bigram2s.txt")

print("Частоти літер")
PrintLetterTable(letters1,Alphabet1,text1,"Без пробілів", "letters1.txt")
PrintLetterTable(letters2,Alphabet2,text2,"З пробілами","letters2.txt")

print("Топ 20 біграм")
PrintBigramTop(bigram1,"Перехресні біграми без пробілів")
PrintBigramTop(bigram2,"Прості біграми без пробілів")
PrintBigramTop(bigram1s,"Перехресні біграми з пробілами")
PrintBigramTop(bigram2s,"Прості біграми з пробілами")

print("\nЕнтропія для букв без пробілів: ", EntropyLetters(LetterFrequancy(letters1, Alphabet1, text1)))
print("Надлишковість: ", redandancy1(letters1, Alphabet1, text1))
print("\nЕнтропія для букв з пробілами: ", EntropyLetters(LetterFrequancy(letters2, Alphabet2, text2)))
print("Redundancy: ", redandancy1(letters2, Alphabet2, text2))

print("\n\nЕнтропія для перехресних біграм без пробілів: ", EntropyBigram(BigramFrequancy(bigram1)))
print("Надлишковість: ", redandancy2(bigram1,Alphabet1))
print("\nЕнтропія для простих біграм без пробілів: ", EntropyBigram(BigramFrequancy(bigram2)))
print("Надлишковість: ", redandancy2(bigram2,Alphabet1))
print("\nЕнтропія для перехресних біграм з пробілами: ", EntropyBigram(BigramFrequancy(bigram1s)))
print("Надлишковість: ", redandancy2(bigram1s,Alphabet2))
print("\nЕнтропія для біграм з пробілами: ", EntropyBigram(BigramFrequancy(bigram2s)))
print("Надлишковість: ", redandancy2(bigram2s,Alphabet2))
