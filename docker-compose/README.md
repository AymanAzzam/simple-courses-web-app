## Prerequisites
1. Install docker compose

## Steps
1. Set env variables
```
export DB_HOST=localhost
export DB_USERNAME=ayman
export DB_PASSWORD=12345678
export DB_ROOT_PASSWORD=12345678
export DB_NAME=courses_app
```
2. Run docker-compose file from the project directory
```
docker-compose -f docker-compose/docker-compose.yaml
```