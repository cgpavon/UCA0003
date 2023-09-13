from flask import Flask, request, jsonify, render_template, send_from_directory, Response
from flask_cors import CORS
#import pyodbc
import os

app = Flask(__name__)

CORS(app)

# Ruta para obtener la página defaul (en general se la llama Index.HTML)
@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/get_imagenes', methods=['GET'])
def get_imagenes():
    archivos_Img = os.listdir('img')
    #img_Urls = [f'/img/{img}' for img in archivos_Img]
    img_Urls = [f'http://127.0.0.1:4500/get_imagenes/{img}' for img in archivos_Img]
    return jsonify(img_Urls)

@app.route('/get_imagenes/<nombre>', methods=['GET'])
def get_imagen(nombre):
    try:
        # Construye la ruta completa al archivo de imagen
        ruta_imagen = '/img/' + nombre
        # Utiliza send_from_directory para enviar la imagen al cliente
        return send_from_directory('/img/', nombre)
    except Exception as e:
        # En caso de error, devuelve una respuesta de error con un mensaje
        mensaje_error = "Error al obtener la imagen: " + str(e)
        return Response(mensaje_error, status=500)
    return send_from_directory('/img/', nombre)


if __name__ == '__main__':
    app.run(debug=True, port=4500)