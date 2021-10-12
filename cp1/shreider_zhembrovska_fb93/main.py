alph = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ",
        "ъ","ы","ь","э","ю","я"]

#text editing
text = []
with open('text.txt', 'r', encoding = 'utf-8') as file:
    space = False
    for line in file:
        line = line.lower()
        length = len(line)
        for i in range(length):
            if line[i] in alph:
                text.append(line[i])
                space = False
            else:
                if space == True:
                    continue
                else:
                    text.append(" ")
                    space = True

