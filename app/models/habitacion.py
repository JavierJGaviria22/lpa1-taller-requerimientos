from app import db

class Habitacion(db.Model):
    __tablename__ = 'habitaciones'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), default='disponible')
    hotel_id = db.Column(db.Integer, db.ForeignKey('hoteles.id'), nullable=False)
