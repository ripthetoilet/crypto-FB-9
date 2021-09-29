from collections import defaultdict
from math import log
import re


def filter_text(file_name: str, with_whitespace: bool) -> str:
    with open(file_name, mode='rt', encoding='UTF-8') as f:
        filtered = f.read().lower().replace("ъ", "ь").replace("ё", "е")
    return re.sub("[^а-я]+", '', filtered) if not with_whitespace else re.sub("[^а-я]+", ' ', filtered)


def make_dict_of_frequency_of_chars(text: str) -> dict:
    stats = defaultdict(int)
    for char in text:
        stats[char] += 1
    stats = dict(stats)
    return stats


def make_list_of_bigram(text: str, step: int) -> list:
    if len(text) % 2 == 1:
        text = text + 'a'
    return [text[i] + text[i + 1] for i in range(0, len(text) - 1, step)]


def make_dict_of_stats_of_bigram(text: str, step: int) -> dict:
    list_of_bigram = make_list_of_bigram(text, step)
    dict_of_stats_of_bigram = {}
    if len(text) % 2 == 1:
        text = text + 'a'
    for bigram in set(list_of_bigram):
        dict_of_stats_of_bigram[bigram] = text.count(bigram)
    return dict_of_stats_of_bigram


def print_results_in_file(file_name: str, dict_of_items: dict[str, float]):
    with open(f'./results/{file_name}.csv', mode='w', encoding='UTF-8') as frc_of_chars_file:
        frc_of_chars_file.write('symbol, frequency\n')
        d = dict(sorted(dict_of_items.items(), key=lambda item: item[1], reverse=True))
        for k, v in d.items():
            frc_of_chars_file.write(f'"{k}",{v}\n')


def stats_to_frequency(stat: dict) -> dict:
    return {k: v / sum(stat.values()) for k, v in
            stat.items()}


def calculate_entropy(n: int, stats: dict) -> float:
    entropy = 0
    quantity = sum(stats.values())
    for i in stats:
        entropy += stats[i] / quantity * log(stats[i] / quantity, 2)
    return -entropy / n
