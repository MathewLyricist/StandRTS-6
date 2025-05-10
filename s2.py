def f1(x):
    """Вычисляет дробь (x² + 3x + 2) / (x - 5). При x=5 знаменатель = 0 → ошибка."""
    try:
        result = (x ** 2 + 3 * x + 2) / (x - 5)  # Знаменатель = 0 при x=5
        return result
    except ZeroDivisionError:
        print(f"Ошибка в f1(): Деление на ноль. Введите x ≠ 5.")
        return None
    except TypeError:
        print(f"Ошибка в f1(): x должен быть числом.")
        return None


def f2(x, y):
    """Вычисляет (x + y) / z, но z не определена → ошибка."""
    try:
        result = (x + y) / z  # Переменная z не определена → NameError
        return result
    except NameError:
        print(f"Ошибка в f2(): Переменная z не определена.")
        return None
    except TypeError:
        print(f"Ошибка в f2(): x и y должны быть числами.")
        return None


def f3(s):
    """Возвращает длину строки. Если передано не str → ошибка."""
    if not isinstance(s, str):
        print(f"Ошибка в f3(): Ожидается строка, получен {type(s).__name__}.")
        return None
    return len(s)


def f4(numbers):
    """Сравнивает среднее чётных и нечётных чисел из списка."""
    if not isinstance(numbers, (list, tuple)):
        print(f"Ошибка в f4(): Ожидается список или кортеж, получен {type(numbers).__name__}.")
        return None

    try:
        even = [x for x in numbers if x % 2 == 0]
        odd = [x for x in numbers if x % 2 != 0]

        avg_even = sum(even) / len(even) if even else 0
        avg_odd = sum(odd) / len(odd) if odd else 0

        if avg_even > avg_odd:
            return "Среднее чётных больше"
        elif avg_odd > avg_even:
            return "Среднее нечётных больше"
        else:
            return "Средние равны"
    except TypeError:
        print(f"Ошибка в f4(): Список должен содержать только числа.")
        return None


def f5():
    """Считает сумму квадратов чисел [1, 2, 3, 4, 5], но с логической ошибкой (выход за границы списка)."""
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for i in range(len(numbers)):  # Было range(len(numbers) + 1) → IndexError
        total += numbers[i] ** 2
    return total


# Примеры вызовов:
print(f1(5))        # Деление на ноль → None
print(f2(2, 3))     # NameError (z не определена) → None
print(f3("Hello"))  # 5
print(f3(123))      # Ошибка: ожидается строка → None
print(f4([1, 2, 3, 4, 5]))  # Среднее чётных (3) > нечётных (3) → "Средние равны"
print(f5())         # 55 (1 + 4 + 9 + 16 + 25)