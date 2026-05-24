# Задача 4: Рабочий график
# Определение дня недели по номеру и режима работы

# --- Исходные данные ---
day_number = 7  # Номер дня (1-7, где 1 - Понедельник)

# --- Определение дня недели ---
if day_number == 1:
    day_name = "Понедельник"
    is_working = True
elif day_number == 2:
    day_name = "Вторник"
    is_working = True
elif day_number == 3:
    day_name = "Среда"
    is_working = True
elif day_number == 4:
    day_name = "Четверг"
    is_working = True
elif day_number == 5:
    day_name = "Пятница"
    is_working = True
elif day_number == 6:
    day_name = "Суббота"
    is_working = False
elif day_number == 7:
    day_name = "Воскресенье"
    is_working = False
else:
    day_name = "Неизвестный день"
    is_working = False

# --- Определение режима работы ---
if is_working:
    mode = "Рабочий день — 8:00 начало смены"
else:
    mode = "Выходной — Отдых"

# --- Вывод ---
print("=== РАБОЧИЙ ГРАФИК ===")
print(f"День недели: {day_number}")
print(f"Название: {day_name}")
print(f"Режим: {mode}")