.PHONY: install
install:
	poetry install

.PHONY: migrations
migrations:
	poetry run python src/manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python src/manage.py migrate

.PHONY: superuser
superuser:
	poetry run python src/manage.py createsuperuser

.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: run-server
run-server:
	poetry run python src/manage.py runserver

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrate install-pre-commit ;
