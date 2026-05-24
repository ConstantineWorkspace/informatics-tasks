# Задача 5: Калькулятор скидки
# Расчёт стоимости покупки с прогрессивной системой скидок

# --- Исходные данные ---
price = 1500.0   # Цена за единицу товара в рублях
quantity = 3     # Количество товара

# --- Вычисления ---
total = price * quantity  # Общая сумма без скидки

# --- Определение скидки ---
if total < 1000:
    discount_percent = 0
elif total <= 5000:
    discount_percent = 5
else:
    discount_percent = 10

# --- Расчёт итоговой суммы ---
discount_amount = round(total * discount_percent / 100, 2)  # Сумма скидки
final_price = round(total - discount_amount, 2)             # Итоговая сумма

# --- Вывод ---
print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена за единицу: {price} руб.")
print(f"Количество: {quantity} шт.")
print(f"Сумма без скидки: {total:.2f} руб.")
print(f"Скидка: {discount_percent}% ({discount_amount} руб.)")
print(f"Итоговая сумма: {final_price} руб.")