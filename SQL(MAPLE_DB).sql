
use maple_db;
/*
CREATE TABLE sell_item
(
   id INT PRIMARY KEY AUTO_INCREMENT,
   item_name VARCHAR(32) NOT NULL,
   item_sell_date VARCHAR(32) NOT NULL,
   item_price VARCHAR(32) NOT NULL,
   item_option_id INT NOT NULL
) ENGINE=INNODB;


CREATE TABLE sell_item
(
   id INT PRIMARY KEY AUTO_INCREMENT,
   item_name VARCHAR(32) NOT NULL,
   item_sell_date VARCHAR(32) NOT NULL,
   item_price VARCHAR(32) NOT NULL,
   item_option_id INT NOT NULL
) ENGINE=INNODB;
CREATE INDEX sell_item_idx1 ON sell_item(item_name)

CREATE TABLE sell_item_option
(
   item_option_id INT,
   option_name VARCHAR(200) not null,
   first_amt VARCHAR(50),
   second_amt VARCHAR(50),
   third_amt VARCHAR(50),
   forth_amt VARCHAR(50)
) ENGINE=INNODB;
CREATE INDEX sell_item_option_idx1 ON sell_item_option(item_option_id,option_name);

CREATE TABLE SEQUENCES(
	NAME VARCHAR(32)
    ,CURRVAL BIGINT UNSIGNED
) ENGINE = InnoDB;


DELIMITER $$
	DROP FUNCTION nextval;
	CREATE FUNCTION nextval
    (the_name VARCHAR(32))
    RETURNS BIGINT UNSIGNED
    MODIFIES SQL DATA
    DETERMINISTIC
    BEGIN
		DECLARE ret BIGINT UNSIGNED;
        UPDATE sequences SET currval = currval + 1 WHERE seq_name = the_name;
        SELECT currval INTO ret FROM sequences WHERE seq_name = the_name LIMIT 1;
        RETURN ret;
	END;

DELIMITER $$
    DROP PROCEDURE create_sequence;
	CREATE PROCEDURE create_sequence (IN the_name text)
    MODIFIES SQL DATA
    DETERMINISTIC
    BEGIN 
    DELETE FROM sequences WHERE seq_name = the_name;
    INSERT INTO sequences VALUES(the_name,0);
	END;
    

DELIMITER $$
	drop function currval;
	CREATE FUNCTION currval
    (the_name VARCHAR(32))
    RETURNS BIGINT UNSIGNED
    MODIFIES SQL DATA
    DETERMINISTIC
    BEGIN
		DECLARE ret BIGINT UNSIGNED;
        SELECT currval INTO ret FROM sequences WHERE seq_name = the_name LIMIT 1;
        RETURN ret;
	END;    
    
    #시퀀스 테이블 만들기
    DROP TABLE sequences;
   CREATE TABLE sequences   ( seq_name VARCHAR(32) , currval BIGINT UNSIGNED) ENGINE = InnoDB;
    */

CALL create_sequence('sell_item_option');
INSERT INTO `maple_db`.`sell_item` (`item_name`, `item_sell_date`, `item_price`, `item_option_id`) VALUES ('234', '234', '234', '234');

 
select * from sell_item;
select *
from sell_item_option;
select nextval('sell_item_option');
select *
from sequences;

