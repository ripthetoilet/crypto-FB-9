#coding=UTF-8
import random

rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
                'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']

def calc_symbol_freq(symbol, text):
    symbol_counter = 0
    for text_symbol in text:
        if symbol == text_symbol:
            symbol_counter = symbol_counter + 1
    return symbol_counter / len(text)

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

def generate_key(size):
    key = ''
    for i in range(0, size):
        #TODO: It is better to find another solution
        key += ''.join(random.choice(rus_alphabet))
    return key

def main():
    text = str()
    with open('dyuma_cut.txt', 'r') as dyuma_file:
        text = dyuma_file.read()
    key = generate_key(2)
    with open('enc_text1.txt', 'w') as enc_file1:
        enc_file1.write(encrypt(text, key))
    key = generate_key(10)
    with open('enc_text2.txt', 'w') as enc_file2:
        enc_file2.write(encrypt(text, key))

if __name__ == '__main__':
    main()