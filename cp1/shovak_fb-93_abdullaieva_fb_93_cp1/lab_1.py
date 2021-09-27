import math
import re
import numpy as np
file = open("1.txt", "r")
data = file.read().replace("ъ","ь")
one = re.sub(r"[^а-я]+", " ", data.lower()).replace("ъ","ь").replace("ё","е")

# m=32 - кількість букв алфавіту
alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я',' ']
alphabet1 = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24,26,27,28,29,30,31]
arr1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24,26,27,28,29,30]
save = []
save1 = []
save2 = []

print("1. Leters with and without spaces\n2. Bigram without crossing\n3. Bigram with crossing")
ans = input()

def func(numb):
    for i in alphabet:
        letter = one.count(i)
        if letter == 0:
            P = 0
        else:
            P = -math.log2(letter/numb)
        H = letter/numb * P
        save.append(H)
        save1.append(i)
        save2.append("%.4f" % H)
    a = np.column_stack([save1,save2])
    b = sorted(a, key = lambda  x: x[1])
    c = "\n".join(map(str,b))
    print(c)
    print("H1: ", (sum(save)))

def bigram(a, alp, numb):
    line = [one[k:k + 2] for k in range(0, len(one), 2)]
    for i in alp:
        r = [alp[a] + i]
        bigram1 = line.count(r[0])
        if bigram1 == 0:
            P = 0
        else:
            P = -math.log2(bigram1/numb)
        H = bigram1/numb * P
        save1.append("%.3f" % H)
        save2.append(H)
    print(alp[a], "  ".join(map(str, save1)))
    save1.clear()

def bigram2(a, alp, numb):
    line = [one[k:k+2] for k in range(len(one))]
    for i in alp:
        r = [alp[a] + i]
        bigram1 = line.count(r[0])
        if bigram1 == 0:
            P = 0
        else:
           P = -math.log2(bigram1/numb)
        H = bigram1/numb * P
        save1.append("%.3f" % H)
        save2.append(H)
    print(alp[a], "  ".join(map(str, save1)))
    save1.clear()

if ans == "1":
    # with spaces
    number = len(one)
    func(number)
    # without spaces
    print("\n")
    save.clear()
    one = one.replace(" ", "")
    number1 = len(one)
    func(number1)
elif ans == "2":
    # не перетинаються
    # with spaces
    number = len(one)/2
    print("   ", "      ".join(alphabet))
    for item in arr:
        bigram(item, alphabet, number)
    print("H2 with spaces: ", (sum(save2)/2))
    save2.clear()
    print ("\n")
    # without spaces
    one = one.replace(" ", "")
    number1 = len(one)/2
    print("   ", "      ".join(alphabet))
    for item in arr1:
        bigram(item, alphabet, number1)
    print("H2 without spaces: ", (sum(save2)/2))
elif ans == "3":
    # перетинаються
    # with spaces
    number = len(one)-1
    print("   ", "      ".join(alphabet))
    for item in arr:
        bigram2(item, alphabet, number)
    print("H2: ", (sum(save2)/2))
    save2.clear()
    print("\n")
    # without spaces
    one = one.replace(" ", "")
    number1 = len(one)-1
    print("   ", "      ".join(alphabet1))
    for item in arr1:
        bigram2(item, alphabet1, number1)
    print("H2: ", (sum(save2)/2))
else:
    print("Wrong input")
