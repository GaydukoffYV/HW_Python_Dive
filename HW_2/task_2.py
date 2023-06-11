# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

num = int(input("Введите целое число: "))
hex_dict = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}

hex_list = []

while num != 0:
    remainder = num % 16
    hex_list.append(hex_dict[remainder])
    num = num // 16
if len(hex_list) == 0:
    hex_list.append('0')
hex_str = ''.join(hex_list[::-1])

print("Шестнадцатеричное представление числа", num, ":", hex_str)

# num = int(input("Введите целое число: "))
# hex_num = hex(num)
# print(hex_num)
