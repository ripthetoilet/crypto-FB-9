import re
import collections
import math
from collections import Counter
import numpy as np
import pandas as pd

text1 =open("text.txt",encoding="utf-8").read().lower().replace("ъ", "ь").replace("ё", "е").replace(" ","")
text2 =open("text.txt",encoding="utf-8").read().lower().replace("ъ", "ь").replace("ё", "е")
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
#print(Bigram1())


#для біграм що не перетинаються
def Bigram2(text):
    i =0
    arr2=[]
    for i in np.arange(0,len(text)-1,2):
        arr2.append(text[i]+text[i+1])     
    return arr2

#print(Bigram2())

#без пробелов
bigram1 = Counter(Bigram1(text1))
bigram2 = Counter(Bigram2(text1))
#с пробелами
bigram1s=Counter(Bigram1(text2))
bigram2s = Counter(Bigram2(text2))



#частота биграм
def BigramFrequancy(bigram,text):
    bigramfreq=[]
    for i in bigram:
        bigramfreq.append(bigram[i]/len(text))
        #print(bigramfreq)
    return bigramfreq

print(BigramFrequancy(bigram1,text1))

 #частота букв
def LetterFrequancy(letters,Alphabet,text):
    letterfreq=[]
    for i in Alphabet:
        letterfreq.append(letters[i]/len(text))
        #print(i,letterfreq)
    return letterfreq
#print(LetterFrequancy(letters,Alphabet2))

#H2
def EntropyBigram(bigramfreq):
    Entropy =0
    for i in bigramfreq:
        Entropy += -i*math.log(i,2)
    return Entropy/2

print(EntropyBigram(BigramFrequancy(bigram1,text1)))
print(EntropyBigram(BigramFrequancy(bigram2,text1)))
print(EntropyBigram(BigramFrequancy(bigram1s,text2)))
print(EntropyBigram(BigramFrequancy(bigram2s,text2)))

#H1
def EntropyLetters(letterfreq):
    Entropy =0
    for i in letterfreq:
        Entropy += -i*math.log(i,2)
    return Entropy
print(EntropyLetters(LetterFrequancy(letters1,Alphabet1,text1)))
print(EntropyLetters(LetterFrequancy(letters2,Alphabet2,text2)))
#LetterFrequancy(letters)

def redandancy1(letters,Alphabet,text):
    return 1 - EntropyLetters(LetterFrequancy(letters,Alphabet,text))/math.log(31,2)
def redandancy2(letters,Alphabet,text):
    return 1 - EntropyLetters(LetterFrequancy(letters,Alphabet,text))/math.log(32,2)

print(redandancy1(letters1,Alphabet1,text1))
print(redandancy2(letters2,Alphabet2,text2))

