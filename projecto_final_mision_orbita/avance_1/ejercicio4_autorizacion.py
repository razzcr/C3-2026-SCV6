# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Carlos Apellido, Integrante 2, Integrante 3
# Fecha: 01/10/2026        Versión: 1.0
# Descripción: Autoriza o rechaza el lanzamiento según los cuatro recursos.
# ============================================================

# ----- Declaración de constantes -----
RESERVA_COMBUSTIBLE = 10

# ----- Entrada de datos -----
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
energia_disponible = int(input("Energía disponible: "))
energia_requerida = int(input("Energía requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# ----- Procesamiento -----
# Se exige combustible para ida, regreso y reserva desde el lanzamiento.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# ----- Decisión (condición compuesta, sin condicionales anidados) -----
if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
