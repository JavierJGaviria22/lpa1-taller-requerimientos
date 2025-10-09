from app import ma
from app.models.tarifa import Tarifa

class TarifaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tarifa
        load_instance = True
