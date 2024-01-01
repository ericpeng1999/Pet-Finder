Each folder corresponds to a different realization. The images(separated_front_back_end) are on AWS and can be deployed as follows:

start: (should be in two separate terminal)
	docker compose -f backend.yaml up
	docker compose -f frontend.yaml up
stop:
	docker compose -f backend.yaml down
	docker compose -f frontend.yaml down