from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(10), nullable=False)
    dv = db.Column(db.String(1), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=True)
    celular = db.Column(db.String(15), nullable=False)
    correo = db.Column(db.String(100), nullable=False)

class Transaccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)