import ifcopenshell
import ifcopenshell.util.element

filepath = r"C:\Users\Constantine\Desktop\informatics-tasks\ifc_task\Example_1.ifc"
model = ifcopenshell.open(filepath)

doors = model.by_type("IfcDoor")
min_width = 900  # порог в миллиметрах

narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)
    
    if width is not None and width < min_width:
        narrow_doors.append((name, width, height))

if narrow_doors:
    for name, width, height in narrow_doors:
        print(f"{name}: ширина = {round(width, 3)}, высота = {round(height, 3)}")
    print(f"Всего узких дверей: {len(narrow_doors)}")
else:
    print("Узких дверей не обнаружено")