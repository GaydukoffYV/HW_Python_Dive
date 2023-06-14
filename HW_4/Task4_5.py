# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.
def kwargs_to_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if not hash(key):
            key = str(key)
        result_dict[value] = key
    return result_dict


result = kwargs_to_dict(first_name='John', last_name='Doe', age=30)
print(result)
