import re
from collections import Counter
from math import log2

file = open('source.txt', encoding='cp1251')
report = open('report.txt', 'w')
text = file.read()
text_with_spaces = re.sub(r'[^а-яА-Я ]', '', text).lower()
text_without_spaces = re.sub(r'[^а-яА-Я]', '', text).lower()


def letters_frequency(text):
    frequency = Counter(text)
    return dict(frequency)


def bigrams_frequency(text):
    frequency = Counter(text[bi: bi + 2] for bi in range(len(text) - 1))
    return dict(frequency)


def get_probability(frequency, text):
    probability = frequency
    for key in frequency.keys():
        probability[key] /= len(text)
    return probability


def entropy(probability):
    entropy = 0
    for value in probability.values():
        entropy += -value * log2(value)
    return entropy


def excess(entropy, quantity):
    return 1 - entropy / log2(quantity)


def output(var):
    for letter in var:
        report.write(f'{letter} -- {str(var[letter])}\n')
    report.write(f'\n\n')


letters_w_spaces_frequency = letters_frequency(text_with_spaces)
letters_wo_spaces_frequency = letters_frequency(text_without_spaces)
bigrams_w_spaces_frequency = bigrams_frequency(text_with_spaces)
bigrams_wo_spaces_frequency = bigrams_frequency(text_without_spaces)

letters_w_spaces_probability = get_probability(letters_w_spaces_frequency, text_with_spaces)
letters_wo_spaces_probability = get_probability(letters_wo_spaces_frequency, text_without_spaces)
bigrams_w_spaces_probability = get_probability(bigrams_w_spaces_frequency, text_with_spaces)
bigrams_wo_spaces_probability = get_probability(bigrams_wo_spaces_frequency, text_without_spaces)

letters_w_spaces_entropy = entropy(letters_w_spaces_probability)
letters_wo_spaces_entropy = entropy(letters_wo_spaces_probability)
bigrams_w_spaces_entropy = entropy(bigrams_w_spaces_probability) / 2
bigrams_wo_spaces_entropy = entropy(bigrams_wo_spaces_probability) / 2

letters_w_spaces_excess = excess(letters_w_spaces_entropy, 33)
letters_wo_spaces_excess = excess(letters_wo_spaces_entropy, 32)
bigrams_w_spaces_excess = excess(bigrams_w_spaces_entropy, 33)
bigrams_wo_spaces_excess = excess(bigrams_wo_spaces_entropy, 32)

report.write(f'Entropy of letters with spaces:\n{letters_w_spaces_entropy}\n'
             f'Entropy of letters without spaces:\n{letters_wo_spaces_entropy}\n'
             f'Entropy of bigrams with spaces:\n{bigrams_w_spaces_entropy}\n'
             f'Entropy of bigrams without spaces:\n{bigrams_wo_spaces_entropy}\n\n')

report.write(f'Excess of letters with spaces:\n{letters_w_spaces_excess}\n'
             f'Excess of letters without spaces:\n{letters_wo_spaces_excess}\n'
             f'Excess of bigrams with spaces:\n{bigrams_w_spaces_excess}\n'
             f'Excess of bigrams without spaces:\n{bigrams_wo_spaces_excess}\n\n')

report.write(f'Letters with spaces frequency:\n')
output(letters_w_spaces_frequency)
report.write(f'Letters without spaces frequency:\n')
output(letters_wo_spaces_frequency)
report.write(f'Bigrams with spaces frequency:\n')
output(bigrams_w_spaces_frequency)
report.write(f'Bigrams without spaces frequency:\n')
output(bigrams_wo_spaces_frequency)

report.write(f'Letters with spaces probability:\n')
output(letters_w_spaces_probability)
report.write(f'Letters without spaces probability:\n')
output(letters_wo_spaces_probability)
report.write(f'Bigrams with spaces probability:\n')
output(bigrams_w_spaces_probability)
report.write(f'Bigrams without spaces probability:\n')
output(bigrams_wo_spaces_probability)
