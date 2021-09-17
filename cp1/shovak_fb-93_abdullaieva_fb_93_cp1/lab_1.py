import math
import re
import numpy as np
file = open("/Users/esmira.23/Desktop/КПИ/3курс/Крипта/1.txt", "r")
data = file.read().replace("ъ","ь")
one = re.sub(r"[^а-я]+", " ", data.lower()).replace("ъ","ь").replace("ё","е")

# m=32 - кількість букв алфавіту
alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я',' ']
save = []
save1 = []
save2 = []
save3 = []
save4 = []

print("1. First task\n2. Second task\n3. Third task\n4. Fourth task\n")
ans = input()

def func():
    for i in alphabet:
        letter = one.count(i)
        if letter == 0:
            y = 0
        else:
            y = -math.log2(letter/number)
        H1 = letter/number * y
        save.append(H1)
        save1.append(i)
        save4.append("%.4f" % H1)
    a = np.column_stack([save1,save4])
    b = sorted(a, key = lambda  x: x[1])
    c = "\n".join(map(str,b))
    print(c)
    print("H1: ", (sum(save)))

def bigram(a):
    for i in alphabet:
        r = [alphabet[a] + i]
        for j in r:
            letter = one.count(j)
            if letter == 0:
                y1 = 0
            else:
                y1 = -math.log2(letter/number)
            H2 = letter/number * y1
            save1.append("%.3f" % H2)
            save3.append(H2)
            save2.append(i)
    print(alphabet[a], "  ".join(map(str, save1)))
    save1.clear()

if ans == "1":
    number = len(one)
    func()
elif ans == "2":
    one = one.replace(" ", "")
    number = len(one)
    func()
elif ans == "3":
    number = len(one)
    arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24,26,27,28,29,30,31]
    print("   ", "      ".join(alphabet))
    for item in arr:
        bigram(item)
    print("H2: ", (sum(save3)))
elif ans == "4":
    one = one.replace(" ", "")
    number = len(one)
    arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24,26,27,28,29,30,31]
    print("   ", "      ".join(alphabet))
    for item in arr:
        bigram(item)
    print("H2: ", (sum(save3)))

else:
    print("Wrong input")