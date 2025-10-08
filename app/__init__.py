from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    # Importar y registrar blueprints
    from app.routes.hoteles import hoteles_bp
    from app.routes.habitaciones import habitaciones_bp  # ✅ ahora sí existe

    app.register_blueprint(hoteles_bp)
    app.register_blueprint(habitaciones_bp)

    with app.app_context():
        db.create_all()

    return app
