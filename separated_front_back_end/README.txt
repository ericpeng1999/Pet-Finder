build images:
docker build -t pet-frontend .\react_frontend\
docker build -t pet-backend .\database_server\

start:
	docker compose -f .\database_server\backend.yaml up
	docker compose -f .\react_frontend\frontend.yaml up
stop:
	docker compose -f .\database_server\backend.yaml down
	docker compose -f .\react_frontend\frontend.yaml down