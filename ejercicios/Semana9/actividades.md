# Listas: gestor de tareas

## Parte 2: Siga el contenido de la lista

| Paso | Opción y dato ingresado | Contenido de `tareas` después del paso | `len(tareas)` | Mensaje que muestra el programa |
|---|---|---|---|---|
| 1 | Opción 1, tarea «Estudiar listas» | - Estudiar listas | 1 | Tarea agregada. |
| 2 | Opción 1, tarea «Hacer la práctica» | - Estudiar listas<br>- Hacer la práctica | 2 | Tarea agregada. |
| 3 | Opción 1, tarea «Leer el capítulo 5» | - Estudiar listas<br>- Hacer la práctica<br>- Leer el capítulo 5 | 3 | Tarea agregada. |
| 4 | Opción 2, número 1 | - Hacer la práctica<br>- Leer el capítulo 5 | 2 | Tarea completada: Estudiar listas |
| 5 | Opción 2, número 3 | - Hacer la práctica<br>- Leer el capítulo 5 | 2 | Número de tarea no válido. |
| 6 | Opción 1, tarea «Repasar ciclos» | - Hacer la práctica<br>- Leer el capítulo 5<br>- Repasar ciclos | 3 | Tarea agregada. |
| 7 | Opción 2, número 2 | - Hacer la práctica<br>- Repasar ciclos | 2 | Tarea completada: Leer el capítulo 5 |

## Parte 3: Preguntas

**1. ¿Por qué el programa usa `numero_tarea - 1` y no `numero_tarea` dentro de `pop()`?**

El programa usa `numero_tarea - 1` porque el usuario ve las tareas numeradas desde 1 (1, 2, 3, ...), pero las posiciones de una lista en Python empiezan en 0. Restar 1 convierte el número que el usuario escribe en la posición real de la tarea dentro de la lista. Por ejemplo, «Estudiar listas» se muestra como 1, pero está en la posición 0. Si se usara `numero_tarea` sin restar, `pop(1)` eliminaría «Hacer la práctica», que es otra tarea.

**2. Si se elimina el `if` del espacio 5 y el usuario escribe el número 10 con solo 2 tareas en la lista, ¿qué ocurre al ejecutar `pop()`?**

Si se elimina el `if` del espacio 5 y el usuario escribe 10 con solo 2 tareas en la lista, `pop(numero_tarea - 1)` se ejecuta como `pop(9)`. Con 2 elementos solo existen las posiciones 0 y 1, así que la posición 9 no existe. Python no elimina nada y lanza un `IndexError: pop index out of range`, y el programa se detiene de golpe. El `if` evita ese error: solo permite llamar a `pop()` cuando el número está entre 1 y `len(tareas)`, y en caso contrario muestra "Número de tarea no válido." y el programa sigue funcionando.

**3. ¿Qué guarda la variable `completada` después de ejecutar `completada = tareas.pop(numero_tarea - 1)`?**

`completada` guarda el valor (el nombre de la tarea) que estaba en la posición `numero_tarea - 1` y que `pop()` elimina de la lista y devuelve. El programa lo usa en la línea siguiente para mostrar "Tarea completada:" junto con el nombre de la tarea. Por ejemplo, en el paso 4 guarda «Estudiar listas».

**4. Después de completar una tarea, ¿qué pasa con la posición de las tareas que estaban después de ella?**

Cuando se elimina una tarea con `pop()`, las tareas que estaban después de ella se mueven una posición hacia atrás (su índice baja en 1), y las que estaban antes no cambian. Por ejemplo, en el paso 7 la lista era `["Hacer la práctica", "Leer el capítulo 5", "Repasar ciclos"]`. Al eliminar «Leer el capítulo 5» (posición 1), «Repasar ciclos» pasa de la posición 2 a la 1. Por eso la numeración que ve el usuario cambia después de completar una tarea.