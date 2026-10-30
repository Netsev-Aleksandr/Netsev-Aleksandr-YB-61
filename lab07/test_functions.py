from functions import sum_digits, average, normalize_text, select_numbers, is_palindrome

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ    Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")
test_list = [-5, 0, 2, 5]
assert select_numbers(test_list, 2) == [2]
assert select_numbers([], 2) == []
border_list = [3, -3, 3, 4, -2, 0]
assert select_numbers(border_list, 3) == [3, -3, 3]
backup_list = [-5, 0, 2, 5]
select_numbers(backup_list, 2)
assert backup_list == [-5, 0, 2, 5]
actual_avg = average([1, 2, 4])
expected_avg = 2.3333333333333335
assert abs(actual_avg - expected_avg) < 1e-9
assert is_palindrome("А роза упала на лапу Азора") == True
assert is_palindrome("Привет") == False
assert is_palindrome("   ") == False
assert is_palindrome("") == False
assert is_palindrome("А!") == False
print("Индивидуальные проверки пройдены")
