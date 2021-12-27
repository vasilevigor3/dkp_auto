CREATE DATABASE IF NOT EXISTS database_name;
USE database_name;
CREATE TABLE IF NOT EXISTS mytable
(
    id INT NOT NULL AUTO_INCREMENT,
    string VARCHAR(20),
    PRIMARY KEY (id)
);
