order_name = input("Введите название заказа (например, Магазин растений): ")
customer_name = input("Введите имя заказчика: ")
print("\n--- Первая позиция ---")
item1_name = "Саженцы"
print(f"Позиция: {item1_name}")
item1_count = int(input(f"Количество ({item1_name}): "))
item1_price = float(input(f"Цена за единицу ({item1_name}) в рублях: "))
print("\n--- Вторая позиция ---")
item2_name = "Горшки"
print(f"Позиция: {item2_name}")
item2_count = int(input(f"Количество ({item2_name}): "))
item2_price = float(input(f"Цена за единицу ({item2_name}) в рублях: "))
print("\n--- Скидка и Доставка ---")
discount_percent = float(input("Введите скидку на товары в процентах (от 0 до 100): "))
delivery_cost = float(input("Введите стоимость доставки в рублях: "))
amount_paid = float(input("Введите внесённую сумму денег в рублях: "))
item1_total = item1_count * item1_price
item2_total = item2_count * item2_price
items_subtotal = item1_total + item2_total
discount_rub = items_subtotal * (discount_percent / 100)
items_with_discount = items_subtotal - discount_rub
total_with_delivery = items_with_discount + delivery_cost
total_items_count = item1_count + item2_count
change = amount_paid - total_with_delivery
print("\n========================================")
print(f"ЗАКАЗ: {order_name}")
print(f"Заказчик: {customer_name}")
print("========================================")
print(f"{item1_name} | {item1_count} шт. | {item1_price:.2f} руб. | {item1_total:.2f} руб.")
print(f"{item2_name} | {item2_count} шт. | {item2_price:.2f} руб. | {item2_total:.2f} руб.")
print("----------------------------------------")
print(f"Общее количество предметов: {total_items_count} шт.")
print(f"Стоимость товаров до скидки: {items_subtotal:.2f} руб.")
print(f"Размер скидки ({discount_percent}%): {discount_rub:.2f} руб.")
print(f"Стоимость товаров со скидкой: {items_with_discount:.2f} руб.")
print(f"Стоимость доставки (без скидки): {delivery_cost:.2f} руб.")
print(f"НОВАЯ ИТОГОВАЯ СУММА К ОПЛАТЕ: {total_with_delivery:.2f} руб.")
print(f"Внесено покупателем: {amount_paid:.2f} руб.")
print(f"СДАЧА: {change:.2f} руб.")
print("========================================")
