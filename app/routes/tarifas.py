from flask import Blueprint, jsonify, request
from app import db
from app.models.tarifa import Tarifa
from app.schemas.tarifa_schema import TarifaSchema

tarifas_bp = Blueprint('tarifas', __name__, url_prefix='/api/tarifas')

tarifa_schema = TarifaSchema()
tarifas_schema = TarifaSchema(many=True)

# Obtener todas las tarifas
@tarifas_bp.route('/', methods=['GET'])
def listar_tarifas():
    tarifas = Tarifa.query.all()
    return tarifas_schema.jsonify(tarifas)

# Obtener una tarifa por destino
@tarifas_bp.route('/<string:destino>', methods=['GET'])
def obtener_tarifa(destino):
    tarifa = Tarifa.query.filter_by(destino=destino.capitalize()).first()
    if not tarifa:
        return jsonify({"error": "Tarifa no encontrada"}), 404
    return tarifa_schema.jsonify(tarifa)

# Agregar tarifas (para carga inicial o prueba)
@tarifas_bp.route('/seed', methods=['POST'])
def cargar_tarifas():
    data = [
        {"destino": "Aruba", "pasajes": 418, "silver": 134, "gold": 167, "platinum": 191},
        {"destino": "Bahamas", "pasajes": 423, "silver": 112, "gold": 183, "platinum": 202},
        {"destino": "Cancún", "pasajes": 350, "silver": 105, "gold": 142, "platinum": 187},
        {"destino": "Hawaii", "pasajes": 858, "silver": 210, "gold": 247, "platinum": 291},
        {"destino": "Jamaica", "pasajes": 380, "silver": 115, "gold": 134, "platinum": 161},
        {"destino": "Madrid", "pasajes": 496, "silver": 190, "gold": 230, "platinum": 270},
        {"destino": "Miami", "pasajes": 334, "silver": 122, "gold": 151, "platinum": 183},
        {"destino": "Moscu", "pasajes": 634, "silver": 131, "gold": 153, "platinum": 167},
        {"destino": "NewYork", "pasajes": 495, "silver": 104, "gold": 112, "platinum": 210},
        {"destino": "Panamá", "pasajes": 315, "silver": 119, "gold": 138, "platinum": 175},
        {"destino": "Paris", "pasajes": 512, "silver": 210, "gold": 260, "platinum": 290},
        {"destino": "Rome", "pasajes": 478, "silver": 184, "gold": 220, "platinum": 250},
        {"destino": "Seul", "pasajes": 967, "silver": 205, "gold": 245, "platinum": 265},
        {"destino": "Sidney", "pasajes": 1045, "silver": 170, "gold": 199, "platinum": 230},
        {"destino": "Taipei", "pasajes": 912, "silver": 220, "gold": 245, "platinum": 298},
        {"destino": "Tokio", "pasajes": 989, "silver": 189, "gold": 231, "platinum": 255}
    ]

    for item in data:
        if not Tarifa.query.filter_by(destino=item['destino']).first():
            db.session.add(Tarifa(**item))

    db.session.commit()
    return jsonify({"mensaje": "Tarifas cargadas exitosamente"}), 201
