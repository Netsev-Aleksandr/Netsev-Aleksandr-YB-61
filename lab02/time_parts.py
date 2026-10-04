total_seconds = int(input("Введите количество секунд (>= 0): "))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"Результат: {hours} ч {minutes} мин {seconds} с")
