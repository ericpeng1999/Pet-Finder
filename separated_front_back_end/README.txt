build images:
	docker build --no-cache -t pet-frontend:1.0 .\react_frontend\
	docker build --no-cache -t pet-backend:1.0 .\database_server\

start: (should be in two separate terminal)
	docker compose -f .\database_server\backend.yaml up
	docker compose -f .\react_frontend\frontend.yaml up
stop:
	docker compose -f .\database_server\backend.yaml down
	docker compose -f .\react_frontend\frontend.yaml down