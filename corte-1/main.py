from student_list import StudentList
from subject_list import SubjectList

def register_subject():
    name = input("Nombre de la asignatura: ")
    credits = int(input("Número de créditos: "))
    credit_cost = float(input("Costo por crédito: "))
    semester = int(input("Semestre (1 o 2): "))
    return {
        "name": name,
        "credits": credits,
        "credit_cost": credit_cost,
        "semester": semester,
        "students": StudentList()
    }

def register_student(subject):
    name = input("Nombre del estudiante: ")
    gender = input("Género (M/F): ")
    age = int(input("Edad: "))
    stratum = int(input("Estrato (1-6): "))
    student = {"name": name, "gender": gender, "age": age, "stratum": stratum}
    subject["students"].add_student(student)

def calculate_revenue(subject):
    discounts = {1: 0.5, 2: 0.3, 3: 0.1}
    total = 0
    for student in subject["students"].iterate():
        discount = discounts.get(student["stratum"], 0)
        total += (subject["credit_cost"] * subject["credits"]) * (1 - discount)
    return total

def count_students_by_stratum(subject, stratum):
    return subject["students"].count_by_stratum(stratum)

def show_information(subjects):
    if not subjects.head:
        print("No hay asignaturas registradas.")
        return

    for subject in subjects.iterate():
        student_count = sum(1 for _ in subject["students"].iterate())
        print(f"Asignatura: {subject['name']}, Estudiantes Matriculados: {student_count}")

    max_subject = None
    max_revenue = -1
    for subject in subjects.iterate():
        revenue = calculate_revenue(subject)
        if revenue > max_revenue:
            max_revenue = revenue
            max_subject = subject
    if max_subject:
        print(f"Asignatura con mayor recaudación: {max_subject['name']} (${max_revenue:.2f})")

    total_credit_cost = sum(subject['credit_cost'] for subject in subjects.iterate())
    total_subjects = sum(1 for _ in subjects.iterate())
    avg_credit_cost = total_credit_cost / total_subjects if total_subjects else 0
    print(f"Promedio del costo de créditos: ${avg_credit_cost:.2f}")

    stratum = int(input("Ingrese el estrato para calcular descuentos (1-3): "))
    total_discount = 0
    for subject in subjects.iterate():
        for student in subject["students"].iterate():
            if student["stratum"] == stratum:
                discount = {1: 0.5, 2: 0.3, 3: 0.1}.get(stratum, 0)
                total_discount += (subject["credit_cost"] * subject["credits"]) * discount
    print(f"Total de descuentos otorgados para estrato {stratum}: ${total_discount:.2f}")

    for subject in subjects.iterate():
        count = count_students_by_stratum(subject, 1)
        print(f"Estudiantes de estrato 1 en {subject['name']}: {count}")

    total_revenue = sum(calculate_revenue(subject) for subject in subjects.iterate())
    print(f"Valor total recaudado entre todas las asignaturas: ${total_revenue:.2f}")

def show_semester_info(subjects):
    semester = int(input("Ingrese el semestre que quiere consultar (1-2): "))
    stratum = int(input("Ingrese el estrato para calcular descuentos (1-3): "))

    sum_semester = 0
    total_discount_semester = 0

    for subject in subjects.iterate():
        if subject["semester"] == semester:
            sum_semester += subject["credit_cost"]
            for student in subject["students"].iterate():
                if student["stratum"] == stratum:
                    discount = {1: 0.5, 2: 0.3, 3: 0.1}.get(stratum, 0)
                    total_discount_semester += (subject["credit_cost"] * subject["credits"]) * discount

    print(f"Los costos del semestre {semester} son: {sum_semester}")
    print(f"Total de descuentos aplicados para estrato {stratum}: {total_discount_semester}")

def main():
    subjects = SubjectList()

    while True:
        print("\n--- Menú ---")
        print("1. Registrar asignatura")
        print("2. Registrar estudiante en una asignatura")
        print("3. Mostrar información")
        print("4. Mostrar información por semestre")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            subjects.add_subject(register_subject())
        elif option == "2":
            if not subjects.head:
                print("No hay asignaturas registradas.")
            else:
                subject_list = list(subjects.iterate())
                for i, subject in enumerate(subject_list, 1):
                    print(f"{i}. {subject['name']}")
                try:
                    index = int(input("Seleccione la asignatura: ")) - 1
                    if 0 <= index < len(subject_list):
                        register_student(subject_list[index])
                    else:
                        print("Opción inválida.")
                except ValueError:
                    print("Entrada inválida.")
        elif option == "3":
            show_information(subjects)
        elif option == "4":
            show_semester_info(subjects)
        elif option == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
