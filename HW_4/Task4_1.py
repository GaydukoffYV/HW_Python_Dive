# Задание №6 семинара 4
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 2
j = 5


def sum_between_indexes(numbers, i, j):
    start_index = min(i, j)
    end_index = max(i, j)
    list_length = len(numbers)
    start_index = max(start_index, 0)
    end_index = min(end_index, list_length - 1)
    if start_index > end_index:
        return 0
    else:
        return sum(numbers[start_index:end_index + 1])


result = sum_between_indexes(numbers, i, j)
print(result)
