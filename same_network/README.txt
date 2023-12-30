build images:
docker build -t pet-frontend .\react_frontend\
docker build -t pet-backend .\database_server\

start:
	docker compose -f .\petfinder.yaml up
stop:
	docker compose -f .\petfinder.yaml down