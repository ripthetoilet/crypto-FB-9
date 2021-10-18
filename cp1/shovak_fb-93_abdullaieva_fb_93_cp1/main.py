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

def func(text, numb):
    for i in alphabet:
        letter = text.count(i)
        fr = letter / numb
        if letter == 0:
            P = 0
        else:
            P = -math.log2(fr)
        H = fr * P
        save.append(H)
        save1.append(i)
        save2.append("%.4f" % fr) # or H
    a = np.column_stack([save1,save2])
    b = sorted(a, key = lambda  x: x[1])
    c = "\n".join(map(str,b))
    print(c)


def bigram(a, alp, numb):
    line = [one[k:k + 2] for k in range(0, len(one), 2)]
    for i in alp:
        r = [alp[a] + i]
        bigram1 = line.count(r[0])
        fr = bigram1 / numb
        if bigram1 == 0:
            P = 0
        else:
            P = -math.log2(fr)
        H = fr * P
        save1.append("%.3f" % fr) # or H
        save2.append(H)
    print(alp[a], "  ".join(map(str, save1)))
    save1.clear()

def bigram2(a, alp, numb):
    line = [one[k:k+2] for k in range(len(one))]
    for i in alp:
        r = [alp[a] + i]
        bigram1 = line.count(r[0])
        fr = bigram1 / numb
        if bigram1 == 0:
            P = 0
        else:
            P = -math.log2(fr)
        H = fr * P
        save1.append("%.3f" % fr) # or H
        save2.append(H)
    print(alp[a], "  ".join(map(str, save1)))
    save1.clear()

if ans == "1":
    # with spaces
    number = len(one)
    func(one,number)
    x = sum(save)
    print("H1: ", x)
    R = 1 - x / math.log2(32)
    print("R for H1 with spaces: ", R)
    # without spaces
    print("\n")
    save.clear()
    save1.clear()
    save2.clear()
    two = one.replace(" ", "")
    number1 = len(two)
    func(two, number1)
    x = sum(save)
    print("H1: ", x)
    R = 1 - x / math.log2(32)
    print("R for H1 without spaces: ", R)
elif ans == "2":
    # не перетинаються
    # with spaces
    number = len(one)/2
    print("   ", "      ".join(alphabet))
    for item in arr:
        bigram(item, alphabet, number)
    x = sum(save2) / 2
    print("H2 with spaces: ", x)
    R = 1 - x / math.log2(32)
    print("R for H2 with spaces: ", R)
    save2.clear()
    print ("\n")
    # without spaces
    one = one.replace(" ", "")
    number1 = len(one)/2
    print("   ", "      ".join(alphabet1))
    for item in arr1:
        bigram(item, alphabet1, number1)
    x = sum(save2) / 2
    print("H2 without spaces: ", x)
    R = 1 - x / math.log2(32)
    print("R for H2 without spaces: ", R)
elif ans == "3":
    # перетинаються
    # with spaces
    number = len(one)-1
    print("   ", "      ".join(alphabet))
    for item in arr:
        bigram2(item, alphabet, number)
    x = sum(save2) / 2
    print("H2 with spaces: ", x)
    R = 1 - x/math.log2(32)
    print("R for H2 with spaces: ", R)
    save2.clear()
    print("\n")
    # without spaces
    one = one.replace(" ", "")
    number1 = len(one)-1
    print("   ", "      ".join(alphabet1))
    for item in arr1:
        bigram2(item, alphabet1, number1)
    x = sum(save2) / 2
    print("H2 without spaces: ", x)
    R = 1 - x / math.log2(32)
    print("R for H2 without spaces: ", R)
else:
    print("Wrong input")
