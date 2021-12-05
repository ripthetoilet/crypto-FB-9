class PetyaUtils:
    @staticmethod
    def calculate_gcd(first_number, second_number):
        if first_number == 0:
            return second_number, 0, 1
        else:
            gcd, x, y = PetyaUtils.calculate_gcd(second_number % first_number, first_number)
            return gcd, y - (second_number // first_number) * x, x

