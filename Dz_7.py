class IterableGenerator:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        for item in self.data:
            yield item ** 5

my_obj = IterableGenerator([1 , 2, 3, 4, 5])
gen = iter(my_obj)
print(f"Результат ітерації: {list(gen)}")