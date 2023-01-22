## Prerequisites
1. Python3
2. Flask
```
pip3 install flask
```
3. PyMySql
```
pip3 install pymysql
```

## Steps
1. Set **FLASK_APP**, **FLASK_ENV** and **FLASK_DEBUG** env variables
```
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
```
2. Set the database env variables
```
export MYSQL_SERVICE_HOST=localhost
export DB_USERNAME=ayman
export DB_PASSWORD=12345678
export DB_NAME=courses_app
```
3. Run the flask app
```
python3 app.py
```