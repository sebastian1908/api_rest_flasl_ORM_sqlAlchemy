from models.modeloProducto import request, jsonify
from models.modeloProducto import productos, app, db, data, datas
from models import *

class Metodos:

    @app.route('/productos', methods=['POST'])
    def createProducto():
      nombre_producto = request.json['nombre_producto']
      precio = request.json['precio']
      cantidad = request.json['cantidad']

      dataProducto = productos(nombre_producto, precio, cantidad)

      db.session.add(dataProducto)
      db.session.commit()

      return jsonify({
        'status': 200,
        'message': 'Producto registrado con exito'
        })

    @app.route('/productos', methods=['GET'])
    def getProducto():
      get_product = productos.query.all()
      result = datas.dump(get_product)
      return jsonify(result)

    @app.route('/productos/<id>', methods=['GET'])
    def getProductId(id):
      produc = productos.query.get(id)
      return data.jsonify(produc)

    @app.route('/productos/<id>', methods=['PUT'])
    def updateProduct(id):
      product = productos.query.get(id)

      nombre_producto = request.json['nombre_producto']
      precio = request.json['precio']
      cantidad = request.json['cantidad']


      product.nombre_producto = nombre_producto
      product.precio = precio
      product.cantidad = cantidad

      db.session.commit()

      return jsonify({
        'status': 200,
        'message': 'Producto actualizado con exito'
      })

    @app.route('/productos/<id>', methods=['DELETE'])
    def deleteProductos(id):
      product = productos.query.get(id)
      db.session.delete(product)
      db.session.commit()
      return jsonify({
          'status': 200,
          'message': 'Producto eliminado con exito'
      })


    @app.route('/', methods=['GET'])
    def index():
          return jsonify({'message': 'Bienvenido API con Flask'})



    if __name__ == "__main__":
      app.run(debug=True)


obj = Metodos()
