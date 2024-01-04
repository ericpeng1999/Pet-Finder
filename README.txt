Each folder corresponds to a different local realization, follow instructions inside.

To get the public AWS images, run the follows:

start: (should be in two separate terminal)
	docker compose -f backend.yaml up
	docker compose -f frontend.yaml up
stop:
	docker compose -f backend.yaml down
	docker compose -f frontend.yaml down