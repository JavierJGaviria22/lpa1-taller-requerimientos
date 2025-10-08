from app import db

class Hotel(db.Model):
    __tablename__ = 'hoteles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(150))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    ubicacion = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    servicios = db.Column(db.Text)
    estado = db.Column(db.String(20), default="activo")
    calificacion_promedio = db.Column(db.Float, default=0.0)

    habitaciones = db.relationship('Habitacion', backref='hotel', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Hotel {self.nombre}>'
