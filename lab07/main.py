from functions import sum_digits, average, normalize_text, select_numbers, is_palindrome


def main():
    print("--- Тестирование функции sum_digits ---")
    user_num = int(input("Введите целое число: "))
    print(f"Сумма цифр его модуля: {sum_digits(user_num)}")
    print("\n--- Тестирование функции average и select_numbers ---")
    list_input = input("Введите целые числа через пробел: ")
    numbers_list = [int(x) for x in list_input.split()] if list_input.strip() else []
    avg_res = average(numbers_list)
    print(f"Среднее арифметическое: {f'{avg_res:.2f}' if avg_res is not None else 'Нет данных'}")
    thresh_input = input("Введите порог: ")
    threshold = int(thresh_input)
    print(f"Результат отбора (модуль равен {threshold}): {select_numbers(numbers_list, threshold)}")
    print("\n--- Тестирование функции normalize_text ---")
    user_text = input("Введите произвольный текст: ")
    print(f"Нормализованный текст: \"{normalize_text(user_text)}\"")
    print("\n--- Тестирование доп. задания (is_palindrome) ---")
    pal_text = input("Введите текст для проверки на палиндром: ")
    if is_palindrome(pal_text):
        print("Результат: Палиндром (True)")
    else:
        print("Результат: Не палиндром или пустая строка (False)")


if __name__ == "__main__":
    main()
