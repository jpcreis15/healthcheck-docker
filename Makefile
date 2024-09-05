install:
	python -m pip install -r requirements.txt

run:
	uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down --rmi all

stop:
	docker-compose stop