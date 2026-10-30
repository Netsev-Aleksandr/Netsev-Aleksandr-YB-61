def sum_digits(number: int) -> int:
    n = abs(number)
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum


def average(numbers: list) -> float | None:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text: str) -> str:
    return " ".join(text.split()).lower()


def select_numbers(numbers: list, threshold: int) -> list:
    return [x for x in numbers if abs(x) == threshold]


def is_palindrome(text: str) -> bool:
    cleaned_text = text.lower().replace(" ", "")
    if not cleaned_text:
        return False
    return cleaned_text == cleaned_text[::-1]
