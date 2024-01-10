Each folder corresponds to a different local realization, follow instructions inside.

To get the public AWS images, run the follows:

start: (should be in two separate terminal)
	docker compose -f backend.yaml up
	docker compose -f frontend.yaml up
stop:
	docker compose -f backend.yaml down
	docker compose -f frontend.yaml down


If aws login attempt fails with
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/r4t8b3u1
go into C:\Users\Default.DESKTOP-V3H4PV2\.docker and remove the "credsStore" key in config.json while Docker is running.