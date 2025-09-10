run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

test:
	python manage.py test

lint:
	isort ./create_quote_request && black ./create_quote_request && flake8 ./create_quote_request

