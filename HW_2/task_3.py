# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def reduce_fraction(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def add_fractions(frac1, frac2):
    numerator = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    return reduce_fraction(numerator, denominator)


def multiply_fractions(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return reduce_fraction(numerator, denominator)


frac1_str = input("Введите первую дробь в формате a/b: ")
frac1 = tuple(map(int, frac1_str.split('/')))
frac2_str = input("Введите вторую дробь в формате a/b: ")
frac2 = tuple(map(int, frac2_str.split('/')))
sum_frac = add_fractions(frac1, frac2)
prod_frac = multiply_fractions(frac1, frac2)

print("Сумма дробей:", sum_frac[0], '/', sum_frac[1])
print("Произведение дробей:", prod_frac[0], '/', prod_frac[1])

# frac1 = Fraction(a, b)
# frac2 = Fraction(c, d)
# sum_frac = frac1 + frac2
# prod_frac = frac1 * frac2
# print(sum_frac)
# print(prod_frac)
