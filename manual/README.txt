manual start

database configuration:
	run the yaml file in terminal:
		docker-compose -f petfinder.yaml up
	or setup manually:
		docker network create petfinder
		docker run -d --name postgresDB -p5432:5432 --net petfinder -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=user -e POSTGRES_DB=petfinder postgres


In terminal, first enter either of the two server folder and execute:
	python -m uvicorn server:app --reload
to start the backend server.

Then start another terminal, enter the react_frontend folder and execute
	npm install
to install necessary dependencies and use
	npm start
to start the frontend server.