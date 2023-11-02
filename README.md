# python_microservice_project
Python is a perfect tool for building micro-services. So this is a simple movie based microservice python program. 
## Build and Run
### Requirements
* Python
* Docker
* Docker-compose
* PostgreSQL
### Run
* Install FastAPI and Uvicorn
  ```
  pip install fastapi
  pip install uvicorn
  pip install 'databases[postgresql]'
  ```
* Running the microservice using Docker Compose
```
docker-compose up -d
```
* Go to the APIs http://localhost:8080/movie for movie service and http://localhost:8080/cast for cast service.
* For the documentation of Movie Service:- http://localhost:8080/movie/docs and Cast-Service:- http://localhost:8080/casts/docs
