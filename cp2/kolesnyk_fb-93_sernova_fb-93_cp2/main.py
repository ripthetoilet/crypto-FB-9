import re
def filter(filename):
    file = open(filename, 'r', encoding='utf-8')
    text = file.read()
    text = re.sub(r'[^А-Яа-я]', '', text)
    text = text.lower()
    return text

def encode(txt,key,lett):
    j = 0
    i = 0
    outtext = ""
    alphabet_len = (len(lett))
    while i < len(txt):
        if j == len(key):
            j = 0
        res = (lett.index(txt[i]) + lett.index(key[j])) % alphabet_len
        outtext += lett[res]
        i += 1
        j += 1
    return outtext

def Affinity_Index(txt,lett):
    entry_quantity = [0]*len(lett)
    for i in range(0, len(lett)):
        entry_quantity[i] = txt.count(lett[i])      # количество вхождений каждой буквы
        entry_quantity[i] = entry_quantity[i]*(entry_quantity[i]-1)   # ищем уже часть формулы N*(N-1)
    indx=sum(entry_quantity)
    indx*=1/(len(txt)*(len(txt)-1))
    print(indx)
    return indx


blin=filter("blin.txt")
alphabet = "абвгдежзийклмнопрстуфхцчшщыьъэюя"
keys = ["ян", "туз", "шифр", "пивас", "приветдруг", "криптология", "лабораторная", "открытыйтекст", "суммаэлементов",
        "структураданних", "написатьрецензию", "настоящийвиновник", "шифрованиевиженера", "количествовхождений", "языкпрограммирования"]

file = open("plaintext.txt", 'w', encoding='utf-8')
index = Affinity_Index(blin, alphabet)
file.write("Affinity Index is " + str(index))
file.write("\n Plaintext:" + blin)
for key in keys:
    encodedtext = encode(blin, key, alphabet)
    index = Affinity_Index(encodedtext, alphabet)
    file = open("encoded"+str(len(key))+".txt", 'w', encoding='utf-8')
    file.write("Affinity Index is " + str(index))
    file.write("\nKey is " + str(key) + ", Encodedtext:\n")
    file.write(encodedtext)


# encoded = encode("приветмойдруг", "абв", alphabet)
# AffinIndex=Affinity_Index(encoded, alphabet)




# key2 = "ян"
# key3 = "туз"
# key4 = "шифр"
# key5 = "пивас"
# key10 = "приветдруг"
# key11 = "криптология"
# key12 = "лабораторная"
# key13 = "открытыйтекст"
# key14 = "суммаэлементов" #double m
# key15 = "структураданних" #double n
# key16 = "написатьрецензию"
# key17 = "настоящийвиновник"
# key18 = "шифрованиевиженера"
# key19 = "количествовхождений"
# key20 = "языкпрограммирования" #double m
