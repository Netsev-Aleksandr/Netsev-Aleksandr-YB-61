text = input("Введите строку: ")
if not text.strip():
    print("Нет совпадений")
    print("Количество 0")
else:
    raw_words = text.split()
    matched_words = []
    for word in raw_words:
        cleaned = word.strip(".,!?;:").lower()
        if not cleaned:
            continue
        if 3 <= len(cleaned) <= 5:
            matched_words.append(cleaned)
    if matched_words:
        for w in matched_words:
            print(w)
        print(f"Общее количество: {len(matched_words)}")
    else:
        print("Нет совпадений")
        print("Количество 0")
