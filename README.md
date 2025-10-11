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
- **R1**: El sistema debe permitir registrar hoteles con su información básica (nombre, dirección, teléfono, correo, ubicación, descripción y servicios).
- **R2**: El sistema debe permitir registrar habitaciones asociadas a un hotel, con su tipo, descripción, precio, capacidad, servicios y estado (activo/inactivo/mantenimiento).
- **R3**: Solo las habitaciones y hoteles activos podrán mostrarse en las búsquedas o ser reservadas.
- **R4**: El sistema debe permitir registrar clientes con nombre, teléfono, correo electrónico y dirección.
- **R5**: Los clientes deben poder buscar habitaciones disponibles por **fecha**, **ubicación**, **precio** o **calificación**.
- **R6**: Los clientes podrán realizar **reservas** seleccionando habitación, rango de fechas y número de huéspedes, validando la disponibilidad y capacidad.
- **R7**: Las reservas podrán tener diferentes estados (`pendiente`, `confirmada`, `cancelada`, `completada`).
- **R8**: Cada hotel podrá definir sus propias políticas de cancelación y pago.
- **R9**: El sistema debe permitir registrar **comentarios y calificaciones** de los clientes una vez completada la estancia.
- **R10**: El sistema debe calcular calificaciones promedio por habitación y por hotel.
- **R11**: Se deben registrar las **tarifas de destinos turísticos**, con precios base de pasajes y categorías **silver**, **gold** y **platinum**.
- **R12**: Los clientes podrán reservar **paquetes turísticos** combinando destino y categoría.
- **R13**: Las habitaciones inactivas o en mantenimiento no podrán ser reservadas.

#### Requerimientos no funcionales
- **RNF1**: La aplicación debe estar desarrollada en Python con Flask.
- **RNF2**: La arquitectura debe seguir los principios de POO.
- **RNF3**: El sistema debe contar con persistencia de datos (ej. SQLite o MySQL).
- **RNF4**: La interfaz debe ser simple, clara y funcional para demostración académica.
- **RNF5**: El sistema debe permitir fácilmente la extensión de nuevas funcionalidades (ofertas, temporadas, reportes).

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
venv/bin/activate
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
