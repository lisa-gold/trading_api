start:
	uvicorn positions.main:app --reload

lint:
	poetry run flake8 positions
