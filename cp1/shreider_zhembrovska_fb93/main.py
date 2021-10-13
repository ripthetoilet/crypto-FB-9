import math
from collections import Counter


alph = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ",
        "ъ","ы","ь","э","ю","я", " "]

#text editing
text_spaces = []
text_nospaces = []

with open('text.txt', 'r', encoding = 'utf-8') as file:
    file = file.read()
    file = file.lower()
    length = len(file)

    space = False
    for i in range(length):
        if file[i] in alph:
            if file[i] == " ":
                if space == True:
                    continue
                else:
                    text_spaces.append(" ")
                    space = True
            else:
                text_spaces.append(file[i])
                text_nospaces.append(file[i])
                space = False
        else:
            if space == False:
                text_spaces.append(" ")
                space = True


def letters_entropy(text):
    length = len(text)
    freq = {}
    for i in range(34):
        count = 0
        for j in range(length):
            if text[j] == alph[i]:
                count += 1
        if count/length == 0: #for text without spaces
            continue
        freq.update({alph[i]: count/length})
    return -1 * sum(freq[k] * math.log(freq[k], 2) for k in freq)


def bigrams_entropy(text, intersection):
    length = len(text)
    if length % 2 == 1 and intersection == 0:
        length -= 1

    bigrams = []
    for i in range(0, length, 2-intersection):
        bigrams.append(text[i]+text[i+1])
    count = len(bigrams)

    freq = Counter(bigrams)
    for i in freq:
        freq[i] /= count
    return sum(freq[k] * math.log(freq[k], 2) for k in freq) / (-2)

