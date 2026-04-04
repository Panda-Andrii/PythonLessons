result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументи повинні бути числами")
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше 100")
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, 0: 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError:
        print("Ділення на нуль!")
    except Exception as e:
        print(f"Тип виключення: {type(e).__name__}: \nСповіщення: {e} ")

print("\nРезультат: ", result)