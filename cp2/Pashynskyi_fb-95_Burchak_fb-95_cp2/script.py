import os
#\/\/\/\/\/\/\/\/\/\|1 - Шифрування власного тексту ключами різної довжини|/\/\/\/\/\/\/\/\/\/#


chars = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
         'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

keys = ['со', 'мба', 'дива', 'нстол', 'дмизеволдизгонаролми']


def Char_filter(text):      # функція фільтрації тексту з лаби 1
    A = []
    text = text.lower()
    for ch in text:
        if ch in chars:
            A.append(ch)
    text = ''.join(A)
    text = text.replace('ё', 'е')   # заміна 'ё' на 'е'
    return text


f = open(".\\going_to_the_river.txt", "r", encoding='UTF-8')
text = f.read()
f.close()

filtered_text = Char_filter(text)
f = open(".\\Filtered txt\\filtered.txt", "w")
f.write(filtered_text)
f.close()


def encode(text, key):      # функція шифрування
    A = []
    for i, ch in enumerate(text):
        # алфавітний індекс символу
        text_i = chars.index(ch)
        # багаторазовий прохід по символам ключа
        key_i = chars.index(key[(i % len(key))])

        # зашифрований символ за формулою
        e_char = chars[(text_i + key_i) % len(chars)]

        # додаємо зашифровані символи в масив
        A.append(e_char)

    return ''.join(A)


def index(text):
    index = 0
    for i in range(0, len(chars)):
        N = text.count(chars[i])
        index += N*(N-1)
    index /= (len(text) * (len(text) - 1))
    return index


if os.path.exists(".\\task1-2.txt"):
    os.remove(".\\task1-2.txt")

f = open(".\\task1-2.txt", "a")
s = "Normal text index: " + str(index(filtered_text)) + "\n\n"
f.write(s)

for key in keys:
    e_text = encode(filtered_text, key)
    s = "Text, encrypted with key length " + \
        str(len(key)) + " index = " + \
        str(index(e_text)) + "\n" + e_text + "\n\n"
    f.write(s)
f.close()
