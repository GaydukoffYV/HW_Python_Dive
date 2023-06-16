# функция для пополнения счета
def deposit(amount):
    global balance, operations
    if amount % 50 != 0:
        print("Сумма должна быть кратна 50")
        return
    balance += amount
    operations.append(f"Пополнение: {amount}")
    if len(operations) % 3 == 0:
        add_interest()


# функция для снятия со счета
def withdraw(amount):
    global balance, operations
    if amount % 50 != 0:
        print("Сумма должна быть кратна 50")
        return
    if amount > balance:
        print("Недостаточно средств на счете")
        return
    if balance >= 5000000:
        tax = balance * 0.1
        balance -= tax
        operations.append(f"Налог на богатство: {tax}")
    fee = amount * 0.015
    if fee < 30:
        fee = 30
    elif fee > 600:
        fee = 600
    balance -= (amount + fee)
    operations.append(f"Снятие: {amount}, комиссия: {fee}")
    if len(operations) % 3 == 0:
        add_interest()


# функция для добавления процентов
def add_interest():
    global balance, operations
    interest = balance * 0.03
    balance += interest
    operations.append(f"Начисление процентов: {interest}")


# функция для вывода баланса
def show_balance():
    global balance
    print(f"Баланс: {balance}")


# функция для вывода всех операций
def show_operations():
    global operations
    print("Операции:")
    for op in operations:
        print(op)


# функция для сохранения операций в файл
def save_operations():
    global operations
    with open("operations.txt", "w") as f:
        for op in operations:
            f.write(op + "\n")


balance = 0
operations = []

while True:
    print("Выберите действие:")
    print("1 - Пополнить счет")
    print("2 - Снять со счета")
    print("3 - Показать баланс")
    print("4 - Показать все операции")
    print("5 - Выйти")
    choice = input()
    if choice == "1":
        amount = int(input("Введите сумму для пополнения: "))
        deposit(amount)
        show_balance()
    elif choice == "2":
        amount = int(input("Введите сумму для снятия: "))
        withdraw(amount)
        show_balance()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        show_operations()
    elif choice == "5":
        save_operations()
        break
    else:
        print("Некорректный выбор")
