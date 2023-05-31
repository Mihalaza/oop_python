result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except ValueError:
        print(f"ValueError: a ({a}) має бути більше або дорівнювати b ({b})")
    except IndexError:
        print(f"IndexError: b ({b}) має бути менше або дорівнювати 100")

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
'''В цьому коды я використовував 
   конструкцію try-except для перехоплення
   винятків ValueError і IndexError. У випадку
   виникнення винятку, програма виводить 
   відповідне повідомлення у консоль. Результати
   обчислень також будуть додані до списку result 
   і надруковані після завершення циклу.'''