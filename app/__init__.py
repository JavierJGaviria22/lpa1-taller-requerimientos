from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    ma.init_app(app)

    # Registrar blueprints (rutas)
    try:
        from app.routes.hoteles import hoteles_bp
        from app.routes.habitaciones import habitaciones_bp
        app.register_blueprint(hoteles_bp)
        app.register_blueprint(habitaciones_bp)
    except Exception as e:
        print(f"⚠️ No se pudieron registrar los blueprints: {e}")

    # ✅ Crear las tablas dentro del contexto de la app
    with app.app_context():
        db.create_all()
        print("✅ Base de datos creada correctamente (app.db)")

    return app
