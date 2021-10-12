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



