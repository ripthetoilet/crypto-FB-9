import re
import collections
import math
from collections import Counter
import numpy as np
import pandas as pd
from tabulate import tabulate

Alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф','х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
with open("01.txt",'r',encoding='utf-8') as f1:
    text=f1.read().lower().replace("ъ", "ь").replace("ё", "е").replace("\n","")
VT_birgams = ['ст','но','то','на','ен']

def Bigram(text):
    i =0
    arr1=[]
    for i in range(len(text)-1):
        arr1.append(text[i]+text[i+1])              
    return arr1

def BigramFrequancy(bigram):
    bigramfreq=[]
    for i in bigram:
        bigramfreq.append(bigram[i]/sum(bigram.values()))       
    return bigramfreq

def Top_bigrams(text):
    top_bigrams =[]
    bigram_counter = Counter(Bigram(text))
    bigramfreq=dict(list(zip(bigram_counter,BigramFrequancy(bigram_counter))))
    bigramfreq=sorted(bigramfreq, key=lambda x:x[1], reverse=True)
    # print(bigramfreq)
    c= Counter(bigramfreq)
    most_common_bigrams=c.most_common(5)
    top_bigrams=[key for key, value in most_common_bigrams]
    return top_bigrams
    
def Gcd(val1,val2):
    if val1==0:
        return val2,1, 0
    else:
        div, x, y = Gcd(val2 % val1, val1)
    return div, y -(val2 // val1)*x, x
    

def Reversed_element(elem, mod):
    div, y,x = Gcd(elem, mod)
    if Gcd ==1:
        return (y % mod + mod)%mod
    else: return -1

# def Equation(text):



# def Bigram_encription():

# def Bigram_decription():

# def Cipher(text):

# def Decipher(text):


# print(Top_bigrams(text))
print(Reversed_element(-4, 33))