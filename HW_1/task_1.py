# Задача №7 с семинара1, которую не успели решить

number = int(input("Введите число от 1 до 999: "))

if number < 1 or number > 999:
    print("Число не входит в диапазон от 1 до 999")
elif number < 10:
    print("Введена цифра")
    print(number ** 2)
elif number < 100:
    print("Введено двузначное число")
    first_digit = number // 10
    second_digit = number % 10
    print(first_digit * second_digit)
else:
    print("Введено трехзначное число")
    first_digit = number // 100
    second_digit = (number // 10) % 10
    third_digit = number % 10
    reversed_number = third_digit * 100 + second_digit * 10 + first_digit
    print(reversed_number)
