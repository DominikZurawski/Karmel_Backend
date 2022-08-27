# Karmel_Backend
Karmel App - Backend python code

## Git repository clone
```
cd <open docker folder to local machine>
git clone https://github.com/DominikZurawski/Karmel_Backend.git
```

## Docker run & build
Move to the project and simply run `docker-compose up --build` to start the dockers.

To run all the dockers in background, use `docker-compose up -d`.

To change the initial username and password for building mongodb on the first time(when there is no files in `mongodb/db`), edit `.env` to pass in environment variables.

To restore from existing mongodb, put backup file in `mongo/db`, after dockers run, run `docker exec -it mongodb sh` to enter interactive shell inside of the mongodb docker container and use mongo shell command to retore your backup file under `/data/db`.
### Add .env file
```
MONGO_INITDB_ROOT_USERNAME=<username>
MONGO_INITDB_ROOT_PASSWORD=<password>
MONGO_INITDB_DATABASE=<database_name>
MONGODB_HOSTNAME=mongodb
MONGODB_PORT=27017
MONGODB_DATA_DIR=/data/db
MONDODB_LOG_DIR=/dev/null
```
### Run & build
```
docker-compose up -d --build
```
### Change image
```
docker tag karmel_backend_flask:latest user/DockerRepository:version
```
### Login to DockerHub and push image
```
docker login
username:***
password: ***
docker push user/DockerRepository:version
docker logout
```
# Static files
```
cd nginx/html/database
```
