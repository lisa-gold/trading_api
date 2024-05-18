PORT ?= 8000
start:
	uvicorn positions.main:app --host 0.0.0.0 --port 8000  

lint:
	poetry run flake8 positions
