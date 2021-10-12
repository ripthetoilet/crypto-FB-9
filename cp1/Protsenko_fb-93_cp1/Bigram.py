from collections import Counter
import re
from math import log

print("1 >>> Bigram without spaces\n2 >>> Bigram with spaces\n")
what = input()
print("1 >>> Step 1\n2 >>> Step 2\n")
head = input()
with open("need.txt", "r", encoding="utf-8") as txt:
    if what == "1":
        content = re.sub('[^а-я\ё]+', '', txt.read().lower())
    elif what == "2":
        content = re.sub('[^а-я\ё]+', ' ', txt.read().lower())


def amount(content: str) -> dict:
    result = Counter(content[idx: idx + 2]
                     for idx in range(0, len(content) - 1, int(head)))
    return dict(result)


def freq(mark: dict) -> dict:
    return {x: y / sum(mark.values()) for x, y in
            mark.items()}


def entr(mark: dict) -> float:
    summ = sum(mark.values())
    en = 0
    for i in mark:
        en += mark[i] / summ * log(mark[i] / summ, 2)
    return - en / 2


if what == "1" and head == "1":
    with open("BgWithoutSpaces1.txt", "w+", encoding="utf-8") as file:
        for letter, num in sorted(freq(amount(content)).items(), key=lambda symbol: symbol[1], reverse=True):
            file.write(f'{letter} >>> {num} time(s)\n')
    print(f'Our Bg entropy without spaces 1 >>> {entr(amount(content))}')
elif what == "1" and head == "2":
    with open("BgWithoutSpaces2.txt", "w+", encoding="utf-8") as file:
        for letter, num in sorted(freq(amount(content)).items(), key=lambda symbol: symbol[1], reverse=True):
            file.write(f'{letter} >>> {num} time(s)\n')
    print(f'Our Bg entropy without spaces 2 >>> {entr(amount(content))}')
elif what == "2" and head == "1":
    with open("BgWithSpaces1.txt", "w+", encoding="utf-8") as file:
        for letter, num in sorted(freq(amount(content)).items(), key=lambda symbol: symbol[1], reverse=True):
            file.write(f'{letter.replace(" ", "_")} >>> {num} time(s)\n')
    print(f'Our Bg entropy with spaces 1 >>> {entr(amount(content))}')
elif what == "2" and head == "2":
    with open("BgWithSpaces2.txt", "w+", encoding="utf-8") as file:
        for letter, num in sorted(freq(amount(content)).items(), key=lambda symbol: symbol[1], reverse=True):
            file.write(f'{letter.replace(" ", "_")} >>> {num} time(s)\n')
    print(f'Our Bg entropy with spaces 2 >>> {entr(amount(content))}')
