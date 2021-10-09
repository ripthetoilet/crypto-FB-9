from array import *
import math
from collections import Counter
import re
alphavit = "абвгдежзийклмнопрстуфхцчшщыьэюя "
# Очистка файла
def clear_file(name, mode):
    fin = open(name + '.txt', "r")
    text = fin.read()
    fin.close()
    if mode == True:
        clear_text=text.replace("\n", " ").replace("\r", "").lower().replace("ё", "е").replace("ъ", "ь")
        for char in clear_text[:]:
                if char not in alphavit:
                    clear_text = clear_text.replace(char, "")
        clear_text = re.sub(r'\s+', ' ', clear_text)
        fout = open(name + '_clean.txt', "w")
        fout.write(clear_text)
        fout.close()
    else:
        clear_text=text.replace("\n", " ").replace("\r", "").lower().replace("ё", "е").replace("ъ", "ь").replace(" ","")
        for char in clear_text[:]:
                if char not in alphavit:
                    clear_text = clear_text.replace(char, "")
        fout = open(name + '_clean2.txt', "w")
        fout.write(clear_text)
        fout.close()   
# Частота букв
def letter_frequency(name):
    fin = open(name+'.txt', "r")
    text = fin.read()
    fin.close
    counts=Counter(text)
    for i in sorted(counts, key=counts.get, reverse = True):
        print(i,counts[i]/len(text))
# Частота биграмм
# mode указывает на то, пересекаются ли биграммы или нет
def bigramm_frequencey(name, mode):
    fin = open(name+'.txt', "r")
    text = fin.read()
    fin.close
    bigramms = {}
    if mode == True:
        bigramms = [(text[i-1],text[i]) for i in range(1, len(text))]
    else:
        if len(text)%2==1:
            text = text + " "
        bigramms = [(text[i-1],text[i]) for i in range(1, len(text), 2)]
    counts=Counter(bigramms)
    for i in sorted(counts):
        print(i,counts[i]/len(bigramms))
# Энтропия и излишек языка для монограмм
# mode указывает на наличие пробелов 
def entrophy_for_letters(name, mode):
    fin = open(name+'.txt', "r")
    text = fin.read()
    fin.close
    counts=Counter(text)
    entropy = 0
    for i in counts.values():
        entropy += - (i/len(text)) * math.log2(i/len(text))
    if mode == True:
        print("Entropy H1 with spaces: "+ str(entropy))
        print("Surplus H1 with spaces: "+ str(1-entropy/math.log2(32)))
    else:
        print("Entropy H1 without spaces: "+ str(entropy))
        print("Surplus H1 without spaces: "+ str(1-entropy/math.log2(31)))
# Энтропия и излишек языка для биграмм
# mode1 указывает на наличие пробелов 
# mode2 указывает на то, пересекаются ли биграммы или нет
def entrophy_for_bigramms(name, mode1, mode2):
    fin = open(name+'.txt', "r")
    text = fin.read()
    fin.close
    bigramms = {}
    if mode2 == True:
        bigramms = [(text[i-1],text[i]) for i in range(1, len(text))]
    else:
        if len(text)%2==1:
            text = text + " "
        bigramms = [(text[i-1],text[i]) for i in range(1, len(text), 2)]
    counts=Counter(bigramms)
    entropy = 0
    for i in counts.values():
        entropy += - (i/len(bigramms)) * math.log2(i/len(bigramms))
    entropy = entropy/2
    if mode1 == True and mode2 == True:
        print("Entropy H2 with spaces with intersection: "+ str(entropy))
        print("Surplus H2 with spaces with intersection: "+ str(1-entropy/math.log2(32)))
    elif mode1 == True and mode2 == False:
        print("Entropy H2 with spaces without intersection: "+ str(entropy))
        print("Surplus H2 with spaces without intersection: "+ str(1-entropy/math.log2(32)))
    elif mode1 == False and mode2 == True:
        print("Entropy H2 without spaces with intersection: "+ str(entropy))
        print("Surplus H2 without spaces with intersection: "+ str(1-entropy/math.log2(31)))
    elif mode1 == False and mode2 == False:
        print("Entropy H2 without spaces without intersection: "+ str(entropy))
        print("Surplus H2 without spaces without intersection: "+ str(1-entropy/math.log2(31)))
# Текст без пробелов
print("Text with spaces")
# clear_file('bulgakov1',True)
# print("Frequencey for letters:\n")
# letter_frequency('bulgakov1_clean')
# print("\nFrequencey for bigramms with intersection:\n")
# bigramm_frequencey('bulgakov1_clean', True)
# print("\nFrequencey for bigramms without intersection:\n")
bigramm_frequencey('bulgakov1_clean', False)
# print("\n")
# entrophy_for_letters('bulgakov1_clean',True)
# print("\n")
# entrophy_for_bigramms('bulgakov1_clean', True, True)
# print("\n")
# entrophy_for_bigramms('bulgakov1_clean', True, False)
# Текст с пробелами
print("Text without spaces")
# clear_file('bulgakov1',False)
# print("Frequencey for letters:\n")
# letter_frequency('bulgakov1_clean2')
# print("\nFrequencey for bigramms with intersection:\n")
# bigramm_frequencey('bulgakov1_clean2', True)
# print("\nFrequencey for bigramms without intersection:\n")
# bigramm_frequencey('bulgakov1_clean2', False)
# print("\n")
# entrophy_for_letters('bulgakov1_clean2',False)
# print("\n")
# entrophy_for_bigramms('bulgakov1_clean2', False, True)
# print("\n")
# entrophy_for_bigramms('bulgakov1_clean2', False, False)