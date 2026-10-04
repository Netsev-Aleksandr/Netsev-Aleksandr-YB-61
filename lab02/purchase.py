price = int(input("Введите цену одной тетради в целых рублях: "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите переданную сумму денег: "))
total_cost = price * count
change = paid - total_cost
print(f"Стоимость покупки: {total_cost} руб.")
print(f"Сдача: {change} руб.")
