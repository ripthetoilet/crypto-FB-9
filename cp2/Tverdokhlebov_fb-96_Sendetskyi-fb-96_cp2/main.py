import collections
import re
from collections import Counter
from tabulate import tabulate
import numpy as np
import pandas as pd

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф','х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я','ъ']
keys = ['да','нет','дети','зверь','машина', 'наверно', 'затоплен', 'газировка' ,'автомобиль', 'бездействие','баскетболист', 'автобиография','выпендриваться','замаскироваться']

with open("text1.txt",'r',encoding='utf-8') as f1:
    text1=f1.read().lower().replace("ъ", "ь").replace("ё", "е")
    text1=re.sub("[^а-я]","",text1)
with open("text2.txt",'r',encoding='utf-8') as f2:
    text2=f2.read()


def Cipher(text, key):
    ciphered_text = []
    index_key = [alphabet.index(i) for i in key]
    for index, char in enumerate(text):
        ciphered_text.append(alphabet[(alphabet.index(char)+index_key[index % len(key)]) % len(alphabet)])
    return "".join(ciphered_text)

def Decipher(text,key):
    deciphered_text=[]
    key_index = [alphabet.index(i) for i in key]
    for i, char in enumerate(text):
        deciphered_text.append(alphabet[alphabet.index(char)-key_index[i%len(key)]+len(alphabet)%len(alphabet)])
    return "".join(deciphered_text)


def index(text):
    freq= dict(Counter(text))
    res = 0
    for i in freq.values():
        res+= i * (i-1)
    return res/(len(text)*(len(text)-1))

def Block(text, len):
    block =[]
    for i in range(len):
        block.append(text[i::len])
    return block

def Index_for_keys(text, key):
    block=Block(text, len(key))
    index_for_keys =0
    for i in range(len(block)):
        index_for_keys= index_for_keys + index(block[i])
    index_for_keys=index_for_keys/len(block)
    return index_for_keys


def Index_for_blocks(text):
    index_for_block = {}
    for i in range(2,32):
        temp = 0
        blocks = Block(text,i)
        for block in blocks:
            temp += index(block)
        index_for_block[i] = temp/i
    return index_for_block

def Create_key(text, len):
    blocks=Block(text, len)
    created_key= []
    for i in blocks:
        res = Counter(i).most_common(1)[0]
        if res[0] not in created_key:
            created_key.append(res)
    return created_key

def Task1(text, filename):
    task1_dic=[]
    with open(filename, 'w', encoding='utf-8') as w1:
        for i in keys:
            w1.write("\nКлюч " + i + '\n')
            w1.write(Cipher(text1,i))
            task1_dic.append(Index_for_keys(Cipher(text1,i), i))
    task1=dict(list(zip(keys,task1_dic)))
    data=pd.DataFrame.from_dict(task1,'index', columns=["Індекс відповідності"])
    print(tabulate(data, headers='keys', tablefmt='grid'))

def Task2(text):
    for i in keys:
        task2=[]
        print("\nКлюч " + i)
        tmp= []
        for j in Index_for_blocks(Cipher(text, i)):
            tmp.append(Index_for_blocks(Cipher(text, i))[j])
        task2=dict(list(zip(Index_for_blocks(Cipher(text, i)).keys(),tmp)))
        data=pd.DataFrame.from_dict(task2,'index', columns=["Індекс відповідності"])
        print(tabulate(data, headers='keys', tablefmt='grid'))


print("Task1 +-----------------------------------\n")
Task1(text1,'out1.txt')

Task2(text1)
