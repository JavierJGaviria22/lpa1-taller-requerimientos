from app import db

class Tarifa(db.Model):
    __tablename__ = 'tarifas'

    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(100), nullable=False, unique=True)
    pasajes = db.Column(db.Float, nullable=False)
    silver = db.Column(db.Float, nullable=False)
    gold = db.Column(db.Float, nullable=False)
    platinum = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Tarifa destino={self.destino}>"
