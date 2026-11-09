# Curso: SOFT-01 Principios de Programacion 1 - SCV6
# Archivo: ejercicio8_regreso.py
# Integrantes: Carlos Esteban Monge Barquero
# Fecha: 2026-11-01
# Version: 1.0
# Descripcion: Simulacion del regreso y calculo de supervivencia si quedan varados
# Repo: https://github.com/razzcr/C3-2026-SCV6/tree/main/mision-orbita

# ===== Lectura de datos =====
tripulantes = int(input("Ingrese cantidad de tripulantes: "))
dias_ida = int(input("Ingrese días de ida: "))
combustible_disponible = int(input("Ingrese combustible disponible: "))
oxigeno_disponible = int(input("Ingrese oxígeno disponible: "))
energia_disponible = int(input("Ingrese energía disponible: "))
provisiones_disponibles = int(input("Ingrese provisiones disponibles: "))

# sin reserva de +10, a diferencia del avance 1
combustible_necesario = dias_ida * 8

if combustible_disponible >= combustible_necesario:
    # ===== CASO A: regreso dia por dia =====
    dia = 1
    viaje_exitoso = True

    while dia <= dias_ida and viaje_exitoso:
        # orden de verificacion exigido: oxigeno, energia, provisiones
        # (combustible ya se verifico antes del ciclo)
        if oxigeno_disponible < 2 * tripulantes:
            print("Recursos insuficientes: oxígeno.")
            viaje_exitoso = False
        elif energia_disponible < 5:
            print("Recursos insuficientes: energía.")
            viaje_exitoso = False
        elif provisiones_disponibles < 1 * tripulantes:
            print("Recursos insuficientes: provisiones.")
            viaje_exitoso = False
        else:
            combustible_disponible = combustible_disponible - 8
            oxigeno_disponible = oxigeno_disponible - 2 * tripulantes
            energia_disponible = energia_disponible - 5
            provisiones_disponibles = provisiones_disponibles - 1 * tripulantes
            dia = dia + 1

    if viaje_exitoso == True:
        print("=" * 50)
        print("El viaje fue exitoso, pues completó los días de viaje sin interrupciones")
    else:
        print("=" * 50)
        print("El viaje no ha sido exitoso, pues se agotó alguno de los recursos.")
else:
    # ===== CASO B: tripulacion varada =====
    dias_oxigeno = oxigeno_disponible // (tripulantes * 2)
    dias_energia = energia_disponible // 5
    dias_provisiones = provisiones_disponibles // tripulantes

    # minimo de los tres sin usar min()
    if dias_oxigeno <= dias_energia and dias_oxigeno <= dias_provisiones:
        supervivencia = dias_oxigeno
    elif dias_energia <= dias_oxigeno and dias_energia <= dias_provisiones:
        supervivencia = dias_energia
    else:
        supervivencia = dias_provisiones

    print("=" * 50)
    print(f"La tripulación puede sobrevivir {supervivencia} días.")
    print("=" * 50)
    print("El/los recurso(s) limitante(s) es/son:")
    # if independientes (no elif) para reportar TODOS los empates
    if dias_oxigeno == supervivencia:
        print("Oxígeno")
    if dias_energia == supervivencia:
        print("Energía")
    if dias_provisiones == supervivencia:
        print("Provisiones")