from text_processing import process_text
import pandas as pd

ru_alphabet = [chr(code) for code in range(ord("а"), ord("а") + 32)]

with open("keys.txt", "r", encoding="utf-8") as file:
    keys = file.read().lower().split(",")


def encode_text(text: str, key: str) -> str:
    result = []
    for index, letter in enumerate(text):
        result.append(ru_alphabet[(ru_alphabet.index(letter) + ru_alphabet.index(key[index % len(key)])) % len(ru_alphabet)])
    return "".join(result)


def decode_text(text: str, key: str) -> str:
    result = []
    for index, letter in enumerate(text):
        result.append(ru_alphabet[(ru_alphabet.index(letter) - ru_alphabet.index(key[index % len(key)])) % len(ru_alphabet)])
    return "".join(result)


def calculate_index(text: str) -> float:
    index = 0
    for letter in ru_alphabet:
        letter_count = text.count(letter)
        index += letter_count * (letter_count - 1)
    return index / (len(text) * (len(text) - 1))


def theoretical_index() -> float:
    df = pd.read_excel("character_frequency.xlsx", index_col=0)
    df = df.apply(lambda x: pow(x, 2))
    return df['Frequency'].sum()


def split_to_blocks(text, length) -> list:
    blocks = []
    for i in range(length):
        blocks.append(text[i::length])
    return blocks


def find_key_length(encoded_text) -> dict:
    index_length_dict = {}
    possible_lengths = [x for x in range(2, 31)]
    for length in possible_lengths:
        blocks = split_to_blocks(encoded_text, length)
        index = 0
        for block in blocks:
            index += calculate_index(block)
        index /= len(blocks)
        index_length_dict[length] = index
    return dict(sorted(index_length_dict.items(), key=lambda x: x[1], reverse=True))


def char_frequency(some_text: str) -> dict:
    freq_dict = {}
    for char in ru_alphabet:
        char_count = some_text.count(char)
        freq_dict[char] = char_count / len(some_text)
    return dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))


def find_key(encoded_text: str, key_length: int) -> list:
    blocks = split_to_blocks(encoded_text, key_length)
    most_used_letters = "оаеин"
    possible_keys = []
    for letter in most_used_letters:
        key = ""
        for block in blocks:
            most_used_letter_encoded_text = list(char_frequency(block).keys())[0]
            key_part = ru_alphabet[
                (ru_alphabet.index(most_used_letter_encoded_text) - ru_alphabet.index(letter)) % len(ru_alphabet)
                ]
            key += key_part
        possible_keys.append(key)
    return possible_keys


processed_text = process_text(ru_alphabet, "text.txt")

language_index = theoretical_index()
index_for_original_text = calculate_index(processed_text)

print(f"Theoretical index: {language_index}")
print(f"Index for original text: {index_for_original_text}")
all_indexes = {}
for key in keys:
    print(f"Key length: {len(key)}")
    encoded_text = encode_text(processed_text, key)
    decoded_text = decode_text(encoded_text, key)
    index_for_encoded_text = calculate_index(encoded_text)
    print(f"Encoded text: {encoded_text}\nKey: {key}\nDecoded text: {decoded_text}\nI: {index_for_encoded_text}")
    print(f"Possible lengths of a key: {find_key_length(encoded_text)}")
    print("-" * 100)
    all_indexes[key] = index_for_encoded_text  # save this

text_to_decode = process_text(ru_alphabet, "decode.txt")
keys_length = find_key_length(text_to_decode)
possible_key_length = list(keys_length.keys())[0]
print(find_key(text_to_decode, possible_key_length))
print(decode_text(text_to_decode, 'последнийдозор'))
print(text_to_decode)
#  Save keys_length to excel
keys_length_df = pd.DataFrame(keys_length.values(), index=keys_length.keys())
keys_length_df.columns = ["I"]
keys_length_df.index.names = ["R"]
keys_length_df.to_excel("possible_key_lengths.xlsx")
#  Save indexes for encoded text to excel
all_indexes_df = pd.DataFrame(all_indexes.values(), index=all_indexes.keys())
all_indexes_df.columns = ["I"]
all_indexes_df.index.names = ["Key"]
key_length_indexes = [len(x) for x in all_indexes.keys()]
all_indexes_df.insert(0, "Length", key_length_indexes)
all_indexes_df.to_excel("indexes_for_different_keys.xlsx")
