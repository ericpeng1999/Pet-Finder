Each folder corresponds to a different realization. The images(separated_front_back_end) are on AWS and can be deployed as follows:

start: (should be in two separate terminal)
	docker compose -f .\database_server\backend.yaml up
	docker compose -f .\react_frontend\frontend.yaml up
stop:
	docker compose -f .\database_server\backend.yaml down
	docker compose -f .\react_frontend\frontend.yaml down