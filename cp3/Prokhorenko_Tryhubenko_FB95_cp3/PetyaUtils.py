import re
from collections import Counter


class PetyaUtils:
    @staticmethod
    def get_text(path_to_file):
        return re.sub(r"[^а-яА-Я]", "", open(path_to_file).read()).lower()

    @staticmethod
    def calculate_gcd(first_number, second_number):
        if first_number == 0:
            return second_number, 0, 1
        else:
            gcd, x, y = PetyaUtils.calculate_gcd(second_number % first_number, first_number)
            return gcd, y - (second_number // first_number) * x, x

    @staticmethod
    def calculate_inverted(number, module):
        gcd, x, y = PetyaUtils.calculate_gcd(number, module)
        return x % module if gcd == 1 else None

    @staticmethod
    def get_frequent_bigrams(path_to_file):
        text = PetyaUtils.get_text(path_to_file)
        frequency = Counter(text[bi: bi + 2] for bi in range(len(text) - 1))
        frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
        return list(dict(list(frequency.items())[:5]).keys())

    @staticmethod
    def calculate_linear_comparisons(difX, difY, module) -> list:
        gcd, x, y = PetyaUtils.calculate_gcd(difX, module)
        if gcd == 1:
            return [(PetyaUtils.calculate_inverted(difX, module) * difY) % module]
        elif difY % gcd == 0:
            temp = ((difY / gcd) * PetyaUtils.calculate_inverted(difX / gcd, module / gcd)) % (module / gcd)
            return [(temp + d * (module / gcd)) for d in range(0, gcd)]
