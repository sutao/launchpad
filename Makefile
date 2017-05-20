all: install run

build:
	cd launchpad; python manage.py migrate

run: build
	cd launchpad; python manage.py runserver

install:
	pip install -r requirements.txt

superuser:
	python launchpad/manage.py createsuperuser

migrations:
	python launchpad/manage.py makemigrations launchpad

venv:
	rm -rf env && mkdir env && virtualenv env

.PHONY: install clean build run all superuser venv