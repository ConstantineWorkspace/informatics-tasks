import ifcopenshell

filepath = r"C:\Users\Constantine\Desktop\informatics-tasks\ifc_task\Example_1.ifc"
model = ifcopenshell.open(filepath)

doors = model.by_type("IfcDoor")
min_width = 900  # порог в миллиметрах

wide_doors = [d for d in doors if d.OverallWidth is not None and d.OverallWidth >= min_width]

# Создаём новую модель
new_model = ifcopenshell.file(schema=model.schema)

# Копируем нужные элементы
for element in wide_doors:
    new_model.add(element)

new_model.write("_doors_wide.ifc")
print(f"Подмодель сохранена: _doors_wide.ifc")

# Проверка
check = ifcopenshell.open("_doors_wide.ifc")
print(f"Дверей в подмодели: {len(check.by_type('IfcDoor'))}")