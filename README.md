# Sistema de Agencia de Viajes

![commits](https://badgen.net/github/commits/UR-CC/lp2-taller1?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/UR-CC/lp2-taller1)

## Autor

- [@JavierJGaviria22](https://www.github.com/JavierJGaviria22)

---

## Descripción del Proyecto

El **Sistema de Agencia de Viajes** es una aplicación académica desarrollada en **Python** utilizando el microframework **Flask** y los principios de **Programación Orientada a Objetos (POO)**.

El objetivo principal del sistema es **gestionar reservas de hoteles y paquetes turísticos** de forma sencilla y centralizada.  
Permite registrar hoteles, habitaciones y clientes, así como realizar búsquedas, gestionar reservas, aplicar políticas de cancelación y visualizar tarifas de destinos turísticos.

El proyecto fue diseñado con una arquitectura modular y extensible, priorizando la claridad y la funcionalidad sobre la complejidad.  

---

## Documentación

Toda la documentación complementaria se encuentra en [`./docs`](./docs)

---

### Requerimientos

#### Requerimientos funcionales
## 📋 Requerimientos del Sistema

- El sistema permite registrar hoteles con su información básica: nombre, dirección, teléfono, correo, ubicación, descripción y servicios.

- El sistema permite registrar habitaciones asociadas a un hotel, incluyendo tipo, descripción, precio, capacidad, servicios y estado.

- Solo las habitaciones y hoteles activos pueden mostrarse o ser reservadas.

- El sistema permite registrar clientes con nombre, teléfono, correo y dirección.

- Los clientes pueden realizar reservas seleccionando habitación, fechas y número de huéspedes, validando disponibilidad y capacidad.

- Se registran las tarifas de destinos turísticos con precios base y categorías: silver, gold y platinum.

- Habitaciones inactivas o en mantenimiento no pueden ser reservadas.

---

### Diseño

El diseño del sistema se basa en un **modelo orientado a objetos** con clases principales que representan las entidades del dominio:

- `Hotel`
- `Habitacion`
- `Cliente`
- `Reserva`
- `Destino`
- `Tarifa`
- `Reseña` (opcional)

Estas clases se relacionan entre sí mediante composición y asociaciones directas.  
Por ejemplo, un **Hotel** contiene múltiples **Habitaciones**, y una **Habitación** puede tener varias **Reservas**.

El siguiente diagrama de clases ilustra la estructura general del sistema:

Ver [Diagrama de Clases](diagrama.md)

---

### Tárifas

|destino|pasajes|silver|gold|platinum|
|:---|---:|---:|---:|---:|
|Aruba|418|134|167|191|
|Bahamas|423|112|183|202|
|Cancún|350|105|142|187|
|Hawaii|858|210|247|291|
|Jamaica|380|115|134|161|
|Madrid|496|190|230|270|
|Miami|334|122|151|183|
|Moscu|634|131|153|167|
|NewYork|495|104|112|210|
|Panamá|315|119|138|175|
|Paris|512|210|260|290|
|Rome|478|184|220|250|
|Seul|967|205|245|265|
|Sidney|1045|170|199|230|
|Taipei|912|220|245|298|
|Tokio|989|189|231|255|

Estas tarifas pueden ser cargadas desde un archivo o tabla de inicialización, y consultadas mediante el módulo de paquetes turísticos.

---

## Instalación

Para ejecutar el sistema en tu entorno local, sigue los pasos:

1. **Clonar el proyecto**
```bash
git clone https://github.com/JavierJGaviria22/lpa1-taller-requerimientos.git
```

2. Crear y activar entorno virtual
```bash
cd lpa1-taller-requerimientos
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Instalar librerías y dependencias
```bash
pip install -r requirements.txt
```
    
## Ejecución

1. Ejecutar el proyecto
```bash
cd lpa1-taller-requerimientos
python run.py
```

2. Cargar bade de datos
Al ejecutar la app con run.py se creara en instance/app.db
abrir con DBeaver y ejecutar agenciaViajes.sql

3. Ejecutar en frontend index.html con live server de vs code para correr la UI de la app.
