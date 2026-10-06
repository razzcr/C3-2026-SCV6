# Curso: SOFT-01 Principios de Programación 1 (SCV6)
# Archivo: ejercicio4_autorizacion.py
# Integrantes: Carlos Esteban Monge Barquero
# Fecha: 2026-10-06
# Versión: 1.0
# Descripción: Evalúa combustible, oxígeno, energía y provisiones disponibles frente a los requeridos para autorizar o no el lanzamiento.
# Repo: https://github.com/razzcr/C3-2026-SCV6/tree/main/mision-orbita

RESERVA_COMBUSTIBLE = 10

# Lectura de datos
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
energia_disponible = int(input("Energía disponible: "))
energia_requerida = int(input("Energía requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# Cálculos
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Salida
print("=" * 50)
print("          REPORTE DE AUTORIZACIÓN DE LANZAMIENTO")
print("=" * 50)
if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
print("=" * 50)
