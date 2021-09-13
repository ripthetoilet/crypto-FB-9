from collections import Counter
import math

al = {'й':0,'ц':0,'у':0,'к':0,'е':0,'н':0,'г':0,'ш':0,'щ':0,'з':0,'х':0,'ъ':0,'ф':0,'ы':0,'в':0,'а':0,'п':0,'р':0,'о':0,'л':0,'д':0,'ж':0,'э':0,'я':0,'ч':0,'с':0,'м':0,'и':0,'т':0,'ь':0,'б':0,'ю':0,' ':10}
let = al.keys()
f = open('text.txt',"r",encoding = "utf-8")
text = f.read()
text = text.lower()
text1 = "".join([i for i in text if i in al.keys()])        #ridding off nonletters
del al[" "]                                                 #deleting spaces
text2 = "".join([i for i in text if i in al.keys()])

r = lambda x: 1 - (x / math.log2(32))                       #redundency

def letters(text, al):
    for i in text:
        if (i in let):
            al[i] = al[i] + 1                               #setting ammount of letters
    for i in al.keys():
        al[i] /= len(text)                                  #converting frequency to probabilty
    h = sum(list(map(lambda x: -x * math.log2(x), al.values())))    #entropy
    return h, r(h) 

def bigrams(text, inters):
    bis = []
    if inters: 
        for i,j in enumerate(text):
            bi = text[i:i+2]                    #setting pairs
            if (len(bi) == 2):
                bis.append(bi)
    else:
        for i,j in enumerate(text[::2]):        #every second letter is a start of a pair
            bi = text[i:i+2]                    #setting pairs
            if (len(bi) == 2):
                bis.append(bi)
    bisd =  Counter(bis)
    for i in bisd.keys():
        bisd[i] /= len(text)                    #converting frequency to probabilty
    h = sum(list(map(lambda x: -x * math.log2(x), bisd.values()))) / 2      #entropy
    return h, r(h)

print("letter entropy with spaces, and sets redundency",letters(text1, al))
print("bigram entropy with spaces, with intersetcions and sets redundency",bigrams(text1, 1))
print("bigram entropy with spaces, without intersetcions and sets redundency",bigrams(text1, 0))
print("letter entropy without spaces, and sets redundency",letters(text2, al))
print("bigram entropy without spaces, with intersetcions and sets redundency",bigrams(text2, 1))
print("bigram entropy without spaces, without intersetcions and sets redundency",bigrams(text2, 0))