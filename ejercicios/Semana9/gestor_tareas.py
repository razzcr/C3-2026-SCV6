# Gestor de tareas

tareas = []                                                          # 1. Crear la lista vacía
opcion = 0

while opcion != 4:
    print("\n--- Gestor de tareas ---")
    print("1. Agregar una tarea")
    print("2. Completar una tarea")
    print("3. Mostrar las tareas pendientes")
    print("4. Salir")
    opcion = int(input("Seleccione una opción (1, 2, 3 o 4): "))
    if opcion == 1:
        tarea_nueva = input("Ingrese el nombre de la tarea: ")      
        tareas.append(tarea_nueva)                                  # append() pra agregar valor, la lista crece en 1 # 2. Agregue tarea_nueva al final de la lista
        print("Tarea agregada.")
    elif opcion == 2:
                                                                    
                                                                    
        if len(tareas) == 0:                                        # 3. Condición: la lista está vacía
            print("No hay tareas pendientes.")
        else:
            numero = 1                                              # contador para numerar desde 1 (lo que ve el usuario)
                                                                    # for toma cada elemento de la lista, uno por vuelta, en la variable tarea
            for tarea in tareas:                                    # 4. Recorre la lista tareas
                print(numero, "-", tarea)
                numero = numero + 1
            numero_tarea = int(input("Ingrese el número de la tarea completada: "))
                                                                    # Números válidos: de 1 hasta len(tareas)
                                                                    # no puede ser menor que 1 ni mayor que la cantidad de tareas.
            if numero_tarea >= 1 and numero_tarea <= len(tareas):   # 5. Condición: entre 1 y la cantidad
                                                                   
                completada = tareas.pop(numero_tarea - 1)           # 6. Elimine la tarea de la lista
                print("Tarea completada:", completada)
            else:
                print("Número de tarea no válido.")
    elif opcion == 3:
        if len(tareas) == 0:
            print("No hay tareas pendientes.")
        else:
                                                                    # len() para mostrar cuántas tareas hay
            print("Tareas pendientes:", len(tareas))                # 7. Cantidad de tareas
            for tarea in tareas:
                print("-", tarea)
    elif opcion == 4:
        print("¡Lo esperamos pronto!")
    else:
        print("Opción no válida.")