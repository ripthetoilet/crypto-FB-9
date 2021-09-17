# This is the 1st lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92

from collections import Counter

# Cleaning example text to match the criteria before doing the task
def clean_text(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    #uniqueChars = ''.join(set(text))

    chars = '.71()-«5d?[“!93286”…—4;»0:],'
    for ch in chars:
        text = text.replace(ch, '')

    text = ' '.join([word.strip('\n') for word in text.split()])
    #print(text[:1000])

    with open('exmpl_spaces.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    text = ''.join([word.strip('\n') for word in text.split()])
    # print(text[:1000])

    with open('exmpl_nospaces.txt', 'w', encoding='utf-8') as file:
        file.write(text)

# counting monograms
def count_mono(txt, alphabet):
    # dictionary for output
    output = {}

    # change later
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    for a in alphabet:
        results = text.count(a)
        output.update({a: results})

    return output


def count_bi(txt, alphabet):
    # change later
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    res = Counter(text[idx: idx + 2] for idx in range(len(text) - 1))

    return dict(res)


clean_text('exmpl_unformatted.txt')

alphabet_clean = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet_with_spaces = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я', ' ']

# test and debug
print(count_mono('exmpl.txt', alphabet_clean))
print(count_mono('exmpl.txt', alphabet_with_spaces))
print(count_bi('exmpl.txt', alphabet_with_spaces))
