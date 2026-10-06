# Misión Órbita - Avance 1: Preparación de la misión

Curso SOFT-01 Principios de programación 1, sección SCV6, Universidad CENFOTEC (C3-2026).
Docente: Verónica Mora Lezcano.

**Integrantes:** Carlos Apellido, Integrante 2, Integrante 3

## Descripción
Cuatro programas independientes en Python que preparan una misión espacial:
1. `ejercicio1_calculo_recursos.py`: calcula combustible, oxígeno, energía y provisiones (secuencial).
2. `ejercicio2_combustible.py`: verifica combustible y advierte si el margen es bajo (condicional simple).
3. `ejercicio3_soporte_tripulacion.py`: verifica oxígeno y provisiones (condicional doble).
4. `ejercicio4_autorizacion.py`: autoriza o rechaza el lanzamiento (condicional doble sin anidación).

## Ejecución
Requiere Python 3. Desde la carpeta `avance1/`:

    python ejercicio1_calculo_recursos.py

Los programas piden los datos por consola (valores enteros positivos).

## Convenciones y estilos
- Variables en snake_case; constantes en MAYÚSCULAS declaradas al inicio.
- Indentación de 4 espacios; encabezado y comentarios por bloque lógico.
- Sin ciclos, funciones, colecciones, librerías ni condicionales anidados/elif.
- Documentación (tablas de variables, diagramas, casos de prueba): `documentacion/avance1.pdf`.
