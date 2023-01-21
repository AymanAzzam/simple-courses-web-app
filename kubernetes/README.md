## Prerequisites
1. [Install minikube](https://minikube.sigs.k8s.io/docs/start/)
2. [Install kubectl](https://kubernetes.io/docs/tasks/tools/)

## Steps
1. Run the following command to encode the database password
```
echo -n super-secret-passwod | base64
```
2. Add the output to the flak-app-secrets.yml file at the DB_PASSWORD value
3. Deploy the secrets on the kubernetes cluster
```
kubectl apply -f flask-app-secrets.yml
```
4. Create a persistent volume for mysql database
```
kubectl apply -f mysql-volume.yml
```
5. Deploy the mysql database on the kubernetes cluster
```
kubectl apply -f mysql-deployment.yml
```
6. Deploy the flask app on the kubernetes cluster
```
kubectl apply -f flask-app-deployment.yml
```

## Notes
1. The docker container can't connect to the database if the user is created with localhost, It shoulde be created using the host ip. So Create the user using the following
```
CREATE USER 'ayman'@'{host-ip}' IDENTIFIED BY '12345678';
GRANT ALL PRIVILEGES ON courses_app.* TO 'ayman'@'{host-ip}';
```
2. The app inside the container won't be accessible on the host if you hosted it using local host, So we host the app on **0.0.0.0**