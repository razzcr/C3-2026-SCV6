# Misión Órbita — Avance 1

Simulador de recursos para una misión espacial de ida y vuelta. A partir de datos ingresados por el usuario, el programa calcula y verifica el combustible, oxígeno, energía y provisiones necesarios para una tripulación, e informa si la misión puede ser autorizada para el lanzamiento.

## Información del curso

- **Curso:** SOFT-01 Principios de Programación 1 — sección SCV6
- **Universidad:** CENFOTEC
- **Periodo:** C3-2026
- **Docente:** Verónica Mora Lezcano
- **Autor:** Carlos Esteban Monge Barquero (trabajo individual)
- **Entrega:** Avance 1 — 14 de octubre de 2026
- **Repositorio:** https://github.com/razzcr/C3-2026-SCV6/tree/main/mision-orbita

## Estructura del repositorio

```
mision-orbita/
├── avance_1/
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
├── documentacion/
│   └── avance1_documentacion.pdf
└── README.md
```

## Descripción de los ejercicios

### 1. `ejercicio1_recursos.py` — Reporte de recursos de la misión
Solicita el nombre de la misión, la cantidad de tripulantes y los días estimados de viaje al destino. A partir de estos datos calcula el combustible (ida, regreso y reserva), el oxígeno, la energía y las provisiones necesarias para completar el recorrido de ida y vuelta, e imprime un reporte con todos los valores.

### 2. `ejercicio2_combustible.py` — Verificación de combustible
Solicita el combustible disponible y el requerido para ida y regreso. Calcula el combustible total necesario (incluyendo una reserva de emergencia) y el margen adicional disponible, mostrando una advertencia si dicho margen es menor al mínimo recomendado.

### 3. `ejercicio3_soporte_tripulacion.py` — Soporte a la tripulación
Solicita el oxígeno y las provisiones disponibles y requeridas, y determina si la nave cuenta con recursos suficientes para sostener a la tripulación durante la misión.

### 4. `ejercicio4_autorizacion.py` — Autorización de lanzamiento
Solicita los valores disponibles y requeridos de combustible, oxígeno, energía y provisiones, y evalúa en conjunto si todos los recursos son suficientes para autorizar el lanzamiento de la misión.

## Cómo ejecutar los programas

Desde la carpeta `avance_1/`, ejecutar cada ejercicio con Python 3:

```bash
cd avance_1
python ejercicio1_recursos.py
python ejercicio2_combustible.py
python ejercicio3_soporte_tripulacion.py
python ejercicio4_autorizacion.py
```

Cada programa solicitará los datos necesarios por consola (números enteros positivos) y mostrará el reporte correspondiente.

## Documentación

La documentación completa del avance se encuentra en [`documentacion/avance1_documentacion.pdf`](documentacion/avance1_documentacion.pdf), e incluye portada, tablas de variables, diagramas de flujo, código fuente y 18 casos de prueba con capturas de consola para los cuatro ejercicios.

## Convenciones y restricciones de código

Siguiendo los lineamientos del curso para este avance, el código:

- No utiliza ciclos, funciones, colecciones ni imports.
- No utiliza `elif` ni condicionales anidados (únicamente `if` / `else` simples).
- Usa nombres de variables en `snake_case` y constantes en mayúsculas.
- Asume que todas las entradas son números enteros positivos.
