# # This is the 2nd lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92

# getting the alphabet
def get_dict():
    a = ord('а')
    alphabet = ["_"] + [chr(i) for i in range(a,a+32)]

    return alphabet


# Cleaning example text to match the criteria before doing the task
def clean_text(txt):
    chars = '.71()-«5d?[“!93286”…—4;»0:],na'

    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    for ch in chars:
        text = text.replace(ch, '')

    text = ''.join([word.strip('\n') for word in text.split('_')])

    with open('exmpl_prepared.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def encode(text, key):

    print(1)


def decode():
    print(1)


get_dict()

in_text = "большойфлопченко"
in_key = "кот"

encode(in_text, in_key)
