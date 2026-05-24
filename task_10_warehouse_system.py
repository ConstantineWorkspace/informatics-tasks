# Задача 10: Система учёта склада
# Создание системы учёта материалов с контролем критических остатков

# --- Словарь с вложенными словарями ---
warehouse = {
    "Кирпич":  {"quantity": 5000, "price": 12.50,    "min_quantity": 1000},
    "Цемент":  {"quantity": 120,  "price": 450.00,   "min_quantity": 50},
    "Песок":   {"quantity": 8,    "price": 800.00,   "min_quantity": 10},
    "Арматура":{"quantity": 30,   "price": 48000.00, "min_quantity": 20},
    "Бетон":   {"quantity": 45,   "price": 4200.00,  "min_quantity": 15}
}

# --- Вывод таблицы ---
print("=" * 78)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 78)
print(f"{'Материал':<12} | {'Кол-во':>6} | {'Цена':>8} | {'Мин.':>5} | Стоимость")
print("-" * 78)

for name, data in warehouse.items():
    total = data["quantity"] * data["price"]
    critical = " ⚠ КРИТИЧ!" if data["quantity"] < data["min_quantity"] else ""
    print(f"{name:<12} | {data['quantity']:>6} | {data['price']:>8.2f} | {data['min_quantity']:>5} | {total:.2f}{critical}")
    # --- Общая стоимость ---
total_cost = sum(d["quantity"] * d["price"] for d in warehouse.values())
print("=" * 78)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")

# --- Самый дорогой материал ---
most_expensive = max(warehouse, key=lambda x: warehouse[x]["quantity"] * warehouse[x]["price"])
most_exp_cost = warehouse[most_expensive]["quantity"] * warehouse[most_expensive]["price"]
print(f"Самый дорогой: {most_expensive} ({most_exp_cost:.2f} руб)")
# --- Критические остатки ---
critical = {k: v for k, v in warehouse.items() if v["quantity"] < v["min_quantity"]}
print(f"⚠ КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical)}):")
for name, data in critical.items():
    print(f"  - {name}: {data['quantity']} < {data['min_quantity']}")

# --- Выдача материала со склада ---
print("=== ВЫДАЧА МАТЕРИАЛА ===")
material = "Цемент"
amount = 25
warehouse[material]["quantity"] -= amount
print(f"✓ Выдано {amount} единиц '{material}'")
print(f"Остаток: {warehouse[material]['quantity'] + amount} → {warehouse[material]['quantity']}")