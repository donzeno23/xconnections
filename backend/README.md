## Create virtual env
```
python3 -m venv fastbe
source fastbe/bin/activate
```

## Install packages
```
pip3 install -r requirements.txt
```

## Update all packages
```
pip3 install -U -r requirements.txt
```

## Start BE (from backend)
```
uvicorn app.server.app:app --reload
OR
python app/main.py
```

## Install MySQL
```
root user:
root password: abcd1234
```

## Create Database
```
mysql> CREATE DATABASE xconnections;
Query OK, 1 row affected (0.00 sec)
mysql> use xconnections;
Database changed
```

## Create Tables
```
mysql> create table users (
    -> user_id int AUTO_INCREMENT PRIMARY KEY,
    -> name varchar(45) NOT NULL, 
    -> email varchar(60) NOT NULL,
    -> password varchar(20) NULL, 
    -> phone varchar(20) NOT NULL, 
    -> user_type enum ('Client', 'Vendor') NOT NULL,
    -> sector varchar(30) NULL, 
    -> pending varchar(2) NOT NULL,
    -> UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql> create table vendors (
    ->   vendor_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ->   user_id int NOT NULL,
    ->   address1 varchar(45) NOT NULL,
    ->   address2 varchar(45) NOT NULL,
    ->   city varchar(45) NOT NULL,
    ->   state varchar(45) NOT NULL,
    ->   country varchar(45) NOT NULL,
    ->   zipcode INT NOT NULL,
    ->   UNIQUE INDEX `vendor_id_UNIQUE` (`vendor_id` ASC) VISIBLE,
    ->   INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
    ->   CONSTRAINT `user_id`
    ->     FOREIGN KEY (`user_id`)
    ->     REFERENCES users (`user_id`)
    ->     ON DELETE NO ACTION
    ->     ON UPDATE NO ACTION);
Query OK, 0 rows affected (0.04 sec)

mysql> create table skills (
    ->   skill_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ->   skill varchar(45) NOT NULL,
    ->   UNIQUE INDEX `skill_id_UNIQUE` (`skill_id` ASC) VISIBLE);
Query OK, 0 rows affected (0.03 sec)

mysql> create table vendor_skills (
    ->   vs_id int NOT NULL AUTO_INCREMENT,
    ->   vs_vendor_id int NOT NULL,
    ->   vs_skill_id int NOT NULL,
    ->   PRIMARY KEY (`vs_id`),
    ->   UNIQUE INDEX `vs_id_UNIQUE` (`vs_id` ASC) VISIBLE,
    ->   INDEX `vendor_id_idx` (`vs_vendor_id` ASC) VISIBLE,
    ->   INDEX `skill_id_idx` (`vs_skill_id` ASC) VISIBLE,
    ->   CONSTRAINT `vendor_id`
    ->     FOREIGN KEY (`vs_vendor_id`)
    ->     REFERENCES vendors (`vendor_id`)
    ->     ON DELETE NO ACTION
    ->     ON UPDATE NO ACTION,
    ->   CONSTRAINT `skill_id`
    ->     FOREIGN KEY (`vs_skill_id`)
    ->     REFERENCES skills (`skill_id`)
    ->     ON DELETE NO ACTION
    ->     ON UPDATE NO ACTION);
Query OK, 0 rows affected (0.02 sec)


mysql> describe users;
+-----------+-------------------------+------+-----+---------+----------------+
| Field     | Type                    | Null | Key | Default | Extra          |
+-----------+-------------------------+------+-----+---------+----------------+
| user_id   | int                     | NO   | PRI | NULL    | auto_increment |
| name      | varchar(45)             | NO   |     | NULL    |                |
| email     | varchar(60)             | NO   |     | NULL    |                |
| password  | varchar(20)             | YES  |     | NULL    |                |
| phone     | varchar(20)             | NO   |     | NULL    |                |
| user_type | enum('Client','Vendor') | NO   |     | NULL    |                |
| sector    | varchar(30)             | YES  |     | NULL    |                |
| pending   | varchar(2)              | NO   |     | NULL    |                |
+-----------+-------------------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

mysql> describe vendors;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| vendor_id | int         | NO   | PRI | NULL    | auto_increment |
| user_id   | int         | NO   | MUL | NULL    |                |
| address1  | varchar(45) | NO   |     | NULL    |                |
| address2  | varchar(45) | NO   |     | NULL    |                |
| city      | varchar(45) | NO   |     | NULL    |                |
| state     | varchar(45) | NO   |     | NULL    |                |
| country   | varchar(45) | NO   |     | NULL    |                |
| zipcode   | int         | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

mysql> describe skills;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| skill_id | int         | NO   | PRI | NULL    | auto_increment |
| skill    | varchar(45) | NO   |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> describe vendor_skills;
+--------------+------+------+-----+---------+----------------+
| Field        | Type | Null | Key | Default | Extra          |
+--------------+------+------+-----+---------+----------------+
| vs_id        | int  | NO   | PRI | NULL    | auto_increment |
| vs_vendor_id | int  | NO   | MUL | NULL    |                |
| vs_skill_id  | int  | NO   | MUL | NULL    |                |
+--------------+------+------+-----+---------+----------------+
3 rows in set (0.01 sec)
```

## Grant priveleges
```
mysql> CREATE USER 'daloia'@'localhost' IDENTIFIED WITH authentication_plugin BY 'admin';
ERROR 1524 (HY000): Plugin 'authentication_plugin' is not loaded

TODO: use MySQL Workbench to add user and grant privileges

(fastbe) Rachels-MacBook-Pro:backend racheldaloia$ mysql -u daloia -p xconnections
Enter password: 
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 24
Server version: 8.0.28 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```