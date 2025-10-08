from app import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)

    reservas = db.relationship('Reserva', backref='cliente', lazy=True)
