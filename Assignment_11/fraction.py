import math

class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def pulse(self, other):
        result_numerator = other.numerator * self.denominator + other.denominator * self.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def multiple(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def minus(self, other):
        temp_numerator = (self.numerator * other.denominator)
        temp_numerator2 = (other.numerator * self.denominator)
        result_numerator = temp_numerator - temp_numerator2
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other):
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        return Fraction(result_numerator, result_denominator)

    def fraction_to_int(self):
        return self.numerator / self.denominator

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def show(self):
        print(f"{self.numerator}/{self.denominator}")
        