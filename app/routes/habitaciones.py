from flask import Blueprint, jsonify, request
from app.models.habitacion import Habitacion
from app.schemas.hotel_schema import HabitacionSchema
from app import db

# 🔹 Creamos el Blueprint (debe llamarse habitaciones_bp)
habitaciones_bp = Blueprint('habitaciones', __name__)

# 🔹 Schema para serializar datos
habitacion_schema = HabitacionSchema()
habitaciones_schema = HabitacionSchema(many=True)

# 🔹 Ruta: Obtener todas las habitaciones
@habitaciones_bp.route('/habitaciones', methods=['GET'])
def get_habitaciones():
    habitaciones = Habitacion.query.all()
    return jsonify(habitaciones_schema.dump(habitaciones))

# 🔹 Ruta: Crear nueva habitación
@habitaciones_bp.route('/habitaciones', methods=['POST'])
def create_habitacion():
    data = request.get_json()
    nueva_habitacion = Habitacion(
        tipo=data.get('tipo'),
        descripcion=data.get('descripcion'),
        precio=data.get('precio'),
        capacidad=data.get('capacidad'),
        estado=data.get('estado', 'disponible'),
        hotel_id=data.get('hotel_id')
    )
    db.session.add(nueva_habitacion)
    db.session.commit()
    return habitacion_schema.jsonify(nueva_habitacion), 201
