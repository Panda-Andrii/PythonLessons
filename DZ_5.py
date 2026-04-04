import colorama
from colorama import Fore, Back, Style, init
import inspect
import sys

def analyze_module(module):
    print(f"Аналізуємо модуль : {module.__name__}\n")

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

analyze_module(colorama)
init(autoreset=True)
print("*" * 50)
print(len(sys.modules))
print(dir(__builtins__)[:15])
print("*" * 50)
print(Fore.BLUE + "Це синій текст")
print(Back.BLACK + Fore.YELLOW + "Це жовтий текст на чорному фоні")
print(Style.BRIGHT + Fore.GREEN + "Це яскраво зелений текст")
print("А цей текст вже без змін")