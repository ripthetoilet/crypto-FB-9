#coding=UTF-8

rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
                'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']

def calc_symbol_freq(symbol, text):
    symbol_counter = 0
    for text_symbol in text:
        if symbol == text_symbol:
            symbol_counter = symbol_counter + 1
    return symbol_counter / len(text)

def main():
    pass

if __name__ == '__main__':
    main()