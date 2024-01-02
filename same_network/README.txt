build images:
docker build --no-cache -t pet-frontend:1.0 .\react_frontend\
docker build --no-cache -t pet-backend:1.0 .\database_server\

start:
	docker compose -f .\petfinder.yaml up
stop:
	docker compose -f .\petfinder.yaml down