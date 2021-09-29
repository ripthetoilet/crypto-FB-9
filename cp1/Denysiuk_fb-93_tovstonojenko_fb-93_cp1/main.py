import my_lib
NAME_OF_FILE='Dart_Plegas.txt'

text_with_whitespace = my_lib.filter_text(NAME_OF_FILE, with_whitespace=True)
text_without_whitespaces = my_lib.filter_text(NAME_OF_FILE, with_whitespace=False)

#Виведення частотності в файли
my_lib.print_results_in_file('frequency_of_characters_with_whitespace',
                             my_lib.make_dict_of_frequency_of_chars(text_with_whitespace))
my_lib.print_results_in_file('frequency_of_characters_without_whitespace',
                             my_lib.make_dict_of_frequency_of_chars(text_without_whitespaces))