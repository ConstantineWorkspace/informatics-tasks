import ifcopenshell

filepath = r"C:\Users\Constantine\Desktop\informatics-tasks\ifc_task\Example_1.ifc"
model = ifcopenshell.open(filepath)

walls = model.by_type("IfcWall")
print(f"Количество стен в модели: {len(walls)}")

first_wall = walls[0]
print(f"GlobalId: {first_wall.GlobalId}")
print(f"Name: {first_wall.Name}")
print(f"ObjectType: {first_wall.ObjectType}")