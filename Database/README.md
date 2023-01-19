## Prerequisites
1. [Install MySql server](https://www.mysql.com/downloads/)
2. Install MySql Client (I use DBeaver)

## Steps
1. Connect to mysql server using the root user
```
mysql -u root -p
```
2. Create a new database
```
CREATE DATABASE databasename;
```
3. Create a new user
```
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```
4. Give the user access to the database
```
GRANT ALL PRIVILEGES ON databasename.* TO 'username'@'host';
```
5. Connect to the new database with the new user using MySql Client
6. Run **create.sql** script on the client to create the tables
7. Run **dummydata.sql** script to the client create dummy data