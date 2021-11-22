#coding=UTF-8
import random
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

def calc_all_symbols_freq(alphabet, text, is_space_allowed = False, log_file_name = None):
    symbol_num_dict = {}
    symbol_freq_dict = {}
    if is_space_allowed:
        alphabet.append(' ')
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

    return symbol_freq_dict

def generate_key(size):
    key = ''
    for i in range(0, size):
        #TODO: It is better to find another solution
        key += ''.join(random.choice(rus_alphabet))
    return key

def encrypt_letter(ch, key_letter, alphabet=rus_alphabet):
    ch_id = alphabet.index(ch)
    k_id = alphabet.index(key_letter)
    enc_ch_id = (ch_id + k_id) % len(alphabet)
    enc_ch = alphabet[enc_ch_id]
    return enc_ch

def encrypt(text, key):
    enc_text = list()
    for i, j in enumerate(text):
        enc_text.append(encrypt_letter(j, key[i % len(key)]))
    return "".join(enc_text)

def decrypt_letter(enc_ch, key_letter, alphabet=rus_alphabet):
    enc_ch_id = alphabet.index(enc_ch)
    k_id = alphabet.index(key_letter)
    dec_ch_id = (enc_ch_id - k_id) % len(alphabet)
    dec_ch = alphabet[dec_ch_id]
    return dec_ch

def decrypt(enc_text, key, alphabet=rus_alphabet):
    dec_text = list()
    for i, j in enumerate(enc_text):
        dec_text.append(decrypt_letter(j, key[i % len(key)], alphabet))
    return "".join(dec_text) 

def count_considence_index(text):
    index = 0
    for i in calc_all_symbols_freq(rus_alphabet, text).values():
        index += i * (i - 1)
    n = len(text)
    index /= n * (n - 1)
    return index

def main():
    while(True):
        print("To encrypt text: 2")
        print("To calculate index: 1")
        print("Quit: 0")
        command = input()
        if command == '0':
            break
        elif command == '1':
            print("Type file name:")
            file_name = input()
            with open(file_name, 'r') as file:
                text = file.read()
                print(count_considence_index(text))
        elif command == '2':
            print("Type file name of original text:")
            input_file_name = input()
            print("Type size of key for encryption:")
            key_size = int(input())
            print("Enter file name for encrypted text:")
            enc_file_name = input()
            with open(input_file_name, 'r') as input_file:
                input_text = input_file.read()
                with open(enc_file_name, 'w') as output_file:
                    key = generate_key(key_size)
                    output_file.write(encrypt(input_text, key))

                
if __name__ == '__main__':
    main()