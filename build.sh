#!/bin/bash

# ==================================================
# build.sh - Script de build para Render
# ==================================================

# Saia se algum comando falhar
set -e

echo "=== Iniciando build do projeto Django ==="

# Atualiza dependências do pip
echo "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Rodar migrations
echo "Aplicando migrations..."
python manage.py migrate --noinput

# Coletar arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "=== Build finalizado com sucesso! ==="
