## Prerequisites
1. [Install Docker](https://docs.docker.com/desktop/install/mac-install/)

## Steps
1. Run the following command from the project directory to Build the docker image
```
docker build --tag flask-app:latest -f docker/Dockerfile flask-app/
```
2. Run a container on host port 5001
```
docker run -p 5001:5000 -e DB_HOST=192.168.1.9 -e DB_USERNAME=ayman -e DB_PASSWORD=12345678 -e DB_NAME=courses_app flask-app
```
3. Login to docker
```
docker login
```
4. Tag the image
```
docker image tag flask-app:latest aymanazzam07/flask-app:latest
```
5. Push image to docker hub
```
docker push aymanazzam07/flask-app:latest
```

## Notes
1. The docker container can't connect to the database if the user is created with localhost, It shoulde be created using the host ip. So Create the user using the following
```
CREATE USER 'ayman'@'{host-ip}' IDENTIFIED BY '12345678';
GRANT ALL PRIVILEGES ON courses_app.* TO 'ayman'@'{host-ip}';
```
2. The app inside the container won't be accessible on the host if you hosted it using local host, So we host the app on **0.0.0.0**