from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import time
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

users_data = []

@app.route('/api/report', methods=['POST'])
def report():
    data = request.json
    data['timestamp'] = time.time()
    users_data.append(data)
    return jsonify({'status': 'ok'})

@app.route('/api/report', methods=['GET'])
def get_users():
    return jsonify(users_data)

# Ruta genérica para servir archivos estáticos (como login.html)
@app.route('/')
def root():
    return send_from_directory('.', 'login.html')  # Redirige por defecto a login.html

# Por si se navega manualmente a /login.html o /main.html
@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
