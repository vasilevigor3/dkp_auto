CREATE DATABASE IF NOT EXISTS dkp_auto;
USE dkp_auto;
CREATE TABLE IF NOT EXISTS dkp_template
(
    id INT NOT NULL AUTO_INCREMENT,
    template MEDIUMBLOB,
    PRIMARY KEY (id)
);

INSERT INTO dkp_template VALUES(LOAD_FILE('dkp.pdf'));
