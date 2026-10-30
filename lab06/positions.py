user_input = input("Введите целые числа одной строкой: ")
if not user_input.strip():
    print("Нет данных")
else:
    numbers = [int(x) for x in user_input.split()]
    if not numbers:
        print("Нет данных")
    else:
        max_val = max(numbers)
        max_indices = [index for index, val in enumerate(numbers) if val == max_val]
        print(max_indices)
