# Write your code here!
def employee_print(employee_info):
    # Obtener valores base
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    # Copia del diccionario para no modificar el original
    extra_info = employee_info.copy()

    # Eliminar claves base
    extra_info.pop("Name", None)
    extra_info.pop("Salary", None)
    extra_info.pop("Role", None)

    if extra_info:
        for key, value in extra_info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")