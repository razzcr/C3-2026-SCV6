"""
Determina si un estudiante puede acceder a una beca estudiantil.

El estudiante obtiene la beca si cumple alguna de estas condiciones:
  1. Promedio >= 80 y asistencia >= 85%.
  2. Pertenece a un programa de apoyo institucional y asistencia >= 75%.

  """


grade_average = float(input("Promedio académico (0-100): "))
attendance_percentage = float(input("Porcentaje de asistencia (0-100): "))
support_program_answer = input("¿Pertenece a un programa de apoyo institucional? (si/no): ").strip().lower()

in_support_program = support_program_answer == "si" or support_program_answer == "sí"
is_valid_answer = in_support_program or support_program_answer == "no"


if grade_average < 0 or grade_average > 100:
    print("Error: el promedio debe estar entre 0 y 100.")
elif attendance_percentage < 0 or attendance_percentage > 100:
    print("Error: la asistencia debe estar entre 0 y 100.")
elif not is_valid_answer:
    print("Error: en el programa de apoyo debe responder 'si' o 'no'.")
else:
    meets_academic_condition = grade_average >= 80 and attendance_percentage >= 85
    meets_support_condition = in_support_program and attendance_percentage >= 75

    if meets_academic_condition or meets_support_condition:
        print("Resultado: el estudiante OBTIENE la beca.")
    else:
        print("Resultado: el estudiante NO OBTIENE la beca.")