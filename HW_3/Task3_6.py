# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


my_list = [1, 2, 3, 4, 5, 6, 2, 3, 5, 7, 8, 9, 8]

duplicates = []
for item in my_list:
    if my_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)
