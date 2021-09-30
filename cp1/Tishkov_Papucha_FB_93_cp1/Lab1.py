#coding=UTF-8
import os
import math
import pandas as pd

rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
                'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']


def calc_symbol_freq(symbol, text):
    symbol_counter = 0
    for text_symbol in text:
        if symbol == text_symbol:
            symbol_counter = symbol_counter + 1
    return symbol_counter / len(text)


def calc_all_symbols_freq(alphabet, text, log_file_name = None):
    symbol_num_dict = {}
    symbol_freq_dict = {}
    for letter in alphabet:
        symbol_num_dict.update({letter: 0})
        symbol_freq_dict.update({letter: 0})
    for symbol in text:
        symbol_num_dict[symbol] = symbol_num_dict[symbol] + 1
    for symbol in alphabet:
        symbol_freq_dict[symbol] = symbol_num_dict[symbol] / len(text)
    
    if log_file_name != None:
        sorted_symbol_freq_dict = dict(sorted(symbol_freq_dict.items(), key=lambda item: item[1], reverse=True))
        out_df = pd.DataFrame.from_dict(sorted_symbol_freq_dict, orient='index', columns=['Frequency'])
        out_df.to_excel(log_file_name + '.xlsx')
    

def calc_monogramm_entropy(alphabet, text):
    entropy = 0
    for symbol in alphabet:
        p = calc_symbol_freq(symbol, text)
        entropy = entropy + (p * math.log(p, 2))
    entropy = entropy * -1
    return entropy


def calc_bigramm_freq(bigramm, text, is_intersec_allowed = False):
    text_len = 0
    bigramm_counter = 0
    if not is_intersec_allowed and len(text) % 2 > 0:
        text_len = len(text - 1)
    else:
        text_len = len(text)

    index = 0
    while index < text_len - 1:
        if bigramm == text[index] + text[index + 1]:
            bigramm_counter = bigramm_counter + 1
        if is_intersec_allowed:
            index = index + 1
        else:
            index = index + 1

    frequency = bigramm_counter / (text_len / 2)
    return frequency
    

def calc_bigramm_entropy(alphabet, text, is_space_allowed = False, is_intersec_allowed = False):
    bigramm_freq_dict = {}
    bigramm_num_dict = {}

    # Reduce text size if its length is odd
    if is_space_allowed:
        alphabet.append(' ')
    text_len = 0
    if len(text) % 2 == 0:
        text_len = len(text)
    else:
        text_len = len(text) - 1

    # Combine all letters for creating bigramms
    for sym1 in alphabet:
        for sym2 in alphabet:
            new_bigramm = sym1 + sym2
            bigramm_freq_dict.update({new_bigramm: 0})
            bigramm_num_dict.update({new_bigramm: 0})

    # Counting bigramm frequency
    index = 0
    while index < text_len - 1:
        sym1 = text[index]
        sym2 = text[index + 1]
        cur_bigramm = sym1 + sym2
        bigramm_num_dict[cur_bigramm] = bigramm_num_dict[cur_bigramm] + 1
        if is_intersec_allowed:
            index = index + 1
        else:
            index = index + 2
    for bigramm in bigramm_num_dict:
        bigramm_freq_dict.update({bigramm: bigramm_num_dict[bigramm]/(text_len/2)})
        #print(bigramm + '-> ' + str(bigramm_freq_dict[bigramm]))

    # Calculating entropy
    bigramm_entropy = 0
    for bigramm_freq in bigramm_freq_dict.values():
        if bigramm_freq == 0:
            continue
        bigramm_entropy = bigramm_entropy + bigramm_freq * math.log(bigramm_freq, 2)
    bigramm_entropy = bigramm_entropy / (-2)
    return bigramm_entropy
    

def make_text_only_alphabet_symbols(in_file_name, out_file_name):
    text_file = open(in_file_name, 'r')
    context = text_file.read()
    text_file.close()
    new_context = str()
    for text_symbol in context:
        for rus_symbol in rus_alphabet:
            if text_symbol == rus_symbol or text_symbol == ' ':
                new_context = new_context + text_symbol
                break
            elif text_symbol == rus_symbol.upper():
                new_context = new_context + text_symbol.lower()
                break
    edited_text_file = open(out_file_name, 'w')
    edited_text_file.write(new_context)
    edited_text_file.close()


def make_text_without_spaces(in_file_name, out_file_name):
    text_file = open(in_file_name, 'r')
    context = text_file.read()
    text_file.close()
    new_context = context.replace(' ', '')
    edited_text_file = open(out_file_name, 'w')
    edited_text_file.write(new_context)
    edited_text_file.close()


def main():
    # TODO: Correct main workflow
    #make_text_only_alphabet_symbols('dyuma.txt', 'dyuma_edited.txt')
    file = open("dyuma_edited.txt", 'r')
    context = file.read()
    file.close()
    #print(calc_bigramm_entropy(rus_alphabet, context, False, False))
    calc_all_symbols_freq(rus_alphabet, context, 'excel')



if __name__ == '__main__':
    main()
    