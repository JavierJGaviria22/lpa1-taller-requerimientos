from flask import Blueprint, request, jsonify
from app import db
from app.models.hotel import Hotel
from app.schemas.hotel_schema import HotelSchema

hoteles_bp = Blueprint('hoteles', __name__, url_prefix='/api/hoteles')
hotel_schema = HotelSchema()
hoteles_schema = HotelSchema(many=True)

@hoteles_bp.route('/', methods=['GET'])
def listar_hoteles():
    hoteles = Hotel.query.all()
    return jsonify(hoteles_schema.dump(hoteles))

@hoteles_bp.route('/', methods=['POST'])
def crear_hotel():
    data = request.json
    nuevo_hotel = Hotel(**data)
    db.session.add(nuevo_hotel)
    db.session.commit()
    return hotel_schema.jsonify(nuevo_hotel), 201

@hoteles_bp.route('/<int:id>', methods=['GET'])
def obtener_hotel(id):
    hotel = Hotel.query.get_or_404(id)
    return hotel_schema.jsonify(hotel)

@hoteles_bp.route('/<int:id>', methods=['PUT'])
def actualizar_hotel(id):
    hotel = Hotel.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        setattr(hotel, key, value)
    db.session.commit()
    return hotel_schema.jsonify(hotel)

@hoteles_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_hotel(id):
    hotel = Hotel.query.get_or_404(id)
    db.session.delete(hotel)
    db.session.commit()
    return jsonify({"mensaje": "Hotel eliminado"}), 204
