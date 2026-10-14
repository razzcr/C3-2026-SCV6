# Curso: SOFT-01 Principios de Programación 1 (SCV6)
# Archivo: ejercicio3_soporte_tripulacion.py
# Integrantes: Carlos Esteban Monge Barquero
# Fecha: 2026-10-14
# Versión: 1.0
# Descripción: Determina si la nave posee oxígeno y provisiones suficientes para sostener a la tripulación durante la misión.
# Repo: https://github.com/razzcr/C3-2026-SCV6/tree/main/mision-orbita

# Lectura de datos
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# Cálculos / validación
print("=" * 50)
print("          REPORTE DE SOPORTE A LA TRIPULACIÓN")
print("=" * 50)
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    # Salida
    print("La nave posee recursos suficientes para la tripulación.")
else:
    # Salida
    print("La nave no posee recursos suficientes para la tripulación.")
print("=" * 50)
