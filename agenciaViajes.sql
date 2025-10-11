-- --------------------------------------------------------
-- Host:                         C:\Users\DELL\Documents\Javier Jose Gaviria\UniRemigton\4to Semestre\Lenguaje de programacion avanzado 1\lpa1-taller-requerimientos\instance\app.db
-- Versión del servidor:         3.39.0
-- SO del servidor:              
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para app
CREATE DATABASE IF NOT EXISTS "app";
;

-- Volcando estructura para tabla app.cliente
CREATE TABLE IF NOT EXISTS cliente (
	id INTEGER NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	telefono VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla app.clientes
CREATE TABLE IF NOT EXISTS clientes (
	id INTEGER NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	telefono VARCHAR(50) NOT NULL, 
	correo VARCHAR(100) NOT NULL, 
	direccion VARCHAR(200) NOT NULL, 
	PRIMARY KEY (id)
);

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla app.habitaciones
CREATE TABLE IF NOT EXISTS habitaciones (
	id INTEGER NOT NULL, 
	tipo VARCHAR(50) NOT NULL, 
	descripcion TEXT, 
	precio FLOAT NOT NULL, 
	capacidad INTEGER NOT NULL, 
	estado VARCHAR(20), 
	hotel_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(hotel_id) REFERENCES hoteles (id)
);

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla app.hoteles
CREATE TABLE IF NOT EXISTS hoteles (
	id INTEGER NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	direccion VARCHAR(150), 
	telefono VARCHAR(20), 
	email VARCHAR(100), 
	ubicacion VARCHAR(100), 
	descripcion TEXT, 
	servicios TEXT, 
	estado VARCHAR(20), 
	calificacion_promedio FLOAT, 
	PRIMARY KEY (id)
);

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla app.reservas
CREATE TABLE IF NOT EXISTS reservas (
	id INTEGER NOT NULL, 
	fecha_reserva DATETIME, 
	fecha_inicio DATE NOT NULL, 
	fecha_fin DATE NOT NULL, 
	estado VARCHAR(20), 
	total FLOAT NOT NULL, 
	cliente_id INTEGER NOT NULL, 
	habitacion_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cliente_id) REFERENCES clientes (id), 
	FOREIGN KEY(habitacion_id) REFERENCES habitaciones (id)
);

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla app.tarifas
CREATE TABLE IF NOT EXISTS tarifas (
	id INTEGER NOT NULL, 
	destino VARCHAR(100) NOT NULL, 
	pasajes FLOAT NOT NULL, 
	silver FLOAT NOT NULL, 
	gold FLOAT NOT NULL, 
	platinum FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (destino)
);

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
