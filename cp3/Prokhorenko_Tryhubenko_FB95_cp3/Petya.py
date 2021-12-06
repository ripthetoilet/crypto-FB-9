from cp3.Prokhorenko_Tryhubenko_FB95_cp3.PetyaUtils import PetyaUtils


class Petya:
    def __init__(self):
        self.most_frequent_bigrams = ['ст', 'но', 'то', 'на', 'ен']
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"

    def crack(self):

        possibles_keys: list = []
        frequent_bigrams_cipher_text: dict = {}
        for iterator_i in range(0, len(self.most_frequent_bigrams) - 1):
            frequent_bigrams_cipher_text = PetyaUtils.get_frequent_bigrams("01.txt")
            for iterator_j in range(0, len(frequent_bigrams_cipher_text) - 1):
                difX = (self.alphabet.index(self.most_frequent_bigrams[iterator_i][0]) * len(
                    self.alphabet) + self.alphabet.index(self.most_frequent_bigrams[iterator_i][1])) - (
                               self.alphabet.index(self.most_frequent_bigrams[iterator_i + 1][0]) * len(
                           self.alphabet) + self.alphabet.index(self.most_frequent_bigrams[iterator_i + 1][1]))
                difY = (self.alphabet.index(frequent_bigrams_cipher_text[iterator_j][0]) * len(
                    self.alphabet) + self.alphabet.index(frequent_bigrams_cipher_text[iterator_j][1])) - (
                               self.alphabet.index(frequent_bigrams_cipher_text[iterator_j + 1][0]) * len(
                           self.alphabet) + self.alphabet.index(frequent_bigrams_cipher_text[iterator_j + 1][1]))
                possible_values = PetyaUtils.calculate_linear_comparisons(difX, difY, len(self.alphabet) ** 2)
                if (type(possible_values) == list):
                    for possible_value in possible_values:
                        if PetyaUtils.calculate_gcd(possible_value, len(self.alphabet))[0] == 1:
                            y = (self.alphabet.index(frequent_bigrams_cipher_text[iterator_j][0]) * len(
                                self.alphabet) + self.alphabet.index(frequent_bigrams_cipher_text[iterator_j][1]))
                            x = (self.alphabet.index(self.most_frequent_bigrams[iterator_i][0]) * len(
                                self.alphabet) + self.alphabet.index(self.most_frequent_bigrams[iterator_i][1]))
                            possibles_keys.append((possible_value, (y - x * possible_value) % len(self.alphabet) ** 2))
        print(possibles_keys)
        for possibles_key in possibles_keys:
            a, b = possibles_key
            plaintext = ""
            for char in PetyaUtils.get_text("01.txt"):
                plaintext += self.alphabet[(PetyaUtils.calculate_inverted(a, len(self.alphabet)) * (
                            self.alphabet.index(char) + len(self.alphabet) - b)) % len(self.alphabet)]
            print(plaintext + "\n\n\n")

    # a,b -> foo1() -> text -> print(text) -> (approve || decline) by RUSSIAN rozpiznavach


p = Petya()
p.crack()
