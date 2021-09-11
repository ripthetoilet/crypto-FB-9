from collections import Counter
import math

al = {'й':0,'ц':0,'у':0,'к':0,'е':0,'н':0,'г':0,'ш':0,'щ':0,'з':0,'х':0,'ъ':0,'ф':0,'ы':0,'в':0,'а':0,'п':0,'р':0,'о':0,'л':0,'д':0,'ж':0,'э':0,'я':0,'ч':0,'с':0,'м':0,'и':0,'т':0,'ь':0,'б':0,'ю':0,' ':10}
let = al.keys()
f = open('text.txt',"r",encoding = "utf-8")
text = f.read()
text = text.lower()
text1 = "".join([i for i in text if i in al.keys()])     #ridding off nonletters
del al[" "]
text2 = "".join([i for i in text if i in al.keys()])

r = lambda x: 1 - (x / math.log2(32))

def letters(text, al):
    for i in text:
        if (i in let):
            al[i] = al[i] + 1                               #setting ammount of letters
    for i in al.keys():
        al[i] /= len(text)
    h = sum(list(map(lambda x: -x * math.log2(x), al.values())))    #entropy
    print(h)
    print(r(h))         #redundency 

def bigrams(text):
    bis = []
    for i,j in enumerate(text):
        bi = text[i:i+2]                    #setting pairs
        if (len(bi) == 2):
            bis.append(bi)
    bisd =  Counter(bis)
    for i in bisd.keys():
        bisd[i] /= len(text)
    h = sum(list(map(lambda x: -x * math.log2(x), bisd.values()))) / 2      #entropy
    print(h)
    print(r(h))         #redundency

letters(text1, al)
bigrams(text1)
letters(text2, al)
bigrams(text2)