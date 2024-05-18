PORT ?= 10000
start:
	uvicorn positions.main:app --host 0.0.0.0 --port $(PORT)  

lint:
	poetry run flake8 positions
