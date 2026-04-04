"""
try:
    x = int(input("Введіть число: "))
    result = 10 / x
except ValueError:
    print("Це не число!")
except ZeroDivisionError:
    print("Ділення на нуль!")
else:
    print(result)
finally:
    print("Виконання програми завершено")


try:
    x = int("abc")
except Exception as e:
    print("Помилка: ", e)


try:
    x= int("100")
except ValueError:
    print("Помилка")
else:
    print("Успішно", x)


def check_age(age):
    if age < 18:
        raise ValueError("Доступ заборонено")
    return age
print(check_age(21))


try:
    x = int("abc")
except (ValueError, TypeError):
    print("Помилка типу або значення")


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Недостатньо коштів")
    return balance - amount
try:
    print(withdraw(300, 200))
except ValueError as e:
    print(e)


def add(n1, n2): return n1 + n2
def sub(n1, n2): return n1 - n2
def mul(n1, n2): return n1 * n2
def div(n1, n2): return n1 / n2

print("Виберіть операцію: \n1. Додавання \n2. Віднімання \n3. Множення \n4. Ділення")
choice = input("Виберіть (1/2/3/4): ")

try:
    num1 = float(input("Напишіть перше число: "))
    num2 = float(input("Напишіть друге число: "))
except ValueError:
    print("Тільки числа записуйте!")
    exit()
except ZeroDivisionError:
    print("Ділення на нуль не можна!")

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {sub(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {mul(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {div(num1, num2)}")
else:
    print("Неправильне число")


def choice_check():
    print("Поділити числа - 1 \nВихід - 2")
    choice = input("Ваш вибір: ")

    if choice == '1':
        try:
            a = int(input("Введіть перше число: "))
            b = int(input("Введіть друге число: "))
            result = a / b
        except ValueError:
            print("Це не число!")
        except ZeroDivisionError:
            print("Ділення на нуль!")
        else:
            print(f"Результат: {result}")
        finally:
            print("Виконання програми завершено")
    elif choice == '2':
        exit()
    else:
        print("Неправильний вибір, вихід автоматично")
        exit()


choice_check()
"""

import warnings
warnings.warn("Це попередження", UserWarning)

warnings.filterwarnings("ignore")
warnings.warn("Не буде показано!")

try:
    with open("itstep.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не знайдений!")