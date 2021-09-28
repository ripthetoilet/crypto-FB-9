from collections import defaultdict
import re


def filter_text(file_name: str, with_witesspace: bool) -> str:
    with open(file_name, mode='rt', encoding='UTF-8') as f:
        filtered = f.read().lower().replace("ъ", "ь").replace("ё", "е")
    return filtered if not with_witesspace else re.sub("[^а-я]+", ' ', filtered)


def make_dict_of_chars_entry(text: str) -> dict:
    stats = defaultdict(int)
    for char in text:
        stats[char] += 1
    return dict(stats)
