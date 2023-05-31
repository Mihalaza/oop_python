number = int(input("Cкільки піц замовляєте?"))
cost = float(input("Скільки коштує одна піца?"))
total = number * cost
print("Ціна без знижки", total)
discount = total * 0.1
total = total - discount
print("Знижка 2.1\nЦіна зі знижки 18.9")