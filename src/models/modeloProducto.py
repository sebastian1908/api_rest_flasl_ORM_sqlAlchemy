from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(70), unique=True)
    precio = db.Column(db.String(100))
    cantidad = db.Column(db.String(100))


    def __init__(self, nombre_producto, precio, cantidad):
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.cantidad = cantidad

db.create_all()

class Product(ma.Schema):
    class Meta:
      fields = ('id', 'nombre_producto', 'precio', 'cantidad')

data = Product()
datas = Product(many=True)