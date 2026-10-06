# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Carlos Apellido, Integrante 2, Integrante 3
# Fecha: 01/10/2026        Versión: 1.0
# Descripción: Verifica si la nave posee suficiente combustible (condicional simple).
# ============================================================

# ----- Declaración de constantes -----
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO_ADICIONAL = 10  # por debajo de este margen se advierte

# ----- Entrada de datos -----
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para el viaje de ida: "))
combustible_regreso = int(input("Combustible requerido para el viaje de regreso: "))

# ----- Procesamiento -----
# El total incluye el regreso: llegar al destino no es suficiente.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# ----- Salida de resultados (siempre se muestra) -----
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# ----- Decisión (condicional simple, sin else) -----
# Un adicional negativo (combustible insuficiente) también es menor que el margen.
if combustible_adicional < MARGEN_MINIMO_ADICIONAL:
    print("Advertencia: el margen adicional de combustible es bajo.")
