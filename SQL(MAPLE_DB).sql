
use maple_db;
/*
DROP TABLE sell_item;
CREATE TABLE sell_item
(
   id INT PRIMARY KEY AUTO_INCREMENT,
   item_name VARCHAR(32) NOT NULL,
   item_sell_date VARCHAR(32) NOT NULL,
   item_price VARCHAR(32) NOT NULL,
   item_option_id INT NOT NULL,
   crt_id VARCHAR(20),
   crt_dt VARCHAR(14)
) ENGINE=INNODB;
CREATE INDEX sell_item_idx1 ON sell_item(item_name);

DROP TABLE sell_item_option;
CREATE TABLE sell_item_option
(
   item_option_id INT,
   option_name VARCHAR(200) not null,
   first_amt VARCHAR(50),
   second_amt VARCHAR(50),
   third_amt VARCHAR(50),
   forth_amt VARCHAR(50),
   crt_id VARCHAR(20),
   crt_dt VARCHAR(14)
) ENGINE=INNODB;
CREATE INDEX sell_item_option_idx1 ON sell_item_option(item_option_id,option_name);
ALTER TABLE `sell_item_option_idx1` ADD `option_kind` VARCHAR(30) ;

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
   
   #검색 아이템

DROP TABLE search_item_list;
CREATE TABLE search_item_list(
	item_name VARCHAR(150) 
    ,item_type VARCHAR(150),
     PRIMARY KEY(item_name,item_type)
) ENGINE = InnoDB;
ALTER TABLE `search_item_list` ADD `use_yn` VARCHAR(20) ;
ALTER TABLE `search_item_list` ADD `min_amt` VARCHAR(30) ;


DROP TABLE search_item_detail;
CREATE TABLE search_item_detail(
    id INT AUTO_INCREMENT,
    item_name VARCHAR(32) NOT NULL,
    item_sell_date VARCHAR(32) NOT NULL,
    item_price VARCHAR(32) NOT NULL,
    item_option_id INT NOT NULL,
	strz INT,
	strp INT,
	strl INT,
	dexz INT,
	dexp INT,
	dexl INT,
	intz INT,
	intp INT,
	intl INT,
	lukz INT,
	lukp INT,
	lukl INT,
	allz INT,
	allp INT,
	att INT,
	attp INT,
	mtt INT,
	mttp INT,
	btt INT,
	igd INT,
	dmg INT,
	upg INT,
	mhpp INT,
    mhpz INT,
	cool INT,
	cridmg INT,
     PRIMARY KEY(id,item_name)
) ENGINE = InnoDB;

    */






select si.item_name,si.item_sell_date,si.item_price,sio.*
from sell_item si
join sell_item_option sio on si.item_option_id = sio.item_option_id
and sio.crt_dt >='2022110409';

and si.item_price =31111111
 ;
select distinct(option_name)
from sell_item_option;
where item_option_id between 703 and 711
;
select nextval('sell_item_option');
select *
from sequences;


SELECT * 
from search_item_detail 

;
select *
from sell_item si
;




  
select *
from search_item_list l;
where ifnull(use_yn,'Y') ='Y';
insert into search_item_list values
('데아시두스이어링','귀고리','Y','10000000'),
('파풀라투스마크','눈장식','Y','10000000'),
('골든클로버벨트','벨트','Y','10000000'),
('분노한자쿰의벨트','벨트','Y','10000000'),
('도미네이터펜던트','펜던트','Y','10000000'),
('응축된힘의결정석','얼굴장식','Y','10000000'),
('아쿠아틱레터눈장식','눈장식','Y','10000000');


select item_name,item_price,
case when greatest(strz+dexz*0.1+allp*10+att*4, dexz+strz*0.1+allp*10+att*4,intz+lukz*0.1+allp*10+mtt*4,lukz+dexz*0.1+allp*10+att*4) = strz+dexz*0.1+allp*10+att*4 then
	'str'
    when greatest(strz+dexz*0.1+allp*10+att*4, dexz+strz*0.1+allp*10+att*4,intz+lukz*0.1+allp*10+mtt*4,lukz+dexz*0.1+allp*10+att*4) = dexz+strz*0.1+allp*10+att*4 then
    'dex'
    when greatest(strz+dexz*0.1+allp*10+att*4, dexz+strz*0.1+allp*10+att*4,intz+lukz*0.1+allp*10+mtt*4,lukz+dexz*0.1+allp*10+att*4) = intz+lukz*0.1+allp*10+mtt*4 then
    'int'
    when greatest(strz+dexz*0.1+allp*10+att*4, dexz+strz*0.1+allp*10+att*4,intz+lukz*0.1+allp*10+mtt*4,lukz+dexz*0.1+allp*10+att*4) = lukz+dexz*0.1+allp*10+att*4 then
    'luk'
end
,greatest(strz+dexz*0.1+allp*10+att*4, dexz+strz*0.1+allp*10+att*4,intz+lukz*0.1+allp*10+mtt*4,lukz+dexz*0.1+allp*10+att*4)
from  search_item_detail2 sid;