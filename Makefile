.PHONY: install api install_package test

install:
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

install_package:
	venv/bin/pip install -e .

test: install_package
	FLASK_ENV=development venv/bin/pytest
