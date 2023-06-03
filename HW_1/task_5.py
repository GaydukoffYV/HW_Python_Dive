# Задача 2 домашнего задания Семинара1
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
number = int(input("Введите число от 2 до 100000: "))

if number < 2 or number > 100000:
    print("Число не входит в диапазон от 2 до 100000")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Число является простым")
    else:
        print("Число является составным")
