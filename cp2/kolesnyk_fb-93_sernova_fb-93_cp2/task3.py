import re
def filter(filename):
    file = open(filename, 'r', encoding='utf-8')
    text = file.read()
    
    return text


def Affinity_Index(txt,lett):
    entry_quantity = [0]*len(lett)
    for i in range(0, len(lett)):
        entry_quantity[i] = txt.count(lett[i])      # количество вхождений каждой буквы
        entry_quantity[i] = entry_quantity[i]*(entry_quantity[i]-1)   # ищем уже часть формулы N*(N-1)
    indx=sum(entry_quantity)
    indx*=1/(len(txt)*(len(txt)-1))

    return indx

#перший варіант декодування шифру Віженера

def block_div(txt, r): #крок 1: поділ тексту на блоки (>2)
    block_arr = []
    for position in range(0,r):
        block_arr.append(txt[position::r])
    return block_arr

#крок 2: індекс для блоків на основі функції з завдань 1-2
def Affinity_Index_Blocks(block_arr, lett):
    entry_quantity = [0]*len(lett)
    for i in range(0, len(block_arr)):
       entry_quantity[i] = Affinity_Index(block_arr[i], lett)
    indx=sum(entry_quantity)
    indx=indx/len(block_arr)
    return indx

#шукаємо ключ
def find_key(block_arr, lett, letter):
    key = []
    for i in range(0, len(block_arr)): #для каждого блока
        freq = []
        for a in range(0, len(lett)):
            frequency = block_arr[i].count(lett[a])
            freq.append(frequency)

      #  print(frequency)
        max_freq = freq.index(max(freq))
       
        max_key = (max_freq - lett.find(letter)) % len(lett) # k = y - x (mod m)
        key.append(lett[max_key])
        
    full_key = ''.join(key)
    print(full_key)
    return full_key
    #print(full_key)
       

def decode(txt, key, lett):
    encoded = []
    key_seq = []
    for i in key:
        k = lett.find(i)
        key_seq.append(k)
    for j in range(0, len(txt)):
        y = lett.find(txt[j])
        k = key_seq[j % len(key_seq)]
        x = (y - k) % len(lett)
        encoded.append(lett[x])
    full_encoded = ''.join(encoded)
    print(full_encoded)
    return full_encoded


cipher = filter("var7.txt")
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


file = open("lab2_res.txt", 'w', encoding='utf-8')

index = Affinity_Index(cipher, alphabet)

for r in range(2, len(alphabet)):

    block_array = block_div(cipher, r)
    index = Affinity_Index_Blocks(block_array, alphabet)
    print('for key length = ' + str(r) + '   index = ' + str(index))
    print('')
print('length of the key is 15 so...' )

block_arr = block_div(cipher, 15)

key = find_key(block_arr, alphabet, 'о')
key = 'арудазовархимаг' #поиск в гугле сказал что речь о книге "Архимаг" Александра Рудазова
encodedtext = decode(cipher, key, alphabet)

file = open("encoded_task3.txt", 'w', encoding='utf-8')

file.write("\nKey is " + str(key) + ", Encodedtext:\n")
file.write(encodedtext)

