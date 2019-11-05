.PHONY: install install_package test

install:
	pip install --upgrade pip
	pip install -r requirements.txt

install_package:
	pip install -e .

test: install_package
	pytest
