# Задание №6 семинара 3
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text = input("Введите текст: ")
words = text.split()
words_sorted = sorted(words, key=lambda x: x.lower())  # сортировка слов

max_len = max([len(w) for w in words])  # длинна самого длинного слова

for i, word in enumerate(words_sorted, 1):  # перебираем отсортированные слова с нумерацией
    n_spaces = max_len - len(word) + 1
    print(f"{i:2d}.{' ' * n_spaces}{word}")