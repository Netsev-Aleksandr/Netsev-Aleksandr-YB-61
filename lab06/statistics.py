user_input = input("Введите целые числа одной строкой: ")
if not user_input.strip():
    print("Нет данных")
else:
    numbers = [int(x) for x in user_input.split()]
    if not numbers:
        print("Нет данных")
    else:
        count = 0
        total_sum = 0
        minimum = numbers[0]
        maximum = numbers[0]
        for num in numbers:
            count += 1
            total_sum += num
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
        average = total_sum / count
        print(f"Количество: {count}")
        print(f"Сумма: {total_sum}")
        print(f"Минимум: {minimum}")
        print(f"Максимум: {maximum}")
        print(f"Среднее: {average:.2f}")
