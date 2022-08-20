# Karmel_Backend
Karmel App - Backend python code

# Docker Empty Image
```
cd <open docker folder>
git clone https://github.com/DominikZurawski/Karmel_Backend.git
docker-compose up -d
```

If you want run empty image without data on mongodb use docker-compose.ymp script :
```
version: '3'
services:

  flask:
    build: .
    command: ./gunicorn.sh 
    ports:
      - "5000:5000"
    container_name: flask
    restart: unless-stopped
    environment:
      MONGODB_DATABASE: *******
      MONGODB_USERNAME: ******
      MONGODB_PASSWORD: *******
      MONGODB_HOSTNAME: mongodb
      MONGODB_PORT: 27017
    volumes:
      - .:/app
    depends_on:
      - mongodb
    networks:
      - frontend
      - backend
    image: domino675/karmel_flask:latest

  mongodb:
    container_name: mongodb
    restart: unless-stopped
    command: mongod --auth
    environment:
      MONGO_INITDB_ROOT_USERNAME: *****
      MONGO_INITDB_ROOT_PASSWORD: *******
      MONGO_INITDB_DATABASE: ******
      MONGODB_DATA_DIR: /data/db
      MONDODB_LOG_DIR: /dev/null
    volumes:
      - mongodbdata:/data/db
    ports:
      - "27017:27017"
    networks:
      - backend
    image: domino675/karmel_mongodb:empty


  webserver:
    build:
      context: nginx
      dockerfile: Dockerfile
    container_name: webserver
    restart: unless-stopped
    environment:
      APP_ENV: "prod"
      APP_NAME: "webserver"
      APP_DEBUG: "true"
      SERVICE_NAME: "webserver"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - nginxdata:/var/log/nginx
    depends_on:
      - flask
    networks:
      - frontend
    image: domino675/karmel_web:latest


networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge

volumes:
  mongodbdata:
    driver: local
  app:
    driver: local
  nginxdata:
    driver: local
```

## Geting started
Move to the project and simply run `docker-compose up --build` to start the dockers.

To run all the dockers in background, use `docker-compose up -d`.

To change the initial username and password for building mongodb on the first time(when there is no files in `mongodb/db`), edit `.env` to pass in environment variables.

To restore from existing mongodb, put backup file in `mongo/db`, after dockers run, run `docker exec -it mongodb sh` to enter interactive shell inside of the mongodb docker container and use mongo shell command to retore your backup file under `/data/db`.