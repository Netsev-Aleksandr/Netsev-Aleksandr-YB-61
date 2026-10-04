print("--- Часть 1: Отбор чисел по условию Варианта 11 ---")
n = int(input("Введите количество чисел (n >= 0): "))
selected_count = 0
selected_sum = 0
for i in range(1, n + 1):
    num = int(input(f"Введите число {i}: "))
    if abs(num) <= 3:
        selected_count += 1
        selected_sum += num
print(f"Количество: {selected_count}, сумма: {selected_sum}")
print("\n--- Часть 2: Проверка простоты числа (дополнительно) ---")
test_num = int(input("Введите целое число для проверки на простоту (n >= 2): "))
is_prime = True
divisor = 2
while divisor * divisor <= test_num:
    if test_num % divisor == 0:
        is_prime = False
        break
    divisor += 1
if is_prime:
    print(f"Число {test_num} — простое")
else:
    print(f"Число {test_num} — составное")
