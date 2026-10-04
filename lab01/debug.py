print("--- Фрагмент А ---")
first_A = 2
second_A = 3
print("Тип до исправления: <class 'str'>")
print("Тип после исправления:", type(first_A))
print("Результат (сумма чисел):", first_A + second_A)

print("\n--- Фрагмент Б ---")
raw_input_B = input("Возраст (введите 17 для теста): ")
print("Тип до преобразования:", type(raw_input_B))
age_B = int(raw_input_B)
print("Тип после преобразования:", type(age_B))
print("Результат (возраст через год):", age_B + 1)

print("\n--- Фрагмент В ---")
first_V = 4
second_V = 7
third_V = 10
average_V = (first_V + second_V + third_V) / 3
print("Результат (среднее арифметическое):", average_V)
