from array import *
import math
from collections import Counter
import re
import random
I = 0.0553
alphavit = "абвгдежзийклмнопрстуфхцчшщыьъэюя"
x = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэф'
# Очистка файла
def clear_file(name, text):
    clear_text=text.replace("\n", " ").replace("\r", "").lower().replace("ё", "е").replace(" ","")
    for char in clear_text[:]:
            if char not in alphavit:
                clear_text = clear_text.replace(char, "")
    fout = open(name + '_clear.txt', "w", encoding='utf-8')
    fout.write(clear_text)
    fout.close()
def compliance_index(mass):
    index = 0
    i = 0
    counts = Counter(mass)
    while(i < len(alphavit)):
        for l in sorted(counts):
            if(alphavit[i] == l):
                index += counts[l]*(counts[l]-1)
        i += 1
    index = index * (1/(len(mass)*(len(mass)-1)))
    return index
def CT_segmentation(text, r):
    mass = []
    i = 0
    while(i<r):
        mass.append('')
        i += 1
    i = 0
    while(i<r):
        j = i
        while(j<len(text)):
            mass[i] = mass[i] + text[j]
            j = j + r
        i += 1
    return mass
def Char_int(a):
    return ord(a) - 1072
def Int_char(a):
    return chr(a + 1072)
def Encrypt(text, key):
    encrypted = ''
    for i, char in enumerate(text):
        x = Char_int(char)
        y = (x + Char_int(key[i % len(key)])) % 32
        encrypted = encrypted + Int_char(y)
    return encrypted
def Decrypt(text, key):
    decrypted = ''
    for i, char in enumerate(text):
        x = Char_int(char)
        y = (x - Char_int(key[i % len(key)])) % 32
        decrypted = decrypted + Int_char(y)
    return decrypted
def KeyFound(text):
    j = 0
    mass = ''
    while(j<len(x)):
        i = 0
        key = ''
        while(i<len(text)):
            mass = Counter(text[i])
            mass1 = sorted(mass, key=mass.get, reverse = True)
            key = key + Int_char((Char_int(mass1[0]) - Char_int(x[j]))%32)
            i += 1
        print(key)
        j += 1
# def min(It, Ir):
#     minimum = abs(It - Ir[0])
#     i = 1
#     while(i<len(Ir)-1):
#         if(minimum>abs(It-Ir[i])):
#             minimum = abs(It-Ir[i])
#         i += 1
#     return minimum
def main():
    # filename = 'var6'
    # fin = open(filename + '.txt', "r", encoding='utf-8')
    # filetext = fin.read()
    # fin.close()
    # clear_file(filename, filetext)
    fin = open('var6_clear.txt', "r", encoding='utf-8')
    filetext = fin.read()
    fin.close()
    encryptedtext = filetext
    # Завдання 1-2
    r = 2
    while(r<21):
        key = ''
        m = 0
        while(m<r):
            key = key + alphavit[random.randint(0, len(alphavit)-1)]
            m +=1
        textt = Decrypt(encryptedtext, key)
        Ir = compliance_index(textt)
        print('Key: ' + key +', Index: ' + str(Ir))
        r += 1 
    # Завдання 3
    r = 2
    while(r<31):
        Y = []
        Y = CT_segmentation(encryptedtext, r)
        k = 0
        med = 0
        while(k<r):
            index = compliance_index(Y[k])
            print('I(Y'+ str(k) +') = ' + str(index))
            med = med + index
            k += 1
        print()
        med = med/r
        if(abs(I-med)>abs(med - 1/32)):
            r += 1
        else:
            print('Size of key '+ str(r))
            KeyFound(Y)
            INPUT = input('Input "right" key ')
            print(Decrypt(encryptedtext, INPUT))
            return 0
main()
        
