class MyIterable:
    def __iter__(self):
        # Повертаємо генератор
        return self.generator()

    def generator(self):
        # Генеруємо значення по одному
        yield 1
        yield 2
        yield 3

# Створюємо об'єкт-ітератор
my_iterable = MyIterable()

# Ітеруємося по об'єкту та отримуємо значення з генератора
for value in my_iterable:
    print(value)
