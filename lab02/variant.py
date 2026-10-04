import math

total_pages = int(input("Введите общее количество страниц: "))
capacity = int(input("Введите количество страниц в одной тетради: "))
full_units = total_pages // capacity
remainder = total_pages % capacity
total_units = (total_pages + capacity - 1) // capacity
total_units = total_units * (total_pages > 0)
radius = float(input("Введите положительный радиус окружности: "))
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)
print("\n=== РЕЗУЛЬТАТЫ ВАРИАНТА 11 ===")
print(f"Полных единиц: {full_units}")
print(f"Остаток: {remainder}")
print(f"Всего единиц: {total_units}")
print("\n--- Дополнительное задание ---")
print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь круга: {area:.2f}")
print("==============================")
