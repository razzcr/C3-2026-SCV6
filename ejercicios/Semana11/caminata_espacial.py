# Caminata espacial: verificacion de oxigeno de los trajes

CONSUMO_OXIGENO_MINUTO = 2     # unidades por astronauta por minuto
RESERVA_OXIGENO = 20           # unidades que siempre deben quedar de reserva
MARGEN_SEGURO = 30             # margen minimo para considerar la caminata segura


def calcular_oxigeno_requerido(minutos, astronautas):
    # Consumo total mas la reserva
    requerido = minutos * astronautas * CONSUMO_OXIGENO_MINUTO + RESERVA_OXIGENO
    return requerido


def oxigeno_alcanza(disponible, requerido):
    # La comparacion ya da True o False
    alcanza = disponible >= requerido
    return alcanza


def calcular_minutos_maximos(disponible, astronautas):
    # Si no alcanza para la reserva, no se puede caminar (evita negativos)
    if disponible < RESERVA_OXIGENO:
        minutos = 0
    else:
        # // da solo los minutos completos
        minutos = (disponible - RESERVA_OXIGENO) // (astronautas * CONSUMO_OXIGENO_MINUTO)
    return minutos


def clasificar_margen(disponible, requerido):
    margen = disponible - requerido
    # Se revisa primero el caso mas grave
    if margen < 0:
        clasificacion = "Insuficiente"
    elif margen < MARGEN_SEGURO:
        clasificacion = "Bajo"
    else:
        clasificacion = "Seguro"
    return clasificacion


def leer_entero_positivo(mensaje):
    valor = 0  # en 0 para que el while entre la primera vez
    while valor < 1:
        # try: intenta convertir; int() falla si no es un entero (letras, decimales, vacio)
        try:
            valor = int(input(mensaje))
            if valor < 1:
                print("El valor debe ser mayor que 0.")
        # except: se ejecuta solo si int() fallo; el while vuelve a pedir el dato
        except ValueError:
            print("Debe ingresar un numero entero.")
    return valor


def mostrar_reporte(requerido, clasificacion, autorizada, minutos_maximos):
    print(f"Oxígeno requerido: {requerido}")
    print(f"Margen de oxígeno: {clasificacion}")
    if autorizada:
        print("Caminata autorizada.")
    else:
        print("Caminata no autorizada.")
    print(f"Tiempo máximo posible: {minutos_maximos} minutos")


def main():
    astronautas = leer_entero_positivo("Cantidad de astronautas: ")
    minutos = leer_entero_positivo("Duración de la caminata (minutos): ")
    disponible = leer_entero_positivo("Oxígeno disponible: ")

    requerido = calcular_oxigeno_requerido(minutos, astronautas)
    clasificacion = clasificar_margen(disponible, requerido)
    autorizada = oxigeno_alcanza(disponible, requerido)
    minutos_maximos = calcular_minutos_maximos(disponible, astronautas)

    mostrar_reporte(requerido, clasificacion, autorizada, minutos_maximos)


main()