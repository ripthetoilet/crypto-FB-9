# This is the 1st lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92

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

    with open('exmpl.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def count_mono(txt, alphabet):
    # dictionary for output
    output_clean = {}

    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    for a in alphabet:
        results = text.count(a)
        output_clean.update({a: results})

    return output_clean


clean_text('exmpl_unformatted.txt')
alphabet_clean = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
print(count_mono('exmpl_unformatted.txt', alphabet_clean))

#print(resilt)