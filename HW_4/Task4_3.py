# Задача №8 семинара 4
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

a = 5
b = "hello"
c = [1, 2, 3]
d = True
e = "worlds"


def remove_s():
    global a, b, c, d, e
    for var_name in vars().keys():
        if var_name.endswith("s") and var_name != "s":
            var_value = vars()[var_name]
            if isinstance(var_value, str) and len(var_value) > 1:
                var_name_without_s = var_name[:-1]
                vars()[var_name_without_s] = var_value
                vars()[var_name] = None
            elif not isinstance(var_value, str):
                var_name_without_s = var_name[:-1]
                vars()[var_name_without_s] = var_value
                vars()[var_name] = None


remove_s()
print(a, b, c, d, e)
