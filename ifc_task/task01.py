import ifcopenshell

filepath = r"C:\Users\Constantine\Desktop\informatics-tasks\ifc_task\Example_1.ifc"
model = ifcopenshell.open(filepath)

walls = model.by_type("IfcWall")
print(f"Количество стен в модели: {len(walls)}")