# Задача 4 семинара 3

my_list = [2, 4, 3, 4, "apple", "banana", "apple", 3.14, 2]

print("Исходный список:", my_list)

unique_list = []
duplicates = []

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
    else:
        duplicates.append(i)

for i in duplicates:
    while i in unique_list:
        unique_list.remove(i)

print("Список без повторов:", unique_list)
