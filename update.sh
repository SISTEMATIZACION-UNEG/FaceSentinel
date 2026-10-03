#!/bin/bash
set -e

echo "=========================================="
echo "    Actualizando FaceSentinel (UNEG)      "
echo "=========================================="

echo "--> 1. Descargando cambios desde GitHub..."
git pull origin main

echo "--> 2. Deteniendo contenedores anteriores..."
docker compose down 2>/dev/null || docker-compose down 2>/dev/null || true

echo "--> 3. Reconstruyendo imagenes y levantando servicios..."
docker compose up -d --build 2>/dev/null || docker-compose up -d --build

echo "--> 4. Estado de los contenedores..."
docker ps --filter "name=facesentinel"

echo "=========================================="
echo "    Actualizacion completada con exito    "
echo "=========================================="
