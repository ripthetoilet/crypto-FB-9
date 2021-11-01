from collections import Counter
import operator
from itertools import islice

def clean_text(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # uniqueChars = ''.join(set(text))

    # -----------------------------------------------------
    chars = '.71()-«5d?[“!93286”…—4;»0:],naoti*IVXvxse–'
    # -----------------------------------------------------
    for ch in chars:
        text = text.replace(ch, '')
        
    text = '_'.join([word.strip('\n') for word in text.split()])
    # print(text[:1000])

    text = ''.join([word.strip('\n') for word in text.split('_')])
    # print(text[:1000])

    with open('exmpl_clean.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def open_file(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    return text

def count_bi_nointersect(text):
    res = Counter(text[idx: idx + 2] for idx in range(0, (len(text)), 2))
    total_bi = sum(res.values())
    res = {x: round(res[x]/total_bi, 10) for x in res}
    return dict(res)


def find_sence(text):
    current_lst = count_bi_nointersect(text)
    top_bi = ('ст', 'но', 'то', 'на', 'ен')
    final = 0

    current_sorted = dict(sorted(current_lst.items(), key=operator.itemgetter(1), reverse=True))
    current_top = dict(islice(current_sorted.items(), 5))

    for t in top_bi:
        if t in current_top:
            final += 20

    print(f"Top values have {final}% match")


def avg(x):
    print(len(x))
    return sum(x.values())/len(x)


def find_sence_2(text):
    forbidden_lst = ('аъ', 'аь', 'бй', 'бф', 'гщ', 'гъ', 'еъ', 'еь', 'жй', 'жц', 'жщ', 'жъ', 'жы', 'йъ', 'къ', 'лъ', 'мъ', 'оъ', 'пъ', 'ръ', 'уъ', 'уь', 'фщ', 'фъ', 'хы', 'хь', 'цщ', 'цъ', 'цю', 'чф', 'чц', 'чщ', 'чъ', 'чы', 'чю', 'шщ', 'шъ', 'шы', 'шю', 'щг', 'щж', 'щл', 'щх', 'щц', 'щч', 'щш', 'щъ', 'щы', 'щю', 'щя', 'ъа', 'ъб', 'ъг', 'ъд', 'ъз', 'ъй', 'ък', 'ъл', 'ън', 'ъо', 'ъп', 'ър', 'ъс', 'ът', 'ъу', 'ъф', 'ъх', 'ъц', 'ъч', 'ъш', 'ъщ', 'ъъ', 'ъы', 'ъь', 'ъэ', 'ыъ', 'ыь', 'ьъ', 'ьы', 'эа', 'эж', 'эи', 'эо', 'эу', 'эщ', 'эъ', 'эы', 'эь', 'эю', 'эя', 'юъ', 'юы', 'юь', 'яъ', 'яы', 'яь', 'ьь')
    current_lst = count_bi_nointersect(text)
    result = 0
    counter = 0

    for f in forbidden_lst:
        if f in current_lst:
            result += current_lst[f]
            counter += 1
    try:
        final = result/counter
    except ZeroDivisionError:
        return True

    if final <= avg(current_lst):
        return True

clean_text("pushkin_kapitanskaya-dochka_zqapla_253790.txt")
test = open_file("exmpl_clean.txt")
"""
find_sence(test)"""
print(find_sence_2(test))

