
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
    */

CALL create_sequence('sell_item_option');
INSERT INTO `maple_db`.`sell_item` (`item_name`, `item_sell_date`, `item_price`, `item_option_id`) VALUES ('234', '234', '234', '234');

delete from/* sell_item ;*/
/*delete from sell_item_option ;*/
 
select si.*,sio.* 
from sell_item si
join sell_item_option sio on si.item_option_id = sio.item_option_id
;
select *
from sell_item_option
where item_option_id between 703 and 711
;
select nextval('sell_item_option');
select *
from sequences;

select * from search_item_list;


insert into search_item_list values
('마이스터링'),
('가디언엔젤링'),
('아케인셰이드나이트숄더'),
('아케인셰이드나이트글러브'),
('아케인셰이드나이트슈즈'),
('아케인셰이드나이트케이프');
insert into search_item_list values
('아케인셰이드나이트글러브','장갑'),
('아케인셰이드나이트슈즈','신발'),
('아케인셰이드나이트숄더','어깨장식'),
('아케인셰이드나이트케이프','망토'),
('아케인셰이드메이지글러브','장갑'),
('아케인셰이드메이지슈즈','신발'),
('아케인셰이드메이지숄더','어깨장식'),
('아케인셰이드메이지케이프','망토'),
('아케인셰이드시프글러브','장갑'),
('아케인셰이드시프슈즈','신발'),
('아케인셰이드시프숄더','어깨장식'),
('아케인셰이드시프케이프','망토'),
('아케인셰이드아처글러브','장갑'),
('아케인셰이드아처슈즈','신발'),
('아케인셰이드아처숄더','어깨장식'),
('아케인셰이드아처케이프','망토'),
('아케인셰이드파이렛글러브','장갑'),
('아케인셰이드파이렛슈즈','신발'),
('아케인셰이드파이렛숄더','어깨장식'),
('아케인셰이드파이렛케이프','망토'),
('앱솔랩스나이트글러브','장갑'),
('앱솔랩스나이트슈즈','신발'),
('앱솔랩스나이트숄더','어깨장식'),
('앱솔랩스나이트케이프','망토'),
('앱솔랩스나이트헬름','모자'),
('앱솔랩스메이지글러브','장갑'),
('앱솔랩스메이지슈즈','신발'),
('앱솔랩스메이지숄더','어깨장식'),
('앱솔랩스메이지케이프','망토'),
('앱솔랩스메이지헬름','모자'),
('앱솔랩스시프글러브','장갑'),
('앱솔랩스시프슈즈','신발'),
('앱솔랩스시프숄더','어깨장식'),
('앱솔랩스시프케이프','망토'),
('앱솔랩스시프헬름','모자'),
('앱솔랩스아처글러브','장갑'),
('앱솔랩스아처슈즈','신발'),
('앱솔랩스아처숄더','어깨장식'),
('앱솔랩스아처케이프','망토'),
('앱솔랩스아처헬름','모자'),
('앱솔랩스파이렛글러브','장갑'),
('앱솔랩스파이렛슈즈','신발'),
('앱솔랩스파이렛숄더','어깨장식'),
('앱솔랩스파이렛케이프','망토'),
('앱솔랩스파이렛헬름','모자'),
('샤이니레드나이트마이스터심볼','얼굴장식'),
('샤이니레드메이지마이스터심볼','얼굴장식'),
('샤이니레드시프마이스터심볼','얼굴장식'),
('샤이니레드아처마이스터심볼','얼굴장식'),
('샤이니레드파이렛마이스터심볼','얼굴장식'),
('루즈컨트롤머신마크','얼굴장식'),
('트와일라이트마크','얼굴장식'),
('파풀라투스마크','눈장식'),
('마력이깃든안대','눈장식'),
('골든클로버벨트','벨트'),
('분노한자쿰의벨트','벨트'),
('타일런트리카온벨트','벨트'),
('타일런트알테어벨트','벨트'),
('타일런트히아데스벨트','벨트'),
('타일런트케이론벨트','벨트'),
('타일런트헤르메스벨트','벨트'),
('몽환의벨트','벨트'),
('마이스터이어링','귀고리'),
('데아시두스이어링','귀고리'),
('에스텔라이어링','귀고리'),
('오션글로우이어링','귀고리'),
('커맨더포스이어링','귀고리'),
('고통의근원','펜던트'),
('도미네이터펜던트','펜던트'),
('매커네이터펜던트','펜던트'),
('데이브레이크펜던트','펜던트'),
('라이징썬펜던트','펜던트'),
('베어스퍼플펜던트','펜던트'),
('아울스퍼플펜던트','펜던트'),
('울프스퍼플펜던트','펜던트'),
('피콕스퍼플펜던트','펜던트'),
('아케인셰이드튜너','무기'),
('이글아이던위치팬츠','상의'),
('이글아이레인져후드','상의'),
('이글아이어새신셔츠','상의'),
('이글아이워리어아머','상의'),
('이글아이원더러코트','상의'),
('트릭스터던위치팬츠','하의'),
('트릭스터레인져팬츠','하의'),
('트릭스터어새신팬츠','하의'),
('트릭스터워리어팬츠','하의'),
('트릭스터원더러팬츠','하의'),
('하이네스던위치햇','모자'),
('하이네스레인져베레','모자'),
('하이네스어새신보닛','모자'),
('하이네스워리어헬름','모자'),
('하이네스원더러햇','모자'),
('로얄블랙메탈숄더','어깨장식'),
('노블브레이슬릿','보조무기'),
('핑크빛성배','포켓아이템'),
('저주받은녹의마도서','포켓아이템'),
('저주받은청의마도서','포켓아이템'),
('저주받은적의마도서','포켓아이템'),
('저주받은황의마도서','포켓아이템');