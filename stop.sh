#!/bin/bash

echo "@ Matando servidor Flask..."
pkill -f server.py

echo "@ Matando túnel Cloudflare..."
pkill -f cloudflared

echo "@ Detenido todo correctamente."