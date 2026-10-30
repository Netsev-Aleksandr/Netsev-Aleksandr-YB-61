text = input("Введите текст: ")
cleaned_text = text.lower().replace(" ", "")
if not cleaned_text:
    print("Нет текста")
else:
    # СПОСОБ 1: Через обратный срез
    if cleaned_text == cleaned_text[::-1]:
        res_slice = "Палиндром"
    else:
        res_slice = "Не палиндром"
    # СПОСОБ 2: Через цикл (без обратного среза)
    is_palindrome_loop = True
    n = len(cleaned_text)
    for i in range(n // 2):
        if cleaned_text[i] != cleaned_text[n - 1 - i]:
            is_palindrome_loop = False
            break
    if is_palindrome_loop:
        res_loop = "Палиндром"
    else:
        res_loop = "Не палиндром"
    print(f"Способ со срезом: {res_slice}")
    print(f"Способ с циклом: {res_loop}")
    if res_slice == res_loop:
        print("Результаты обоих способов совпали")
    else:
        print("Ошибка: результаты различаются")
