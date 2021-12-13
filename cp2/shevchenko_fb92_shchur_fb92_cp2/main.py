from collections import Counter
import re
from operator import itemgetter
import pandas as pd


def Read_text(filename):
    with open(filename, 'r', encoding = 'utf-8') as fin:
        return fin.read()


def Write_text(filename, text):
    with open(filename, 'w', encoding = 'utf-8') as fout:
        fout.write(text)


def Write_table(filename, table):
    writer = pd.ExcelWriter(filename)
    sheet = 'Індекси відповідості'
    table.to_excel(writer, sheet_name = sheet, index = False)

    for col in table:
        col_width = max(table[col].astype(str).map(len).max(), len(col)) + 3
        col_index = table.columns.get_loc(col)
        writer.sheets[sheet].set_column(col_index, col_index, col_width)

    writer.save()
    print('\nТаблицю індексів відповідості збережено у файлі:' + filename + '\n')


def Clear_text(text):
    cleared_text = text.replace('\n', ' ').replace('\r', ' ').replace('ё', 'е').lower()
    cleared_text = re.sub('[^а-я]', '', cleared_text)
    return cleared_text


def Get_freq(text):
    return dict(Counter(text).most_common())


def Char_int(char):
    return ord(char) - 1072


def Int_char(num):
    return chr(num + 1072)


def Encrypt(text, key):
    encrypted = ''
    for i, char in enumerate(text):
        x = Char_int(char)
        y = (x + Char_int(key[i % len(key)])) % 32
        encrypted = encrypted + Int_char(y)
    return encrypted


def Decrypt(text, key):
    decrypted = ''
    for i, char in enumerate(text):
        x = Char_int(char)
        y = (x - Char_int(key[i % len(key)])) % 32
        decrypted = decrypted + Int_char(y)
    return decrypted


def Get_index(text):
    freq = Get_freq(text)
    sum = 0
    for i in freq:
        sum = sum + freq[i] * (freq[i] - 1)
    index = 1 / (len(text) * (len(text) - 1)) * sum
    return index


def Create_blocks(text, length):
    blocks = []
    for r in range(length):
        blocks.append(text[r::length])
    return blocks


def Find_length(text):
    table_task3 = pd.DataFrame(columns = ['Довжина', 'Індекс відповідості'])
    keys_indexes = {}
    for length in range(1, 31):
        blocks = Create_blocks(text, length)
        sum = 0
        for block in blocks:
            sum = sum + Get_index(block)
        average = sum / length
        keys_indexes[length] = average

        table_task3 = table_task3.append({
            'Довжина': str(length),
            'Індекс відповідості': str(average)
        }, ignore_index = True)
    Write_table(TABLE_TASK3, table_task3)

    subs = []
    for length in keys_indexes:
        subs.append(abs(index_theoretical - keys_indexes[length]))
    return min(enumerate(subs), key = itemgetter(1))[0] + 1


def Find_value(text, length):
    x = []
    for char in ['о', 'а', 'е', 'и', 'н']:
        x.append(Char_int(char))

    blocks = Create_blocks(text, length)
    key = ''
    for block in blocks:
        freq = Get_freq(block)
        y = Char_int(max(freq, key = freq.get))
        k = (y - x[0]) % 32
        key = key + Int_char(k)
    return key


# ШЛЯХИ
# TEXT_PLAIN_TASK1 = 'plain\\kolobok.txt'
TEXT_PLAIN_TASK1 = 'plain\\tank.txt'

TEXT_ENCRYPTED_TASK3 = 'encrypted\\var3.txt'
# TEXT_ENCRYPTED_TASK3 = 'encrypted\\var1.txt'
# TEXT_ENCRYPTED_TASK4 = 'encrypted\\var6.txt'
# TEXT_ENCRYPTED_TASK3 = 'encrypted\\var7.txt'

TEXT_DECRYPTED_TASK3 = 'decrypted\\task3.txt'

TABLE_TASK2 = 'tables\\task2.xlsx'
TABLE_TASK3 = 'tables\\task3.xlsx'
# ШЛЯХИ

# ЗАВДАННЯ №1-2
print('----------------------| ЗАВДАННЯ №1-2 |-----------------------\n')

plain = Clear_text(Read_text(TEXT_PLAIN_TASK1))
print('Відкритий текст збережено у файлі: ' + TEXT_PLAIN_TASK1)

index_theoretical = Get_index(plain)
print('Теоретичний індекс відповідості: ' + str(index_theoretical) + '\n')

table_task2 = pd.DataFrame(columns = ['Довжина', 'Ключ', 'Індекс відповідості'])
keys = ['да', 'нет', 'шкаф', 'повар', 'специалист', 'абрикосовый', 'квалификация',
        'авианавигация', 'автоматический', 'агроконференция', 'безответственный',
        'автопроизводитель', 'агропромышленность', 'антропоцентричность', 'воздухонепроницаемый']
for key in keys:
    print('--------------------------------------------------------------\n')
    TEXT_ENCRYPTED_TASK1 = 'encrypted\\task1_' + str(len(key)) + '.txt'
    TEXT_DECRYPTED_TASK1 = 'decrypted\\task1_' + str(len(key)) + '.txt'

    print('Ключ: ' + key)
    print('Довжина ключа: ' + str(len(key)))

    encrypted = Encrypt(plain, key)
    print('Шифрований текст збережено у файлі: ' + TEXT_ENCRYPTED_TASK1)
    Write_text(TEXT_ENCRYPTED_TASK1, encrypted)

    decrypted = Decrypt(encrypted, key)
    print('Розшифрований текст збережено у файлі: ' + TEXT_DECRYPTED_TASK1)
    Write_text(TEXT_DECRYPTED_TASK1, decrypted)

    index = Get_index(encrypted)
    print('Індекс відповідості шифрованого тексту: ' + str(index) + '\n')

    table_task2 = table_task2.append({
        'Довжина': str(len(key)),
        'Ключ': key,
        'Індекс відповідості': str(index)
    }, ignore_index = True)

Write_table(TABLE_TASK2, table_task2)

print('----------------------| ЗАВДАННЯ №1-2 |-----------------------\n')
# ЗАВДАННЯ №1-2

# ЗАВДАННЯ №3
print('----------------------|  ЗАВДАННЯ №3  |-----------------------\n')

encrypted = Clear_text(Read_text(TEXT_ENCRYPTED_TASK3))
print('Шифрований текст збережено у файлі: ' + TEXT_ENCRYPTED_TASK3)

length = Find_length(encrypted)
print('Довжина ключа: ' + str(length))

value = Find_value(encrypted, length)
print('Значення ключа: ' + value + '\n')

value = 'экомаятникфуко'
decrypted = Decrypt(encrypted, value)
print('Розшифрований текст збережено у файлі: ' + TEXT_DECRYPTED_TASK3 + '\n')
Write_text(TEXT_DECRYPTED_TASK3, decrypted)

print('----------------------|  ЗАВДАННЯ №3  |-----------------------\n')
# ЗАВДАННЯ №3
