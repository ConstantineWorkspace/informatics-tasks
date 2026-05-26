import ifcopenshell
import ifcopenshell.util.element

filepath = r"C:\Users\Constantine\Desktop\informatics-tasks\ifc_task\Example_1.ifc"
model = ifcopenshell.open(filepath)

walls = model.by_type("IfcWall")
first_wall = walls[0]

psets = ifcopenshell.util.element.get_psets(first_wall)
print("Все наборы свойств (полный словарь):")
print(psets)
print()

for pset_name, properties in psets.items():
    print(f"Pset: {pset_name}")
    for prop_name, prop_value in properties.items():
        print(f"  {prop_name}: {prop_value}")