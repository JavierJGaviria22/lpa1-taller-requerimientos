from app import ma
from app.models.hotel import Hotel
from app.models.habitacion import Habitacion

class HabitacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Habitacion
        load_instance = True

class HotelSchema(ma.SQLAlchemyAutoSchema):
    habitaciones = ma.Nested(HabitacionSchema, many=True)

    class Meta:
        model = Hotel
        load_instance = True
        include_fk = True
