FROM python:3.11-slim

# Variables d'environnement pour Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DISABLE_DB=True

# Proxy de l'X (pour le build)
# ARG http_proxy
# ARG https_proxy
# ENV http_proxy=$http_proxy
# ENV https_proxy=$https_proxy

WORKDIR /app

# Dépendances système (pour compiler certains paquets python)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collecte des fichiers statiques 
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Lancement via Gunicorn (Serveur Pro)
CMD ["gunicorn", "kpihx_labs.wsgi:application", "--bind", "0.0.0.0:8000"]