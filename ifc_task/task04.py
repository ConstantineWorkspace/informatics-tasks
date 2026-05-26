import ifcopenshell

filepath = r"C:\Users\Constantine\Desktop\informatics-tasks\ifc_task\Example_1.ifc"
model = ifcopenshell.open(filepath)

print(f"Схема IFC: {model.schema}")

storeys = model.by_type("IfcBuildingStorey")
print(f"Количество этажей: {len(storeys)}")

for storey in storeys:
    elevation = storey.Elevation if storey.Elevation is not None else "None"
    print(f"Этаж: {storey.Name}, Elevation={elevation}")

print("--- BUILDING FLOORS SUMMARY ---")