import ifcopenshell
import ifcopenshell.util.element

filepath = r"C:\Users\Constantine\Desktop\informatics-tasks\ifc_task\Example_1.ifc"
model = ifcopenshell.open(filepath)

walls = model.by_type("IfcWall")
first_wall = walls[0]

print(f"Исходное Name: {first_wall.Name}")
print(f"Исходное ObjectType: {first_wall.ObjectType}")

# Изменяем имя
first_wall.Name = "MODIFIED_" + (first_wall.Name or "Wall")

# Изменяем свойство в Pset_WallCommon
for rel in model.by_type("IfcRelDefinesByProperties"):
    if first_wall in rel.RelatedObjects:
        pset = rel.RelatingPropertyDefinition
        if hasattr(pset, "Name") and pset.Name == "Pset_WallCommon":
            for prop in pset.HasProperties:
                if prop.Name == "IsExternal":
                    prop.NominalValue = model.create_entity("IfcBoolean", True)

model.write("modified.ifc")
print("Файл сохранён как modified.ifc")

# Проверка
model2 = ifcopenshell.open("modified.ifc")
walls2 = model2.by_type("IfcWall")
print(f"Обновлённое Name: {walls2[0].Name}")