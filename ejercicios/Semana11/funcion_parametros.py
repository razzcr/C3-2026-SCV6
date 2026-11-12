"""
KM_A_MILLAS = 0.621371
OPCION_SALIR = 3

# --- Encabezado ---
print("===================================")
print("      CONVERSOR DE UNIDADES")
print("===================================")

opcion = 0
while opcion != OPCION_SALIR:
    # --- Menú ---
    print()
    print("1. Celsius a Fahrenheit")
    print("2. Kilómetros a millas")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        # --- Convertir temperatura ---
        celsius = float(input("Grados Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(celsius, "°C equivalen a", fahrenheit, "°F")

    elif opcion == 2:
        # --- Convertir distancia ---
        kilometros = float(input("Kilómetros: "))
        millas = kilometros * KM_A_MILLAS
        print(kilometros, "km equivalen a", round(millas, 2), "millas")

    elif opcion != OPCION_SALIR:
        print("Opción no válida.")

# --- Despedida ---
print("Gracias por usar el conversor.")
"""

KM_A_MILLAS = 0.621371
OPCION_SALIR = 3

# --- Encabezado ---
def mostrar_encabezado(nombre_usuario):
    print("===================================")
    print("      Bienvenido(a)", nombre_usuario)
    print("      CONVERSOR DE UNIDADES")
    print("===================================")

# --- Menú ---
def mostrar_menu():
    print()
    print("1. Celsius a Fahrenheit")
    print("2. Kilómetros a millas")
    print("3. Salir")

# --- Convertir temperatura ---
def convertir_temperatura():
    celsius = float(input("Grados Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "°C equivalen a", fahrenheit, "°F")

# --- Convertir distancia ---
def convertir_distancia():
    kilometros = float(input("Kilómetros: "))
    millas = kilometros * KM_A_MILLAS
    print(kilometros, "km equivalen a", round(millas, 2), "millas")

# --- Despedida ---
def mostrar_despedida(usuario):
    print("Gracias", usuario, "por usar el conversor.")

# Programa principal: llama a los procedimientos según la opción elegida
def main():
    nombre_usuario = input("Ingrese su nombre: ")
    mostrar_encabezado(nombre_usuario) # Llamada a la función 
    opcion = 0
    while opcion != OPCION_SALIR:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            convertir_temperatura()
        elif opcion == 2:
            convertir_distancia()
        elif opcion != OPCION_SALIR:
            print("Opción no válida.")

    mostrar_despedida(nombre_usuario)

# Si este archivo se está ejecutando directamente, haga lo siguiente: 
if __name__ == "__main__":
    main()

# Procedimientos con parámetros (sin return)

"""Muestra una línea formada por el carácter repetido."""
def mostrar_linea(caracter, cantidad):
    print(caracter * cantidad)

"""Muestra el texto enmarcado entre dos líneas."""
def mostrar_titulo(texto):
    mostrar_linea("*", len(texto) + 4)
    print("  " + texto)
    mostrar_linea("*", len(texto) + 4)

"""Muestra la tabla de multiplicar de numero, desde 1 hasta el valor de hasta."""
def mostrar_tabla(numero, hasta):
    for i in range(1, hasta + 1):
        print(numero, "x", i, "=", numero * i)

"""Programa principal: el mismo procedimiento se llama con distintos argumentos."""
def main():
    mostrar_titulo("TABLAS DE MULTIPLICAR")
    numero = int(input("¿Qué tabla desea ver? "))
    hasta = int(input("¿Hasta qué número? "))
    mostrar_tabla(numero, hasta)
    mostrar_linea("-", 20)


# Si este archivo se está ejecutando directamente, haga lo siguiente: 
if __name__ == "__main__":
    main()