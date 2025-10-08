from flask import Blueprint, request, jsonify
from app import db
from app.models.reserva import Reserva
from app.models.habitacion import Habitacion
from app.models.cliente import Cliente
from app.schemas.reserva_schema import ReservaSchema
from datetime import date

reservas_bp = Blueprint('reservas', __name__, url_prefix='/api/reservas')
reserva_schema = ReservaSchema()
reservas_schema = ReservaSchema(many=True)

def parse_date(s):
    # acepta YYYY-MM-DD
    return date.fromisoformat(s)

def habitacion_disponible(habitacion_id, inicio, fin):
    # solapamiento: inicio <= existing_fin and fin >= existing_inicio
    conflicto = Reserva.query.filter(
        Reserva.habitacion_id == habitacion_id,
        Reserva.fecha_inicio <= fin,
        Reserva.fecha_fin >= inicio
    ).first()
    return conflicto is None

@reservas_bp.route('/', methods=['GET'])
def listar_reservas():
    habitacion_id = request.args.get('habitacion_id', type=int)
    if habitacion_id:
        reservas = Reserva.query.filter_by(habitacion_id=habitacion_id).all()
    else:
        reservas = Reserva.query.all()
    return reservas_schema.jsonify(reservas)

@reservas_bp.route('/availability', methods=['GET'])
def check_availability():
    habitacion_id = request.args.get('habitacion_id', type=int)
    inicio = request.args.get('fecha_inicio')
    fin = request.args.get('fecha_fin')
    if not habitacion_id or not inicio or not fin:
        return jsonify({"error": "habitacion_id, fecha_inicio y fecha_fin son requeridos"}), 400
    try:
        d_inicio = parse_date(inicio)
        d_fin = parse_date(fin)
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400
    available = habitacion_disponible(habitacion_id, d_inicio, d_fin)
    return jsonify({"habitacion_id": habitacion_id, "available": available})

@reservas_bp.route('/', methods=['POST'])
def crear_reserva():
    data = request.get_json() or {}
    required = ['cliente_id', 'habitacion_id', 'fecha_inicio', 'fecha_fin']
    if not all(field in data for field in required):
        return jsonify({"error": f"Campos requeridos: {required}"}), 400

    try:
        d_inicio = parse_date(data['fecha_inicio'])
        d_fin = parse_date(data['fecha_fin'])
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

    if d_inicio > d_fin:
        return jsonify({"error": "fecha_inicio debe ser <= fecha_fin"}), 400

    cliente = Cliente.query.get(data['cliente_id'])
    if not cliente:
        return jsonify({"error": "cliente no encontrado"}), 404

    habitacion = Habitacion.query.get(data['habitacion_id'])
    if not habitacion:
        return jsonify({"error": "habitacion no encontrada"}), 404

    if not habitacion_disponible(habitacion.id, d_inicio, d_fin):
        return jsonify({"error": "La habitación no está disponible en el rango seleccionado"}), 409

    nueva = Reserva(
        fecha_inicio = d_inicio,
        fecha_fin = d_fin,
        cliente_id = cliente.id,
        habitacion_id = habitacion.id
    )

    db.session.add(nueva)
    db.session.commit()
    return reserva_schema.jsonify(nueva), 201

@reservas_bp.route('/<int:id>', methods=['GET'])
def obtener_reserva(id):
    r = Reserva.query.get_or_404(id)
    return reserva_schema.jsonify(r)

@reservas_bp.route('/<int:id>', methods=['DELETE'])
def cancelar_reserva(id):
    r = Reserva.query.get_or_404(id)
    db.session.delete(r)
    db.session.commit()
    return jsonify({"mensaje": "Reserva eliminada"}), 204
