from app import db

def init_db(app):
    with app.app_context():
        db.create_all()
        print("✅ Base de datos inicializada correctamente.")
