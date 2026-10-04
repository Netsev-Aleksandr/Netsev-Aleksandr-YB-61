last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст в полных годах: "))
favorite_subject = input("Введите любимый предмет: ")
hours_per_week = float(input("Введите количество часов подготовки в неделю: "))
future_age = age + 4
hours_4_weeks = hours_per_week * 4
average_hours_per_day = hours_per_week / 7
print("\n=== КАРТОЧКА СТУДЕНТА ===")
print("Полное имя:", first_name, last_name)
print("Группа:", group)
print("Город:", city)
print("Возраст через 4 года:", future_age)
print("Любимый предмет:", favorite_subject)
print(f"Время подготовки за 4 недели: {hours_4_weeks:.2f} ч.")
print(f"Среднее время подготовки в день: {average_hours_per_day:.2f} ч.")
print("============================")
