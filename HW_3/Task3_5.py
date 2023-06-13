# Задание №8 семинара 3
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

from functools import reduce

friends_stuff = {
    'Друг 1': ('Палатка', 'Спальник', 'Фонарик', 'Газовая горелка'),
    'Друг 2': ('Палатка', 'Спальник', 'Тент', 'Перчатки'),
    'Друг 3': ('Палатка', 'Спальник', 'Фонарик', 'Кружка')
}

# Какие вещи взяли все три друга
all_friends_stuff = set(reduce(set.intersection, [set(stuff) for stuff in friends_stuff.values()]))
print(f'Вещи, которые взяли все три друга: {", ".join(all_friends_stuff)}')

# Какие вещи уникальны, есть только у одного друга
unique_items = set.union(*[set(v) for v in friends_stuff.values()]) - all_friends_stuff
for item in unique_items:
    for name, items in friends_stuff.items():
        if item in items:
            print(f'Уникальная вещь {item} у друга {name}')
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
items_data = {}
for friend, items in friends_stuff.items():
    for item in items:
        if item not in items_data:
            items_data[item] = [friend]
        else:
            items_data[item].append(friend)

for item, friends in items_data.items():
    if len(friends) == len(friends_stuff) - 1:
        missing_friend = (set(friends_stuff.keys()) - set(friends)).pop()
        print(f'Друзья {", ".join(friends)} взяли {item}, но нет у друга {missing_friend}.')
