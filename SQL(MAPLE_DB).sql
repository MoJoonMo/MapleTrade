
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
where si.item_name='앱솔랩스시프글러브'
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



insert into search_item_list values
('고통의근원','펜던트','N','10000000000'),
('골든클로버벨트','벨트','N','16000000'),
('노블브레이슬릿','보조무기','N','100000000'),
('데아시두스이어링','귀고리','N','16000000'),
('데이브레이크펜던트','펜던트','N','3000000000'),
('도미네이터펜던트','펜던트','N','1000000000'),
('라이징썬펜던트','펜던트','N','1000000000'),
('로얄블랙메탈숄더','어깨장식','N','16000000'),
('루즈컨트롤머신마크','얼굴장식','N','1000000000'),
('마력이깃든안대','눈장식','N','1000000000'),
('마이스터이어링','귀고리','N','500000000'),
('매커네이터펜던트','펜던트','N','350000000'),
('몽환의벨트','벨트','N','10000000000'),
('베어스퍼플펜던트','펜던트','N','350000000'),
('분노한자쿰의벨트','벨트','N','16000000'),
('샤이니레드매지션마이스터심볼','얼굴장식','N','1000000000'),
('샤이니레드시프마이스터심볼','얼굴장식','N','1000000000'),
('샤이니레드아처마이스터심볼','얼굴장식','N','1000000000'),
('샤이니레드워리어마이스터심볼','얼굴장식','N','1000000000'),
('샤이니레드파이렛마이스터심볼','얼굴장식','N','1000000000'),
('아울스퍼플펜던트','펜던트','N','350000000'),
('아케인셰이드나이트글러브','장갑','N','500000000'),
('아케인셰이드나이트숄더','어깨장식','N','500000000'),
('아케인셰이드나이트슈즈','신발','N','500000000'),
('아케인셰이드나이트케이프','망토','N','500000000'),
('아케인셰이드메이지글러브','장갑','N','500000000'),
('아케인셰이드메이지숄더','어깨장식','N','500000000'),
('아케인셰이드메이지슈즈','신발','N','500000000'),
('아케인셰이드메이지케이프','망토','N','500000000'),
('아케인셰이드시프글러브','장갑','N','500000000'),
('아케인셰이드시프숄더','어깨장식','N','500000000'),
('아케인셰이드시프슈즈','신발','N','500000000'),
('아케인셰이드시프케이프','망토','N','500000000'),
('아케인셰이드아처글러브','장갑','N','500000000'),
('아케인셰이드아처숄더','어깨장식','N','500000000'),
('아케인셰이드아처슈즈','신발','N','500000000'),
('아케인셰이드아처케이프','망토','N','500000000'),
('아케인셰이드튜너','무기','N','500000000'),
('아케인셰이드파이렛글러브','장갑','N','500000000'),
('아케인셰이드파이렛숄더','어깨장식','N','500000000'),
('아케인셰이드파이렛슈즈','신발','N','500000000'),
('아케인셰이드파이렛케이프','망토','N','500000000'),
('앱솔랩스나이트글러브','장갑','N','350000000'),
('앱솔랩스나이트숄더','어깨장식','N','350000000'),
('앱솔랩스나이트슈즈','신발','N','350000000'),
('앱솔랩스나이트케이프','망토','N','350000000'),
('앱솔랩스나이트헬름','모자','N','350000000'),
('앱솔랩스메이지글러브','장갑','N','350000000'),
('앱솔랩스메이지숄더','어깨장식','N','350000000'),
('앱솔랩스메이지슈즈','신발','N','350000000'),
('앱솔랩스메이지케이프','망토','N','350000000'),
('앱솔랩스메이지크라운','모자','N','350000000'),
('앱솔랩스시프글러브','장갑','N','350000000'),
('앱솔랩스시프숄더','어깨장식','N','350000000'),
('앱솔랩스시프슈즈','신발','N','350000000'),
('앱솔랩스시프케이프','망토','N','350000000'),
('앱솔랩스시프캡','모자','N','350000000'),
('앱솔랩스아처글러브','장갑','N','350000000'),
('앱솔랩스아처숄더','어깨장식','N','350000000'),
('앱솔랩스아처슈즈','신발','N','350000000'),
('앱솔랩스아처케이프','망토','N','350000000'),
('앱솔랩스아처후드','모자','N','350000000'),
('앱솔랩스파이렛글러브','장갑','N','350000000'),
('앱솔랩스파이렛숄더','어깨장식','N','350000000'),
('앱솔랩스파이렛슈즈','신발','N','350000000'),
('앱솔랩스파이렛케이프','망토','N','350000000'),
('앱솔랩스파이렛페도라','모자','N','350000000'),
('에스텔라이어링','귀고리','N','3000000000'),
('오션글로우이어링','귀고리','Y','10000000000'),
('울프스퍼플펜던트','펜던트','Y','350000000'),
('이글아이던위치팬츠','상의','Y','350000000'),
('이글아이레인져후드','상의','Y','350000000'),
('이글아이어새신셔츠','상의','Y','350000000'),
('이글아이워리어아머','상의','Y','350000000'),
('이글아이원더러코트','상의','Y','350000000'),
('저주받은녹의마도서','포켓아이템','Y','15000000000'),
('저주받은적의마도서','포켓아이템','Y','15000000000'),
('저주받은청의마도서','포켓아이템','Y','15000000000'),
('저주받은황의마도서','포켓아이템','Y','15000000000'),
('커맨더포스이어링','귀고리','Y','10000000000'),
('타일런트리카온벨트','벨트','Y','700000000'),
('타일런트알테어벨트','벨트','Y','700000000'),
('타일런트케이론벨트','벨트','Y','700000000'),
('타일런트헤르메스벨트','벨트','Y','700000000'),
('타일런트히아데스벨트','벨트','Y','700000000'),
('트릭스터던위치팬츠','하의','Y','350000000'),
('트릭스터레인져팬츠','하의','Y','350000000'),
('트릭스터어새신팬츠','하의','Y','350000000'),
('트릭스터워리어팬츠','하의','Y','350000000'),
('트릭스터원더러팬츠','하의','Y','350000000'),
('트와일라이트마크','얼굴장식','Y','3000000000'),
('파풀라투스마크','눈장식','Y','300000000'),
('피콕스퍼플펜던트','펜던트','Y','1000000000'),
('핑크빛성배','포켓아이템','Y','16000000'),
('하이네스던위치햇','모자','Y','350000000'),
('하이네스레인져베레','모자','Y','350000000'),
('하이네스어새신보닛','모자','Y','350000000'),
('하이네스워리어헬름','모자','Y','350000000'),
('하이네스원더러햇','모자','Y','350000000');