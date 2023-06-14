# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


max_weight = int(input("Введите максимально допустимый вес рюкзака: "))
items = {
    'спальник': 1.5,
    'термос': 0.8,
    'тент': 2.0,
    'кухонный газ': 1.2,
    'бутылка с водой': 0.5,
    'еда': 1.5
}


def fit_backpack(items, max_weight):
    result = []
    for i in range(2 ** len(items)):
        combination = []
        weight = 0
        for j in range(len(items)):
            if i & 2 ** j != 0:
                combination.append(list(items.keys())[j])
                weight += list(items.values())[j]
        if weight <= max_weight:
            result.append(combination)
    return result


possible_combinations = fit_backpack(items, max_weight)
print(possible_combinations)
