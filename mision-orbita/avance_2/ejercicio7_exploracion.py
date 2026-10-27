# ==========================================================================
# Curso: SOFT-01 Principios de Programación 1 - SCV6
# Archivo: ejercicio7_exploracion.py
# Integrantes: Carlos Esteban Monge Barquero
# Fecha: 2026-10-26
# Versión: 1.0
# Descripción: Menú repetitivo de exploración científica
# Repo: https://github.com/razzcr/C3-2026-SCV6/tree/main/mision-orbita
# ==========================================================================

# ======================== Lectura de datos iniciales ======================

energia = int(input("Ingrese energía disponible: "))
provisiones = int(input("Ingrese provisiones disponibles: "))

# ======== Variables de control / acumuladores ==============================

puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
continuar = True  # controla el ciclo while

# ============================ Ciclo del menú ==============================
while continuar:
    print("=" * 50)
    print("MENÚ DE EXPLORACIÓN CIENTÍFICA")
    print("=" * 50)
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Observación")
    print("4. Finalizar")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        costo_energia = 8
        costo_provisiones = 0
        puntos_otorgados = 10
        # Analizar terreno es la actividad más barata: no gasta provisiones,
        # ideal como primera opción cuando los recursos ya están bajos.
        if energia >= costo_energia and provisiones >= costo_provisiones:
            energia = energia - costo_energia
            provisiones = provisiones - costo_provisiones
            puntos_cientificos = puntos_cientificos + puntos_otorgados
            actividades_realizadas = actividades_realizadas + 1
        else:
            print("Recursos insuficientes para analizar terreno.")
            continuar = False

    elif opcion == 2:
        costo_energia = 12
        costo_provisiones = 2
        puntos_otorgados = 20
        # Recolectar muestra es la actividad de mayor costo y mayor recompensa:
        # por eso es la única que incrementa muestras_recolectadas, aparte de
        # los puntos científicos.
        if energia >= costo_energia and provisiones >= costo_provisiones:
            energia = energia - costo_energia
            provisiones = provisiones - costo_provisiones
            puntos_cientificos = puntos_cientificos + puntos_otorgados
            actividades_realizadas = actividades_realizadas + 1
            muestras_recolectadas += 1
        else:
            print("Recursos insuficientes para recolectar muestra.")
            continuar = False

    elif opcion == 3:
        costo_energia = 5
        costo_provisiones = 0
        puntos_otorgados = 8
        # Observación es la más económica en energía y no requiere provisiones,
        # pero otorga menos puntos que las otras dos.
        if energia >= costo_energia and provisiones >= costo_provisiones:
            energia = energia - costo_energia
            provisiones = provisiones - costo_provisiones
            puntos_cientificos = puntos_cientificos + puntos_otorgados
            actividades_realizadas = actividades_realizadas + 1
        else:
            print("Recursos insuficientes para realizar observación.")
            continuar = False

    elif opcion == 4:
        # Finalizar es una salida controlada: a diferencia de "recursos
        # insuficientes", aquí la tripulación decide terminar por su cuenta.
        continuar = False
        print("Exploración finalizada por la tripulación.")
    else:
        print("Opción no válida.")

print("=" * 50)
print("RESUMEN DE LA EXPLORACIÓN")
print("=" * 50)
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia)
print("Provisiones restantes:", provisiones)
print("=" * 50)
