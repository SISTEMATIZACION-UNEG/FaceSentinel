#!/bin/bash
set -e

echo "=== Actualizando FaceSentinel ==="
git pull origin main

echo "=== Verificando variables de entorno ==="
grep -q "^LIVENESS_POLICY=" .env || echo "LIVENESS_POLICY=passive_lbp" >> .env

echo "=== Reconstruyendo y levantando contenedores ==="
docker-compose up -d --build

echo "=== Estado de los servicios ==="
docker ps --filter "name=facesentinel"
