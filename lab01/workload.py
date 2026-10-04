subject1 = input("Введите название первого предмета: ")
lessons1 = int(input("Количество занятий в неделю по первому предмету: "))
duration1 = int(input("Продолжительность одного занятия (в минутах): "))
subject2 = input("Введите название второго предмета: ")
lessons2 = int(input("Количество занятий в неделю по второму предмету: "))
duration2 = int(input("Продолжительность одного занятия (в минутах): "))
available_hours = float(input("Введите доступное время на неделю в часах: "))
minutes_subj1 = lessons1 * duration1
minutes_subj2 = lessons2 * duration2
total_minutes = minutes_subj1 + minutes_subj2
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
total_minutes_4_weeks = total_minutes * 4
total_hours_4_weeks = total_hours * 4
print("\n=== РАСЧЕТ УЧЕБНОЙ НАГРУЗКИ ===")
print(f"Время на предмет '{subject1}': {minutes_subj1} мин.")
print(f"Время на предмет '{subject2}': {minutes_subj2} мин.")
print(f"Общая нагрузка за неделю: {total_minutes} мин. ({total_hours:.2f} ч.)")
print(f"Остаток свободного времени: {free_hours:.2f} ч.")
print(f"Общая нагрузка за 4 недели: {total_minutes_4_weeks} мин. ({total_hours_4_weeks:.2f} ч.)")
print("=================================")
