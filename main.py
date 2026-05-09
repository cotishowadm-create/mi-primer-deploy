from flask import Flask, jsonify
from flask_cors import CORS
import os
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    # Simulamos el estado de tus 5 sucursales
    sucursales_info = [
        {"id": 1, "nombre": "Sucursal Centro", "status": random.choice(["Online", "Offline"])},
        {"id": 2, "nombre": "Sucursal Norte", "status": random.choice(["Online", "Offline"])},
        {"id": 3, "nombre": "Sucursal Sur", "status": random.choice(["Online", "Offline"])},
        {"id": 4, "nombre": "Sucursal Este", "status": "Online"},
        {"id": 5, "nombre": "Sucursal Oeste", "status": "Online"},
    ]

    return jsonify({
        "owner": "Chuck",
        "ultima_actualizacion": datetime.now().strftime("%H:%M:%S"),
        "total_sucursales": len(sucursales_info),
        "detalle_sucursales": sucursales_info,
        "mensaje": "Dashboard de sucursales activo"
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
