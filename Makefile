SHELL := /bin/bash

clean:
	rm -rf api-env

env:
	virtualenv -p /usr/bin/python --always-copy api-env && \
		source api-env/bin/activate && \
		pip install -r requirements/dev.txt

runserver: env
	python manage.py runserver 0.0.0.0:8000

.PHONY: env
