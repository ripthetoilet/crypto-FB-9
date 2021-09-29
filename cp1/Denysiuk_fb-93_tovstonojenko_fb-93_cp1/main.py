import my_lib

NAME_OF_FILE = 'Dart_Plegas.txt'

text_with_whitespace = my_lib.filter_text(NAME_OF_FILE, with_whitespace=True)
text_without_whitespaces = my_lib.filter_text(NAME_OF_FILE, with_whitespace=False)

# Виведення частотності в файли
stats_of_characters_with_whitespace = my_lib.make_dict_of_frequency_of_chars(text_with_whitespace)
stats_of_characters_without_whitespace = my_lib.make_dict_of_frequency_of_chars(text_without_whitespaces)
my_lib.print_results_in_file('frequency_of_characters_with_whitespace',
                             my_lib.stats_to_frequency(stats_of_characters_with_whitespace))
my_lib.print_results_in_file('frequency_of_characters_without_whitespace',
                             my_lib.stats_to_frequency(stats_of_characters_without_whitespace)
                             )
# Виведення частотності біграм без пробілів в файли
stats_of_cross_biggram_without_whitespaces = my_lib.make_dict_of_stats_of_bigram(text_without_whitespaces, 1)
stats_of_biggram_without_whitespaces = my_lib.make_dict_of_stats_of_bigram(text_without_whitespaces, 2)
my_lib.print_results_in_file('frequency_of_cross_biggram_without_whitespace',
                             my_lib.stats_to_frequency(stats_of_cross_biggram_without_whitespaces))
my_lib.print_results_in_file('frequency_of_biggram_without_whitespace',
                             my_lib.stats_to_frequency(stats_of_biggram_without_whitespaces)
                             )
# Виведення частотності біграм з пробілами в файли
stats_of_cross_biggram_with_whitespaces = my_lib.make_dict_of_stats_of_bigram(text_with_whitespace, 1)
stats_of_biggram_with_whitespaces = my_lib.make_dict_of_stats_of_bigram(text_with_whitespace, 2)
my_lib.print_results_in_file('frequency_of_cross_biggram_with_whitespace',
                             my_lib.stats_to_frequency(stats_of_cross_biggram_with_whitespaces))
my_lib.print_results_in_file('frequency_of_biggram_with_whitespace',
                             my_lib.stats_to_frequency(stats_of_biggram_with_whitespaces)
                             )
