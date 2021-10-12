from collections import defaultdict
import re
from math import log

print("1 >>> Text without spaces\n2 >>> Text with spaces\n")
what = input()
with open("need.txt", "r", encoding="utf-8") as txt:
    if what == "1":
        content = re.sub('[^а-я\ё]+', '', txt.read().lower())
    elif what == "2":
        content = re.sub('[^а-я\ё]+', ' ', txt.read().lower())


def amount(content: str) -> dict:
    result = defaultdict(int)
    for char in list(content):
        result[char] += 1
    return dict(result)


def freq(mark: dict) -> dict:
    return {x: y / sum(mark.values()) for x, y in mark.items()}


def entr(mark: dict) -> float:
    summ = sum(mark.values())
    en = 0
    for i in mark:
        en += mark[i] / summ * log(mark[i] / summ, 2)
    return - en


if what == "1":
    with open("TxWithoutSpaces.txt", "w+", encoding="utf-8") as file:
        for letter, num in sorted(freq(amount(content)).items(), key=lambda symbol: symbol[1], reverse=True):
            file.write(f'{letter} >>> {num} time(s)\n')
    print(f'Our entropy without spaces >>> {entr(amount(content))}')
elif what == "2":
    with open("TxWithSpaces.txt", "w+", encoding="utf-8") as file:
        for letter, num in sorted(freq(amount(content)).items(), key=lambda symbol: symbol[1], reverse=True):
            file.write(f'{letter.replace(" ", "_")} >>> {num} time(s)\n')
    print(f'Our entropy with spaces >>> {entr(amount(content))}')
