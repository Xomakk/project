def save_result(func):
    def wrapper(*args):
        result = func(*args)
        file = open("results.txt", "a")
        file.write(f"{result}\n")
        file.close()
        return result
    return wrapper


@save_result
def calculate(a, b, operation='+'):
    """
        Получает на вход два числа и операцию.
        Возвращает результат указанной операции с передаными числами.
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "ОШИБКА: Деление на ноль."
        return a / b
    elif operation == '**':
        return a ** b
    else:
        print('Указанная операция не распознана.')
        return None

calculate(1, 2)
calculate(2, 2, "-")
calculate(3, 2, "**")