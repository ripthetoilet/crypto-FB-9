from collections import Counter
import csv
import math

al = {'й':0,'ц':0,'у':0,'к':0,'е':0,'н':0,'г':0,'ш':0,'щ':0,'з':0,'х':0,'ъ':0,'ф':0,'ы':0,'в':0,'а':0,'п':0,'р':0,'о':0,'л':0,'д':0,'ж':0,'э':0,'я':0,'ч':0,'с':0,'м':0,'и':0,'т':0,'ь':0,'б':0,'ю':0,' ':0}
let = al.keys()
f = open('text.txt',"r",encoding = "utf-8")
text = f.read()
text = text.lower()
text1 = "".join([i for i in text if i in al.keys()])        #ridding off nonletters
text2 = "".join([i for i in text if i in al.keys() and i != ' '])

r = lambda x: 1 - (x / math.log2(32))                       #redundency

def letters(text, al):
    for i in text:
        if (i in let):
            al[i] = al[i] + 1                               #setting ammount of letters
    for i in al.keys():
        al[i] /= len(text)                                  #converting frequency to probabilty
    h = sum(list(map(lambda x: -x * math.log2(x), al.values())))    #entropy
    print( h, "and sets redundency ", r(h) )
    return dict(sorted(al.items(), key=lambda item: item[1], reverse=True))

def bigrams(text, inters):
    bis = []
    if inters: 
        for i,j in enumerate(text):
            bi = text[i:i+2]                    #setting pairs
            if (len(bi) == 2):
                bis.append(bi)
        bisd =  Counter(bis)
        for i in bisd.keys():
            bisd[i] /= len(text) - 1                    #converting frequency to probabilty
    else:
        for i,j in enumerate(text[::2]):        #every second letter is a start of a pair
            bi = text[i:i+2]                    #setting pairs
            if (len(bi) == 2):
                bis.append(bi)
        bisd =  Counter(bis)
        for i in bisd.keys():
            bisd[i] /= len(text) / 2                    #converting frequency to probabilty
    h = sum(list(map(lambda x: -x * math.log2(x), bisd.values()))) / 2      #entropy
    print( h, "and sets redundency ", r(h))
    return dict(sorted(bisd.items(), key=lambda item: item[1], reverse=True))

print("letter entropy with spaces", end = ' ')
data = letters(text1, al)
table = open("1.txt", "w", encoding='utf-8')
writer = csv.writer(table)
for key, value in data.items():
    writer.writerow([key, value])
print("bigram entropy with spaces, with intersetcions and sets redundency",end = ' ')
data = bigrams(text1, 1)
table = open("2.txt", "w", encoding='utf-8')
writer = csv.writer(table)
for key, value in data.items():
    writer.writerow([key, value])
print("bigram entropy with spaces, without intersetcions and sets redundency",end = ' ')
data = bigrams(text1, 0)
table = open("3.txt", "w", encoding='utf-8')
writer = csv.writer(table)
for key, value in data.items():
    writer.writerow([key, value])
print("letter entropy without spaces, and sets redundency",end = ' ')
data = letters(text2, al)
table = open("4.txt", "w", encoding='utf-8')
writer = csv.writer(table)
for key, value in data.items():
    writer.writerow([key, value])
print("bigram entropy without spaces, with intersetcions and sets redundency",end = ' ')
data = bigrams(text2, 1)
table = open("5.txt", "w", encoding='utf-8')
writer = csv.writer(table)
for key, value in data.items():
    writer.writerow([key, value])
print("bigram entropy without spaces, without intersetcions and sets redundency",end = ' ')
data = bigrams(text2, 0)
table = open("6.txt", "w", encoding='utf-8')
writer = csv.writer(table)
for key, value in data.items():
    writer.writerow([key, value])