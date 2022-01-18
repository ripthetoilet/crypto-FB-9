from collections import Counter

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
            'ч', 'ш', 'щ', 'ы', 'ь', 'ъ', 'э', 'ю', 'я']

keys = ["кр", "ара", "нога", "книга", "подсчитать"]


def TextFormater():
    i = 0
    text = ""
    with open("text.txt", encoding='utf-8') as f:
        text = f.read().lower().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('ё', 'е').replace('ъ',
                                                                                                                   'ь')
        NewText = ""
        length = len(text)
        while i < length - 1:
            if text[i] in alphabet:
                NewText += text[i]
            i += 1
    return NewText


def KeysFormater():
    NewKeys = []
    k = ""
    for i in keys:
        while len(i) < len(TextFormater()):
            i += i
        for j in range(len(TextFormater())):
            k += i[j]
        NewKeys.append(k)
        k = ""
        i = ""
    return NewKeys


def EncrypteText(text, key):
    k = KeysFormater()
    key = k[key]
    EncryptedText = ""
    for i in range(0, len(TextFormater())):
        EncryptedText += alphabet[(alphabet.index(text[i]) + alphabet.index(key[i])) % len(alphabet)]
    return EncryptedText


def IndexOfFrequency(Text):
    counter = Counter(Text)
    Index = 0
    for i in range(0, 31):
        Index += (counter[alphabet[i]] * (counter[alphabet[i]] - 1)) / (len(Text) * (len(Text) - 1))
    return Index


# KeyIndex = int(input("Select key:\n0 - r=2\n1 - r=3\n2 - r=4\n3 - r=5\n4 - r=10\n"))

def LengthOfKey(text):
    groups = []
    index = 0
    for i in range(2, len(alphabet)):
        for j in range(0, i):
            groups.append(text[j::i])
            index += IndexOfFrequency(groups[-1])
        index = index / i
        print("Length = " + str(i) + ": " + str(round(index, 8)))
        index = 0


def DecrypteText(enctext, key):
    k = KeysFormater()
    key = k[key]
    DecryptedText = ""
    for i in range(0, len(enctext)):
        DecryptedText += alphabet[(alphabet.index(enctext[i]) - alphabet.index(key[i])) % len(alphabet)]
    return DecryptedText


# print("Index for a open Text: " + str(IndexOfFrequency(TextFormater())))
# for i in range(len(keys)):
# print("Index for a " + str(i + 1) + " encrypted Text: " + str(IndexOfFrequency(EncrypteText(TextFormater(), i))) + " key: " + keys[i] + " length of key = " + str(len(keys[i])))

with open("var11.txt", encoding='utf-8') as f:
    text = f.read().replace('\n', '')
    # print(text)

# LengthOfKey(text)
# length = 17

groups = []
for i in range(17):
    groups.append(text[i::17])

array = []
frequency = []
MaxFrequencyLetters = []
for i in range(len(groups)):
    for char in groups[i]:
        array.append(char)
    for ch in array:
        frequency.append(array.count(ch) / len(array))
    max_frequency = max(frequency)
    MaxFrequencyLetters.append(array[frequency.index(max_frequency)])
    array = []
    frequency = []

key = ""
for ch in MaxFrequencyLetters:
    key += (alphabet[(alphabet.index(ch) - 14) % len(alphabet)])
# print(key)
# венецианскийкупец (Шекспир)

key = "венецианскийкупец"


def KeysFormatered(text):
    key = "венецианскийкупец"
    while len(key) < len(text):
        key += key
    return key[0:len(text)]


def DecryptedText(enctext, key):
    key = KeysFormatered(enctext)
    DecryptedText = ""
    for i in range(0, len(enctext)):
        DecryptedText += alphabet[(alphabet.index(enctext[i]) - alphabet.index(key[i])) % len(alphabet)]
    return DecryptedText

print(DecryptedText(text, key))
