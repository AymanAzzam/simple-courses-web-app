## Prerequisites
1. [Install minikube](https://minikube.sigs.k8s.io/docs/start/)
2. [Install kubectl](https://kubernetes.io/docs/tasks/tools/)

## Steps
1. Run the minikube cluster
```
minikube start
```
2. Deploy the secrets on the kubernetes cluster
```
kubectl apply -f flask-app-secrets.yml
```
3. Create a persistent volume for mysql database
    1. Change **path: "/mnt/data"** to **path: "<existing-path-in-your-machine"** in the file **mysql-volume.yml** (For windows machines only) 
    2. Create the persistent volume
```
kubectl apply -f mysql-volume.yml
```
4. Deploy the mysql database on the kubernetes cluster
```
kubectl apply -f mysql-deployment.yml
```
5. Connect to mysql
    1. Get the mysql pod name
    ```
    kubectl get pod
    ```
    2. Get a shell for the mysql pod
    ```
    kubectl exec --stdin --tty <mysql-pod-name> -- /bin/bash
    ```
    3. Connect to mysql
    ```
    mysql -u root -p
    ```
    4. Create database and tables
    ```
    CREATE DATABASE IF NOT EXISTS courses_app;

    USE courses_app;

    CREATE TABLE IF NOT EXISTS `instructors` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(255) DEFAULT NULL,
        PRIMARY KEY(`id`)
    );

    CREATE TABLE IF NOT EXISTS `courses` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(255) DEFAULT NULL,
        `description` VARCHAR(255) DEFAULT NULL,
        `instructor_id` INT DEFAULT NULL,
        `start_date` DATE DEFAULT NULL,
        `duration` INT DEFAULT NULL,
        `price` INT DEFAULT NULL,
        PRIMARY KEY(`id`),
        FOREIGN KEY(`instructor_id`) REFERENCES `instructors`(`id`)
    );
    ```
6. Deploy the flask app on the kubernetes cluster
```
kubectl apply -f flask-app-deployment.yml
```
7. Test the flask app service
    1. Get the flask app service url
    ```
    minikube service flask-app-service
    ```
    2. Hit the api of flask app service
    ```
    curl -H "Content-Type: application/json"  <flask-app-service_URL>/
    ```

## Useful links
1. [Deploy mysql on kubernetes](https://phoenixnap.com/kb/kubernetes-mysql)
2. [Deploying a Flask API and MySQL server on Kubernetes](https://github.com/RikKraanVantage/kubernetes-flask-mysql)
