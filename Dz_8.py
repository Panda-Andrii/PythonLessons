import time
import unittest
import random

waiter_add_function = random.randint(1, 3)
waiter_simple_function = random.randint(1, 3)

def execution_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Функція '{func.__name__}' працювала {end_time - start_time:.6f} сек.")
        return result
    return wrapper

@execution_timer
def slow_function():
    time.sleep(1)
    return "Готово!"

class TestTimer(unittest.TestCase):
    def test_function_returns_value(self):
        @execution_timer
        def add(a, b):
            time.sleep(waiter_add_function)
            return a + b
        self.assertEqual(add(2, 3), 5)

    def test_execution(self):
        @execution_timer
        def simple():
            time.sleep(waiter_simple_function)
            return True

        self.assertTrue(simple())

if __name__ == '__main__':
    unittest.main()