# Curso: SOFT-01 Principios de Programación 1 (SCV6)
# Archivo: ejercicio2_combustible.py
# Integrantes: Carlos Esteban Monge Barquero
# Fecha: 2026-10-04
# Versión: 1.0
# Descripción: Verifica si el combustible disponible alcanza para el viaje de ida y regreso más la reserva de emergencia, e informa el margen disponible.
# Repo: https://github.com/razzcr/C3-2026-SCV6/tree/main/mision-orbita

RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO_ADICIONAL = 10

# Lectura de datos
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para el viaje de ida: "))
combustible_regreso = int(input("Combustible requerido para el viaje de regreso: "))

# Cálculos
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# Salida
print("=" * 50)
print("          REPORTE DE COMBUSTIBLE")
print("=" * 50)
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

print("=" * 50) 
if combustible_adicional < MARGEN_MINIMO_ADICIONAL:
    print("Advertencia: el margen adicional de combustible es bajo.")
print("=" * 50)
