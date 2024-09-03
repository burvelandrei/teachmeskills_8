def calculator():
    """Функция для выполнения математических операций (сложение/вычитание/умножение/деление) \
наподобии калькулятора."""
    try:
        number_1 = float(input("Введите первое число: "))
        number_2 = float(input("Введите второе число: "))
    except ValueError:
        print("Вы ввели не число!")
        return
    else:
        operation = input(
            "Введите операцию (сложение/вычитание/умножение/деление или + - * /): "
        ).lower()

    print("-" * 30)
    if operation == "сложение" or operation == "+":
        print(f"Результат сложения = {float(number_1 + number_2)}")
    elif operation == "вычитание" or operation == "-":
        print(f"Результат вычитания = {float(number_1 - number_2)}")
    elif operation == "умножение" or operation == "*":
        print(f"Результат умножения = {float(number_1 * number_2)}")
    elif operation == "деление" or operation == "/":
        try:
            print(f"Результат деления = {number_1/number_2}")
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
    else:
        print("Такой операции нет!")


calculator()
