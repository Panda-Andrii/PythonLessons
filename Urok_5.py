import math
import inspect
import sys

print(inspect.ismodule(math))
print(inspect.isclass(math))

for name in dir(math):
    print(name)

print ("*" * 50)
for name in dir(math):
    obj = getattr(math, name)

    if inspect.isfunction(obj):
        print(name)

print(math.sqrt(16))
print(inspect.signature(math.sqrt))
print(inspect.getmodule(math.sqrt))

def analyze_module(module):
    import inspect

    print(f"Аналізуємо модуль :  {module.__name__}\n")

    for name in dir(module):
        obj = getattr(module, name)

        if inspect.isclass(obj):
            print(f"Клас: {name}")
        elif callable(obj):
            try:
                sig = inspect.signature(obj)
            except:
                sig = "(невідомо)"

            print(f"Функція: {name} {sig}")

analyze_module(math)
print("*" * 50)
print("Python: ", sys.version)
print("OC: ", sys.platform)
print("Шлях до Python:", sys.executable)
print("*" * 50)
print(len(sys.modules))
print(dir(__builtins__)[:15])
print("*" * 50)
def multiply(a, b=10):
    return a * b
print("Ім'я: ", multiply.__name__)
print("Аргументи: ", inspect.signature(multiply))
print("Код: " )
print(inspect.getsource(multiply))