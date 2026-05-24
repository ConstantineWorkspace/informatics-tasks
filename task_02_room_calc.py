# Задача 2: Параметры помещения
# Расчёт геометрических параметров и стоимости покраски стен

# --- Исходные данные ---
length = 6.0    # Длина помещения в метрах
width = 4.0     # Ширина помещения в метрах
height = 3.0    # Высота помещения в метрах

paint_price = 125  # Стоимость покраски руб/м²

# --- Вычисления ---
floor_area = length * width                              # Площадь пола
wall_area = 2 * (length + width) * height               # Площадь стен
volume = length * width * height                        # Объём помещения
paint_cost = round(wall_area * paint_price, 2)          # Стоимость покраски

# --- Вывод ---
print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Длина: {length} м")
print(f"Ширина: {width} м")
print(f"Высота: {height} м")
print()
print(f"Площадь пола:  {round(floor_area, 2)} м²")
print(f"Площадь стен:  {round(wall_area, 2)} м²")
print(f"Объём:         {round(volume, 2)} м³")
print()
print(f"Стоимость покраски: {paint_cost} руб.")