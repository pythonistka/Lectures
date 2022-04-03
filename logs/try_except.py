def foo(a:int, b:int):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except TypeError:
        print('Неверный тип данных (не является числом)')
    else:
        print("Я сработаю если нет ошибок")
    finally:
        print("Я отрабатываю всегда")

foo(1, 9)