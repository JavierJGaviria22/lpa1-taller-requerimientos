-- --------------------------------------------------------
-- CREACIÓN DE BASE DE DATOS Y TABLAS
-- --------------------------------------------------------

-- HOTELS
DROP TABLE IF EXISTS hoteles;
CREATE TABLE hoteles (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT,
    email TEXT,
    ubicacion TEXT,
    descripcion TEXT,
    servicios TEXT,
    estado TEXT,
    calificacion_promedio REALj
);

-- HABITACIONES
DROP TABLE IF EXISTS habitaciones;
CREATE TABLE habitaciones (
    id INTEGER PRIMARY KEY,
    tipo TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    capacidad INTEGER NOT NULL,
    estado TEXT,
    hotel_id INTEGER NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hoteles(id)
);

-- CLIENTES
DROP TABLE IF EXISTS clientes;
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT NOT NULL,
    direccion TEXT NOT NULL
);

-- RESERVAS
DROP TABLE IF EXISTS reservas;
CREATE TABLE reservas (
    id INTEGER PRIMARY KEY,
    fecha_reserva TEXT DEFAULT CURRENT_TIMESTAMP,
    fecha_inicio TEXT NOT NULL,
    fecha_fin TEXT NOT NULL,
    estado TEXT,
    total REAL NOT NULL,
    cliente_id INTEGER NOT NULL,
    habitacion_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (habitacion_id) REFERENCES habitaciones(id)
);

-- TARIFAS
DROP TABLE IF EXISTS tarifas;
CREATE TABLE tarifas (
    id INTEGER PRIMARY KEY,
    destino TEXT NOT NULL UNIQUE,
    pasajes REAL NOT NULL,
    silver REAL NOT NULL,
    gold REAL NOT NULL,
    platinum REAL NOT NULL
);

-- --------------------------------------------------------
-- 🔹 DATOS DE PRUEBA
-- --------------------------------------------------------

-- 🏨 HOTELES
INSERT INTO hoteles (nombre, direccion, telefono, email, ubicacion, descripcion, servicios, estado, calificacion_promedio) VALUES
('Hotel Caribe Azul', 'Av. del Mar 123, Cartagena', '3001112233', 'contacto@caribeazul.com', 'Cartagena', 'Hotel frente al mar con piscina y spa.', 'WiFi, Piscina, Spa, Restaurante', 'activo', 4.6),
('Montaña Real Resort', 'Km 12 vía al Nevado, Manizales', '3124455667', 'info@montanareal.com', 'Manizales', 'Resort campestre con vista a las montañas.', 'WiFi, Jacuzzi, Caminatas, Restaurante', 'activo', 4.8),
('Hotel Central Bogotá', 'Cra 10 #15-20, Bogotá', '3107788990', 'recepcion@centralbogota.com', 'Bogotá', 'Hotel ejecutivo en el centro de la ciudad.', 'WiFi, Desayuno, Parqueadero, Gimnasio', 'activo', 4.3);

-- 🛏️ HABITACIONES
INSERT INTO habitaciones (tipo, descripcion, precio, capacidad, estado, hotel_id) VALUES
('Suite Deluxe', 'Habitación con vista al mar y jacuzzi.', 420000, 2, 'activo', 1),
('Doble Estandar', 'Habitación doble con aire acondicionado.', 250000, 2, 'activo', 1),
('Familiar Premium', 'Habitación amplia con dos camas queen.', 380000, 4, 'activo', 2),
('Cabina Ecológica', 'Habitación ecológica con terraza.', 310000, 3, 'activo', 2),
('Ejecutiva Simple', 'Habitación ejecutiva con escritorio y TV.', 200000, 1, 'activo', 3),
('Doble Ejecutiva', 'Habitación con dos camas individuales.', 230000, 2, 'activo', 3);

-- 👤 CLIENTES
INSERT INTO clientes (nombre, telefono, correo, direccion) VALUES
('Ana Gómez', '3112233445', 'ana.gomez@mail.com', 'Cra 12 #45-32, Medellín'),
('Carlos Pérez', '3125566778', 'carlos.perez@mail.com', 'Cll 7 #12-19, Bogotá'),
('Laura Torres', '3009988776', 'laura.torres@mail.com', 'Av. Las Palmas #22-45, Cali');

-- 📅 RESERVAS
INSERT INTO reservas (fecha_inicio, fecha_fin, estado, total, cliente_id, habitacion_id) VALUES
('2025-10-10', '2025-10-12', 'confirmada', 500000, 1, 1),
('2025-11-05', '2025-11-07', 'pendiente', 460000, 2, 4),
('2025-09-15', '2025-09-18', 'completada', 600000, 3, 2);

-- ✈️ TARIFAS
INSERT INTO tarifas (destino, pasajes, silver, gold, platinum) VALUES
('Aruba', 418, 134, 167, 191),
('Bahamas', 423, 112, 183, 202),
('Cancún', 350, 105, 142, 187),
('Hawaii', 858, 210, 247, 291),
('Jamaica', 380, 115, 134, 161),
('Madrid', 496, 190, 230, 270),
('Miami', 334, 122, 151, 183),
('Moscu', 634, 131, 153, 167),
('New York', 495, 104, 112, 210),
('Panamá', 315, 119, 138, 175),
('Paris', 512, 210, 260, 290),
('Rome', 478, 184, 220, 250),
('Seul', 967, 205, 245, 265),
('Sidney', 1045, 170, 199, 230),
('Taipei', 912, 220, 245, 298),
('Tokio', 989, 189, 231, 255);
