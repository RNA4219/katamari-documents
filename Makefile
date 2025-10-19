
.PHONY: dev run fmt lint test docker

dev:
	pip install -r requirements.txt

run:
	chainlit run src/app.py -h --host 0.0.0.0 --port 8787

fmt:
	rufflehog || true

lint:
	python -m pyflakes src || true

test:
	pytest -q
