.PHONY: install api install_package test

install:
	pip install --upgrade pip
	pip install -r requirements.txt

install_package:
	pip install -e .

test: install_package
	FLASK_ENV=development venv/bin/pytest
