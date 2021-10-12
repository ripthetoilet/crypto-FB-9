import math

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


def letters_entropy(text, freq):
    length = len(text)
    for i in range(34):
        count = 0
        for j in range(length):
            if text[j] == alph[i]:
                count += 1
        if count/length == 0: #for text without spaces
            continue
        freq.update({alph[i]: count/length})
    return -1 * sum(freq[k] * math.log(freq[k], 2) for k in freq)

