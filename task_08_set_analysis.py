# Задача 8: Анализ заказов
# Использование множеств для анализа материалов трёх подрядчиков

# --- Списки материалов трёх подрядчиков ---
contractor1 = {"Кирпич", "Цемент", "Штукатурка", "Арматура", "Краска"}
contractor2 = {"Цемент", "Бетон", "Гипс", "Краска", "Утеплитель"}
contractor3 = {"Песок", "Бетон", "Утеплитель", "Брус", "Цемент"}

print("=== АНАЛИЗ ЗАКАЗОВ ПОДРЯДЧИКОВ ===")
print(f"Подрядчик 1: {contractor1}")
print(f"Подрядчик 2: {contractor2}")
print(f"Подрядчик 3: {contractor3}")
# --- Все уникальные материалы ---
all_materials = contractor1 | contractor2 | contractor3
print(f"\nВсе уникальные материалы: {all_materials}")

# --- Общие для всех трёх ---
common_all = contractor1 & contractor2 & contractor3
print(f"Общие для всех: {common_all}")

# --- Только у первого подрядчика ---
only_first = contractor1 - contractor2 - contractor3
print(f"Только у первого: {only_first}")

# --- Ровно у двух подрядчиков ---
two_contractors = (contractor1 & contractor2) | (contractor1 & contractor3) | (contractor2 & contractor3)
two_contractors = two_contractors - common_all
print(f"Ровно у двух: {two_contractors}")