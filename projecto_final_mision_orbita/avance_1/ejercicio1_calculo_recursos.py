# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Carlos Apellido, Integrante 2, Integrante 3
# Fecha: 01/10/2026        Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

# ----- Declaración de constantes -----
# Se usan constantes para evitar "números mágicos" en las fórmulas.
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
OXIGENO_EMERGENCIA = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
PROVISIONES_ADICIONALES = 3
TRAMOS_VIAJE = 2  # ida y regreso (el regreso dura lo mismo que la ida)

# ----- Entrada de datos -----
nombre_mision = input("Nombre de la misión: ")
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Días estimados para llegar al destino: "))

# ----- Procesamiento -----
# El regreso dura los mismos días que la ida, por eso se usa dias_viaje en ambos.
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Los consumos diarios aplican durante ida y regreso (TRAMOS_VIAJE).
oxigeno_requerido = (dias_viaje * CONSUMO_OXIGENO_TRIPULANTE_DIA * cantidad_tripulantes
                     * TRAMOS_VIAJE + OXIGENO_EMERGENCIA)
energia_requerida = (dias_viaje * CONSUMO_ENERGIA_DIA * TRAMOS_VIAJE
                     + ENERGIA_EXPLORACION)
provisiones_requeridas = (dias_viaje * CONSUMO_PROVISIONES_TRIPULANTE_DIA
                          * cantidad_tripulantes * TRAMOS_VIAJE
                          + PROVISIONES_ADICIONALES)

# ----- Salida de resultados -----
print("-" * 60)
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
print("-" * 60)
