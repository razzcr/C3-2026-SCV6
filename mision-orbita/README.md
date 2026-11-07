# Misión Órbita — Proyecto Final

Simulador de recursos para una misión espacial de ida y vuelta. A partir de datos ingresados por el usuario, el programa calcula y verifica el combustible, oxígeno, energía y provisiones necesarios para una tripulación, e informa si la misión puede ser autorizada para el lanzamiento, además de simular el regreso y la exploración científica durante la misión.

## Información del curso

- **Curso:** SOFT-01 Principios de Programación 1 — sección SCV6
- **Universidad:** CENFOTEC
- **Periodo:** C3-2026
- **Docente:** Verónica Mora Lezcano
- **Autor:** Carlos Esteban Monge Barquero (trabajo individual)
- **Repositorio:** https://github.com/razzcr/C3-2026-SCV6/tree/main/mision-orbita

## Estructura del repositorio


mision-orbita/
├── avance_1/
│ ├── ejercicio1_recursos.py
│ ├── ejercicio2_combustible.py
│ ├── ejercicio3_soporte_tripulacion.py
│ └── ejercicio4_autorizacion.py
├── avance_2/
│ ├── ejercicio7_exploracion.py
│ └── ejercicio8_regreso.py
├── documentacion/
│ ├── avance1_documentacion.pdf
│ └── avance2_documentacion.pdf
└── README.md


## Descripción de los ejercicios

### Avance 1 — Entregado 14 de octubre de 2026

#### 1. `ejercicio1_recursos.py` — Reporte de recursos de la misión
Solicita el nombre de la misión, la cantidad de tripulantes y los días estimados de viaje al destino. A partir de estos datos calcula el combustible (ida, regreso y reserva), el oxígeno, la energía y las provisiones necesarias para completar el recorrido de ida y vuelta, e imprime un reporte con todos los valores.

#### 2. `ejercicio2_combustible.py` — Verificación de combustible
Solicita el combustible disponible y el requerido para ida y regreso. Calcula el combustible total necesario (incluyendo una reserva de emergencia) y el margen adicional disponible, mostrando una advertencia si dicho margen es menor al mínimo recomendado.

#### 3. `ejercicio3_soporte_tripulacion.py` — Soporte a la tripulación
Solicita el oxígeno y las provisiones disponibles y requeridas, y determina si la nave cuenta con recursos suficientes para sostener a la tripulación durante la misión.

#### 4. `ejercicio4_autorizacion.py` — Autorización de lanzamiento
Solicita los valores disponibles y requeridos de combustible, oxígeno, energía y provisiones, y evalúa en conjunto si todos los recursos son suficientes para autorizar el lanzamiento de la misión.

### Avance 2 — Entrega 8 de noviembre de 2026

#### 7. `ejercicio7_exploracion.py` — Exploración científica
Presenta un menú repetitivo con cuatro opciones (analizar terreno, recolectar muestra, observación, finalizar). Cada actividad consume energía y/o provisiones y otorga puntos científicos; si los recursos no alcanzan para la actividad elegida, el menú finaliza e informa un resumen con las actividades realizadas, las muestras recolectadas, los puntos obtenidos y los recursos restantes.

#### 8. `ejercicio8_regreso.py` — Regreso y supervivencia
Calcula el combustible necesario para el regreso. Si es suficiente, simula el viaje día por día verificando oxígeno, energía y provisiones, e informa si el regreso fue exitoso. Si el combustible no alcanza, calcula cuántos días podría sobrevivir la tripulación varada según cada recurso disponible, e indica el recurso (o recursos, en caso de empate) que limita esa supervivencia.

## Cómo ejecutar los programas

Desde la carpeta correspondiente, ejecutar cada ejercicio con Python 3:

```bash
cd avance_1
python ejercicio1_recursos.py
python ejercicio2_combustible.py
python ejercicio3_soporte_tripulacion.py
python ejercicio4_autorizacion.py

cd ../avance_2
python ejercicio7_exploracion.py
python ejercicio8_regreso.py