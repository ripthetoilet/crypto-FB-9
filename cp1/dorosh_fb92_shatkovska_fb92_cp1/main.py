# This is the 1st lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92

# Cleaning example text to match the criteria before doing the task
def cleanText(txt):
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

cleanText('exmpl_unformatted.txt')
