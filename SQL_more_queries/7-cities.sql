-- Create table id not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY, state_id INT, FOREIGN KEY(state_id) REFERENCE states(id), name VARCHAR(256) NOT NULL);