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

def make_list_of_bigram(text: str, step:int)->list:
    pass

def make_dict_of_frequency_of_bigram(text:str, step:int)->dict:
    list_of_bigram=make_list_of_bigram(text, step)
    dict_of_frequency_of_bigram={}
    for bigram in list_of_bigram:
        dict_of_frequency_of_bigram[bigram]=text.count(bigram)/len(list_of_bigram)
        
