from app import ma
from app.models.habitacion import Habitacion

class HabitacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Habitacion
        load_instance = True
        include_fk = True
