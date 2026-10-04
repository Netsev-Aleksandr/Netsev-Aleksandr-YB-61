rejected_attempts = 0
while True:
    num = int(input("Введите целое положительное число: "))
    if num > 0:
        break
    rejected_attempts += 1
print(f"Квадрат {num ** 2}, отклонено {rejected_attempts}")
