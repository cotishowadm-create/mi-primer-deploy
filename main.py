from flask import Flask, jsonify
from flask_cors import CORS
import os

# 1. Inicializamos la app
app = Flask(__name__)
CORS(app)

# 2. Definimos la ruta principal (puedes probarla en el navegador)
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "mensaje": "¡Servidor Railway funcionando correctamente!",
        "owner": "Chuck",
        "sucursales": 5
    })

# 3. Definimos una ruta de prueba para tus datos
@app.route('/api/test')
def test():
    return jsonify({
        "item": "Sincronizador de Precios",
        "version": "1.0.0",
        "db_status": "esperando_conexion"
    })

# 4. Configuración del puerto para Railway
if __name__ == '__main__':
    # Railway inyecta automáticamente una variable de entorno llamada PORT
    port = int(os.getenv('PORT', 8080))
    # '0.0.0.0' permite que el servidor sea accesible desde internet
    app.run(host='0.0.0.0', port=port)
