# Задание №7 семинара 4
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


data = {
    'Company A': [100, 50, 100, 200],
    'Company B': [500, 200, 300],
    'Company C': [50, 100, 50, 200],
    'Company D': [200, 100, -100, 300],
}


def check_company_profit(companies_data):
    all_profitable = True
    for company, data in companies_data.items():
        income = sum(data)
        expenses = abs(min(data, default=0))
        profit = income - expenses
        if profit < 0:
            all_profitable = False
        companies_data[company] = profit
    return all_profitable, companies_data


is_all_profitable, companies_profit = check_company_profit(data)
print("Все компании прибыльны:", is_all_profitable)
print("Прибыль/убыток компании:", companies_profit)
