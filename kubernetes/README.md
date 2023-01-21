## Prerequisites
1. [Install minikube](https://minikube.sigs.k8s.io/docs/start/)
2. [Install kubectl](https://kubernetes.io/docs/tasks/tools/)

## Steps
1. Deploy the secrets on the kubernetes cluster
```
kubectl apply -f flask-app-secrets.yml
```
2. Create a persistent volume for mysql database
```
kubectl apply -f mysql-volume.yml
```
3. Deploy the mysql database on the kubernetes cluster
```
kubectl apply -f mysql-deployment.yml
```
4. Deploy the flask app on the kubernetes cluster
```
kubectl apply -f flask-app-deployment.yml
```