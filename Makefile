# Makefile pour KpihX Labs

# Couleurs pour le terminal
GREEN=\033[0;32m
NC=\033[0m # No Color

.PHONY: init up down logs shell

# --- 1. Initialisation du projet (Le truc magique) ---
init:
	@echo "${GREEN}🚀 Initialisation de l'environnement de développement...${NC}"
	@if [ ! -f .env ]; then \
		echo "Copie de .env.example vers .env..."; \
		cp .env.example .env; \
	else \
		echo ".env existe déjà."; \
	fi
	@if [ ! -f docker-compose.override.yml ]; then \
		echo "Copie de docker-compose.override.example.yml vers docker-compose.override.yml..."; \
		cp docker-compose.override.example.yml docker-compose.override.yml; \
	else \
		echo "docker-compose.override.yml existe déjà."; \
	fi
	@echo "${GREEN}✅ Prêt ! Modifie le fichier .env si besoin, puis lance 'make up'.${NC}"

# --- 2. Commandes raccourcies ---
up:
	docker compose up -d --build

down:
	sudo docker compose down

logs:
	docker compose logs -f

shell:
	docker compose exec web bash

migrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

superuser:
	docker compose exec web python manage.py createsuperuser