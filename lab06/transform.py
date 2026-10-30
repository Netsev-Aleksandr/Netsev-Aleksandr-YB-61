user_input = input("Введите целые числа одной строкой: ")
original_list = [int(x) for x in user_input.split()]
transformed_list = [abs(x) for x in original_list]
print(f"Исходный список: {original_list}")
print(f"Новый список: {transformed_list}")
