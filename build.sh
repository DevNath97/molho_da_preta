#!/bin/bash
# build.sh - Render build script

# Instala dependências
pip install -r requirements.txt

# Executa migrações do banco
python manage.py migrate

# Coleta arquivos estáticos
python manage.py collectstatic --noinput
