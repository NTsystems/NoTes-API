SHELL := /bin/bash

env:
	virtualenv -p /usr/bin/python --always-copy api-env && \
		source api-env/bin/activate && \
		pip install -r requirements/dev.txt

.PHONY: env
