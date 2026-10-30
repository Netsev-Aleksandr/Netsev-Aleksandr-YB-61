user_input = input("Введите целые числа одной строкой: ")
if not user_input.strip():
    print("Результат — []")
    print("Количество 0")
    print("Сумма 0")
    print("Сортированная копия []")
    print("Без повторов []")
else:
    numbers = [int(x) for x in user_input.split()]
    matched_numbers = [x for x in numbers if abs(x) <= 3]
    if not matched_numbers:
        print("Результат — []")
        print("Количество 0")
        print("Сумма 0")
        print("Сортированная копия []")
        print("Без повторов []")
    else:
        count = len(matched_numbers)
        total_sum = sum(matched_numbers)
        sorted_copy = sorted(matched_numbers)
        unique_numbers = []
        for num in matched_numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)
        print(f"Результат — {matched_numbers}")
        print(f"Количество {count}")
        print(f"Сумма {total_sum}")
        print(f"Сортированная копия {sorted_copy}")
        print(f"Без повторов {unique_numbers}")
