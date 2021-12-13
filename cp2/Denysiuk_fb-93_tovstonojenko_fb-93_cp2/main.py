from statistics import mean
import vigenere_lib as vl

IOC_RUS = 0.0553
OPEN_TEXT = 'hookah.txt'
CYPHERED_TEXT = 'cyphered_text.txt'

text = vl.filter_text(OPEN_TEXT)

print(f'Index of coincidence original text: {vl.count_index_of_coincidence(text)}')
vl.print_encoded_text_to_files(list(range(2, 6)) + list(range(10, 21)), text)

with open(CYPHERED_TEXT, mode='rt', encoding='utf-8') as file:
    cyphered_text = file.read()

stats_IOF_for_different_length_of_key = {}
for i in range(1, 30):
    stats_IOF_for_different_length_of_key[i] = \
        vl.generate_list_of_indexes_of_coincidence_for_text_with_length_of_key(i, cyphered_text)

vl.print_results_to_file('stats_IOF_for_different_length_of_key', stats_IOF_for_different_length_of_key)

differences_between_expected_and_actual_value = [(k, abs(mean(v) - IOC_RUS)) for k, v in
                                                 stats_IOF_for_different_length_of_key.items()
                                                 if abs(mean(v) - (1 / 32)) > 0.012]
differences_between_expected_and_actual_value.sort(key=lambda item: item[1])

for i in differences_between_expected_and_actual_value:
    print(f'differences between expected and actual for length of key {i[0]}: {i[1]:.10f}')

for supposable_len_of_key in [i[0] for i in differences_between_expected_and_actual_value]:
    answer = input(f'Do you want to try generate key with length {supposable_len_of_key}?(Y-yes/other -no)')
    if answer.lower() != 'y':
        continue
    key = vl.generate_supposable_key(cyphered_text, supposable_len_of_key)
    print(f'\nsupposable key is:{key}')
    print(cyphered_text)
    print(key * 50)
    print(vl.decrypt(cyphered_text, key))

key = input('Enter your variant of key(ENTER to skip):')
if key != '':
    print(vl.decrypt(cyphered_text, key))
