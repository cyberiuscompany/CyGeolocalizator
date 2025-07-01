#!/bin/bash

echo "@ Activando entorno virtual..."
source venv/bin/activate

# Crear carpeta de logs si no existe
mkdir -p logs

echo "@ Instalando dependencias..."
pip install -r requirements.txt

echo "@ Matando procesos anteriores de Flask y Cloudflared..."
pkill -f server.py
pkill -f cloudflared

echo "@ Lanzando servidor Flask..."
nohup python server.py --host=0.0.0.0 --port=5000 > logs/flask.log 2>&1 &

sleep 2  # espera a que Flask arranque

echo "@ Iniciando túnel Cloudflare..."
nohup cloudflared tunnel --url http://localhost:5000 > logs/cloudflare.log 2>&1 &

sleep 5  # espera a que Cloudflare genere la URL

echo "@ URL pública (trycloudflare.com):"
grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' logs/cloudflare.log | head -n 1