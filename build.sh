#!/bin/bash
echo "=== Iniciando build do projeto Django ==="

# Ativa virtualenv (geralmente já ativa no Render)
# source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\Activate.ps1 # Windows, mas Render roda Linux

echo "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Aplicando migrations..."
python manage.py migrate

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Criando superuser se não existir..."
python - <<END
import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

USERNAME = os.environ.get('SUPERUSER_USERNAME', 'DevNath97')
EMAIL = os.environ.get('SUPERUSER_EMAIL', 'seuemail@example.com')
PASSWORD = os.environ.get('SUPERUSER_PASSWORD', 'SenhaTemporaria123')

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superuser '{USERNAME}' criado!")
else:
    print(f"Superuser '{USERNAME}' já existe.")
END

echo "=== Build finalizado com sucesso! ==="
