import logging
import unittest

"""
print("Програма успішно запущена!")

logging.basicConfig(level=logging.INFO)
logging.info("Програма успішно запущена!")

# Повідомлення про помилку
logging.basicConfig(level=logging.ERROR)

age = 5
if age < 0:
    logging.error("Вік не може бути від'ємним!")

logging.basicConfig(filename="test.log", level=logging.INFO)
logging.info("Старт програми")
logging.warning("Мало пам'яті")
logging.error("Помилка підключення")

# Лог + try/except
logging.basicConfig(level=logging.ERROR)
try:
    x = int("555")
except ValueError:
    logging.error("Неможливо перетворити рядок у число")
else:
    print(f"x = {x}")

logging.basicConfig(level=logging.ERROR)
try:
    5 / 0
except Exception:
    logging.exception("Щось пішло не так!")

result = 10 + 5
assert result == 15, "Розрахунок правильний!"

def square(x):
    return x * x

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(5), 25)
if __name__ == "__main__":
    unittest.main()

def square(x):
    return x * x

class TestSquare(unittest.TestCase):
    def test_zeo(self):
        self.assertEqual(square(0), 0)

    def test_negative_zeo(self):
        self.assertEqual(square(-3), 9)

def divide(a, b):
    return a / b

class TestDivide(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5,0)
"""
def check_age(age):
    if age < 0:
        raise ValueError("Некоректний вік")

class TestAge(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(check_age(18), 18)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            check_age(-5)
