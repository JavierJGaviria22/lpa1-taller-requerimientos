from flask import Blueprint, jsonify, request
from app import db, ma
from app.models.cliente import Cliente

clientes_bp = Blueprint('clientes', __name__)

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        load_instance = True

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

# GET todos los clientes
@clientes_bp.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return clientes_schema.jsonify(clientes)

# POST nuevo cliente
@clientes_bp.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.get_json()
    nuevo_cliente = Cliente(
        nombre=data['nombre'],
        email=data['email'],
        telefono=data['telefono']
    )
    db.session.add(nuevo_cliente)
    db.session.commit()
    return cliente_schema.jsonify(nuevo_cliente)
