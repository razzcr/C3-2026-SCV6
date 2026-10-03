# Curso: SOFT-01 Principios de Programación 1 (SCV6)
# Archivo: ejercicio1_recursos.py
# Integrantes: Carlos Esteban Monge Barquero
# Fecha: 2026-10-03
# Versión: 3.0
# Descripción: Calcula los recursos (combustible, oxígeno, energía y provisiones) necesarios para una misión espacial de ida y vuelta.
# Repo: https://github.com/razzcr/C3-2026-SCV6/tree/main/mision-orbita/avance_1

CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
OXIGENO_EMERGENCIA = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
PROVISIONES_ADICIONALES = 3
TRAMOS_VIAJE = 2  # ida y regreso

# Lectura de datos
nombre_mision = input("Nombre de la misión: ")
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Días estimados para llegar al destino: "))

# Cálculos
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
oxigeno_requerido = (dias_viaje * CONSUMO_OXIGENO_TRIPULANTE_DIA * cantidad_tripulantes
                     * TRAMOS_VIAJE + OXIGENO_EMERGENCIA)
energia_requerida = (dias_viaje * CONSUMO_ENERGIA_DIA * TRAMOS_VIAJE
                     + ENERGIA_EXPLORACION)
provisiones_requeridas = (dias_viaje * CONSUMO_PROVISIONES_TRIPULANTE_DIA
                          * cantidad_tripulantes * TRAMOS_VIAJE
                          + PROVISIONES_ADICIONALES)

# Salida
print("=" * 50)
print("          REPORTE DE MISIÓN -", nombre_mision)
print("=" * 50)
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")
print("=" * 50)
