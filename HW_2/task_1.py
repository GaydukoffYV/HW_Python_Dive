# Задача "Банкомат", оставшаяся с семинара
balance = 0  # начальная сумма равна нулю
count = 0  # счетчик операций

while True:
    print("Ваш баланс:", balance, "у.е.")
    action = input("Выберите действие: пополнить, снять, выйти: ")

    if action == "пополнить":
        amount = int(input("Введите сумму для пополнения (кратную 50): "))
        if amount % 50 != 0:
            print("Сумма должна быть кратна 50")
        else:
            balance += amount
            count += 1
            if count % 3 == 0:  # начисление процентов после каждой третьей операции
                interest = balance * 0.03
                balance += interest
                print("Начислены проценты в размере", interest, "у.е.")

    elif action == "снять":
        amount = int(input("Введите сумму для снятия (кратную 50): "))
        if amount % 50 != 0:
            print("Сумма должна быть кратна 50")
        elif amount > balance:
            print("Недостаточно средств на счете")
        else:
            fee = max(30, min(amount * 0.015, 600))  # расчет комиссии
            balance -= amount + fee
            count += 1
            if count % 3 == 0:  # начисление процентов после каждой третьей операции
                interest = balance * 0.03
                balance += interest
                print("Начислены проценты в размере", interest, "у.е.")

            if balance > 5000000:  # вычитание налога на богатство при превышении 5 млн
                tax = balance * 0.1
                balance -= tax
                print("Вычтен налог на богатство в размере", tax, "у.е.")

    elif action == "выйти":
        print("Спасибо за использование нашего банкомата!")
        break

    else:
        print("Некорректное действие")
