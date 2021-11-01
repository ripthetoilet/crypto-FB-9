import collections
import re
from collections import Counter
from tabulate import tabulate
import numpy as np
import pandas as pd

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф','х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']
keys = ['да','нет','дети','зверь','машина', 'наверно', 'затоплен', 'газировка' ,'автомобиль', 'бездействие','баскетболист', 'автобиография','выпендриваться','замаскироваться']

with open("text1.txt",'r',encoding='utf-8') as f1:
    text1=f1.read().lower().replace("ъ", "ь").replace("ё", "е")
    text1=re.sub("[^а-я]","",text1)
with open("text2.txt",'r',encoding='utf-8') as f2:
    text2=f2.read().replace("\n","")


def Cipher(text, key):
    ciphered_text = []
    index_key = [alphabet.index(i) for i in key]
    for index, char in enumerate(text):
        ciphered_text.append(alphabet[(alphabet.index(char)+index_key[index % len(key)]) % len(alphabet)])
    return "".join(ciphered_text)

def Decipher(text,key):
    deciphered_text=[]
    key_index = [alphabet.index(i) for i in key]
    for index, char in enumerate(text):
        deciphered_text.append(alphabet[(alphabet.index(char)-key_index[index % len(key)] + len(alphabet)) % len(alphabet)])
    return "".join(deciphered_text)

#індех відповідності для тексту
def index(text):
    freq= dict(Counter(text))
    res = 0
    for i in freq.values():
        res+= i * (i-1)
    return res/(len(text)*(len(text)-1))

#розбіття тексту на блоки довжини len
def Block(text, len):
    block =[]
    for i in range(len):
        block.append(text[i::len])
    return block

#індекс відповідності для тексту зашифрованим ключем 
def Index_for_keys(text, key):
    block=Block(text, len(key))
    index_for_keys =0
    for i in range(len(block)):
        index_for_keys= index_for_keys + index(block[i])
    index_for_keys=index_for_keys/len(block)
    return index_for_keys

#індекс відповідності для блоку
def Index_for_blocks(text):
    index_for_block = {}
    for i in range(2,32):
        temp = 0
        blocks = Block(text,i)
        for block in blocks:
            temp += index(block)
        index_for_block[i] = temp/i
    return index_for_block


#створення ключа за відомою довжиною
def Create_key(text, key_len):
    popular_letters =[]
    key=[]
    for i in range(key_len):
        j=0
        tmp =''
        while j < len(text)-key_len:
            tmp+= text[i+j]
            j+=key_len
        x=Counter(tmp)
        popular_letters.append(x.most_common(1)[0][0])
    for i in range(len(popular_letters)):
        key.append(alphabet[(alphabet.index(popular_letters[i])-14) % 32 ])
    print("\nТаблиця відповідностей найчастішої літери ШТ до літери ключа")
    Print_table(popular_letters,key,"Буква ключа")
    print("Ключ ","".join(key))
    return "".join(key)


def Print_table(list1, list2, columnname):
    dic=dict(list(zip(list1, list2)))
    data = pd.DataFrame.from_dict(dic, 'index',columns=[columnname])
    print(tabulate(data,headers='keys', tablefmt='grid'))

def Task1(text, filename):
    task1_dic=[]
    with open(filename, 'w', encoding='utf-8') as w1:
        for i in keys:
            w1.write("\nКлюч " + i + '\n')
            w1.write(Cipher(text,i))
            task1_dic.append(Index_for_keys(Cipher(text,i), i))
    Print_table(keys,task1_dic, "Індекс відповідності")


def Task2(text):
    for i in keys:
        print("\nКлюч " + i)
        tmp= []
        for j in Index_for_blocks(Cipher(text, i)):
            tmp.append(Index_for_blocks(Cipher(text, i))[j])
        Print_table(Index_for_blocks(Cipher(text, i)).keys(),tmp,"Індекс відповідності")

def Task3(text, filename):
    print("\n")
    Print_table(Index_for_blocks(text).keys(),Index_for_blocks(text).values(),"Індекс відповідності")
    print("Довжина ключа  з максимальним індексом відповідності ",max(Index_for_blocks(text), key=Index_for_blocks(text).get))
    key =Create_key(text2, max(Index_for_blocks(text), key=Index_for_blocks(text).get))
    with open(filename, 'w', encoding='utf-8') as w2:
        w2.write(Decipher(text2,"вшекспирбуря"))


print("Task1 +-----------------------------------")
Task1(text1,'out1.txt')
print("\nTask2 +-----------------------------------")
Task2(text1)
print("\n\nTask3 +-----------------------------------")
Task3(text2,"out2.txt")

