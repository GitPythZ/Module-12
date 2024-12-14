import calk


def test_add(a, b):
    if calk.add(5, 5) == 10:
        print("Функция сложение отработала штатно")
    else:
        print("Функция сложения сработала неверно")


test_add(5, 5)
