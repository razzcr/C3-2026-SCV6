# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Carlos Apellido, Integrante 2, Integrante 3
# Fecha: 01/10/2026        Versión: 1.0
# Descripción: Verifica si hay oxígeno y provisiones suficientes (condicional doble).
# ============================================================

# ----- Entrada de datos -----
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# ----- Decisión -----
# Ambos recursos deben cumplirse a la vez; por eso se usa "and" y >= (igual alcanza).
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
