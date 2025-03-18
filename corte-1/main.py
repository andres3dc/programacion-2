def register_subject():
    name = input("Ingrese el nombre de la asignatura: ")
    while True:
        try:
            credits = int(input("Ingrese la cantidad de créditos: "))
            credit_cost = float(input("Ingrese el costo por crédito: "))
            if credits > 0 and credit_cost > 0:
                break
            else:
                print("Los valores deben ser positivos.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    return {"name": name, "credits": credits, "credit_cost": credit_cost, "students": []}

def register_student(subject):
    name = input("Ingrese el nombre del estudiante: ")
    gender = input("Ingrese el género del estudiante: ")
    while True:
        try:
            age = int(input("Ingrese la edad del estudiante: "))
            stratum = int(input("Ingrese el estrato del estudiante (1-3): "))
            if age > 0 and stratum in (1, 2, 3):
                break
            else:
                print("Edad debe ser positiva y estrato debe ser 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    student = {"name": name, "gender": gender, "age": age, "stratum": stratum}
    subject["students"].append(student)

def calculate_revenue(subject):
    discounts = {1: 0.5, 2: 0.3, 3: 0.1}
    total = 0
    for student in subject["students"]:
        discount = discounts.get(student["stratum"], 0)
        total += (subject["credit_cost"] * subject["credits"]) * (1 - discount)
    return total

def count_students_by_stratum(subject, stratum):
    return sum(1 for student in subject["students"] if student["stratum"] == stratum)

def show_information(subjects):
    if not subjects:
        print("No hay asignaturas registradas.")
        return
    
    for subject in subjects:
        print(f"Asignatura: {subject['name']}, Estudiantes Matriculados: {len(subject['students'])}")
    
    max_revenue_subject = max(subjects, key=calculate_revenue)
    print(f"Asignatura con mayor recaudación: {max_revenue_subject['name']} (${calculate_revenue(max_revenue_subject):.2f})")
    
    avg_credit_cost = sum(subject['credit_cost'] for subject in subjects) / len(subjects)
    print(f"Promedio del costo de créditos: ${avg_credit_cost:.2f}")
    
    stratum = int(input("Ingrese el estrato para calcular descuentos (1-3): "))
    total_discount = sum(
        (subject['credit_cost'] * subject['credits']) * {1: 0.5, 2: 0.3, 3: 0.1}.get(student['stratum'], 0)
        for subject in subjects for student in subject['students'] if student['stratum'] == stratum
    )
    print(f"Total de descuentos otorgados para estrato {stratum}: ${total_discount:.2f}")
    
    for subject in subjects:
        print(f"Estudiantes de estrato 1 en {subject['name']}: {count_students_by_stratum(subject, 1)}")
    
    total_revenue = sum(calculate_revenue(subject) for subject in subjects)
    print(f"Valor total recaudado entre todas las asignaturas: ${total_revenue:.2f}")

def main():
    subjects = []
    while True:
        print("\nMenú:")
        print("1. Registrar asignatura")
        print("2. Registrar estudiante en una asignatura")
        print("3. Mostrar información del sistema")
        print("4. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            subjects.append(register_subject())
        elif option == "2":
            if not subjects:
                print("No hay asignaturas registradas.")
            else:
                for i, subject in enumerate(subjects, 1):
                    print(f"{i}. {subject['name']}")
                try:
                    index = int(input("Seleccione la asignatura: ")) - 1
                    if 0 <= index < len(subjects):
                        register_student(subjects[index])
                    else:
                        print("Opción inválida.")
                except ValueError:
                    print("Entrada inválida.")
        elif option == "3":
            show_information(subjects)
        elif option == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
