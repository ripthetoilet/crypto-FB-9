import my_lib
NAME_OF_FILE='Dart_Plegas.txt'

text_with_whitespace = my_lib.filter_text(NAME_OF_FILE, with_whitespace=True)
text_without_whitespaces = my_lib.filter_text(NAME_OF_FILE, with_whitespace=False)

with open('./results/frequency_of_characters_with_whitespace.csv', mode='w', encoding='UTF-8') as frc_of_chars_file:
    frc_of_chars_file.write('symbol, frequency\n')
    d=dict(sorted(my_lib.make_dict_of_frequency_of_chars(text_with_whitespace).items(),
                  key=lambda item: item[1], reverse=True))
    for k, v in d.items():
        frc_of_chars_file.write(f'"{k}",{v}\n')

with open('./results/frequency_of_characters_without_whitespace.csv', mode='w', encoding='UTF-8') as frc_of_chars_file:
    frc_of_chars_file.write('symbol, frequency\n')
    d=dict(sorted(my_lib.make_dict_of_frequency_of_chars(text_without_whitespaces).items(),
                  key=lambda item: item[1], reverse=True))
    for k, v in d.items():
        frc_of_chars_file.write(f'"{k}",{v}\n')
