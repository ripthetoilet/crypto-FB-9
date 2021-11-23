#coding=UTF-8
import random
import pandas as pd

rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
                'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']

rus_index_of_considence = 0.0566

def calc_symbol_freq(symbol, text):
    symbol_counter = 0
    for text_symbol in text:
        if symbol == text_symbol:
            symbol_counter = symbol_counter + 1
    return symbol_counter / len(text)

def count_letters_in_text(text, alphabet=rus_alphabet):
    letters_amount_dict = {}
    for i in rus_alphabet:
        letters_amount_dict.update({i: 0})
    for ch in text:
        letters_amount_dict.update({ch: letters_amount_dict[ch] + 1})
    return letters_amount_dict        

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
    for i in count_letters_in_text(text).values():
        index += i * (i - 1)
    n = len(text)
    index /= n * (n - 1)
    return index

def divide_to_blocks(text, num):
    text_blocks_list = []
    

#Additional functions:
def generate_table_of_EncText_and_indexes(open_text, key_len_list, log_file='index_table'):
    key_dict = {}
    enc_text_dict = {}
    index_of_considence_dict = {}

    for i in sorted(key_len_list):
        key_dict.update({i: 0})
        enc_text_dict.update({i: 0})
        index_of_considence_dict.update({i: 0})
    for i in key_len_list:
        key = generate_key(i)
        enc_text = encrypt(open_text, key)
        key_dict.update({i: key})
        enc_text_dict.update({i: enc_text[0:39]})
        index_of_considence_dict.update({i: count_considence_index(enc_text)})
    table = pd.DataFrame({'Key': key_dict.values(),
                        'index of considence': index_of_considence_dict.values(),
                        'Enc. text': enc_text_dict.values()}, index=key_len_list)
    if log_file != None:
        table.to_excel(log_file + '.xlsx')
    return table


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

def main2():
    file_open_text = open('dyuma_cut.txt', 'r')
    open_text = file_open_text.read()
    file_open_text.close()
    key_len_list = [2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    generate_table_of_EncText_and_indexes(open_text, key_len_list, 'indexes1')
                
if __name__ == '__main__':
    main2()
    #main()