print("--- Основное задание: Заполненность парковки ---")
value = int(input("Введите целое число от 0 до 100: "))
if value < 0 or value > 100:
    print("Ошибка диапазона")
else:
    if 0 <= value <= 59:
        print("Много мест")
    elif 60 <= value <= 89:
        print("Мало мест")
    elif 90 <= value <= 100:
        print("Почти занята")
print("\n--- Дополнительное задание: Високосный год ---")
year = int(input("Введите год от 1 до 9999: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("да")
else:
    print("нет")
