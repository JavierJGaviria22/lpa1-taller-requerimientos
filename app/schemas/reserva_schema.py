from app import ma
from app.models.reserva import Reserva
from app.schemas.cliente_schema import ClienteSchema
from app.schemas.habitacion_schema import HabitacionSchema

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    cliente = ma.Nested(ClienteSchema)
    habitacion = ma.Nested(HabitacionSchema)

    class Meta:
        model = Reserva
        load_instance = True
        include_fk = True
