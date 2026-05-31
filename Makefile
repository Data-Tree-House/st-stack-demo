.PHONY: up down build rebuild logs

up:
	docker compose up

down:
	docker compose down

build:
	docker compose build

rebuild:
	docker compose build --no-cache

logs:
	docker compose logs -f

sync:
	uv sync --all-extras --dev
