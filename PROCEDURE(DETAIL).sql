
CALL calc_item_detail;
SELECT * from log_table;

select *
from log_table;

select *
from search_item_detail;
delete from search_item_detail;

    select sio.option_name, sio.first_amt, sio.second_amt, sio.third_amt, sio.forth_amt
    from sell_item_option sio
    where sio.item_option_id = 1360;

	select 	si.item_name,
			si.item_sell_date,
			si.item_price,
            si.item_option_id
	from sell_item si
    where si.item_option_id between 1360 and 1370;
    
DELIMITER $$
DROP PROCEDURE `calc_item_detail`;
CREATE PROCEDURE `calc_item_detail` (

)
BEGIN
	DECLARE done INT DEFAULT FALSE;
    DECLARE done2 INT DEFAULT FALSE;
	DECLARE strz INT;
	DECLARE strp INT;
	DECLARE strl INT;
	DECLARE dexz INT;
	DECLARE dexp INT;
	DECLARE dexl INT;
	DECLARE intz INT;
	DECLARE intp INT;
	DECLARE intl INT;
	DECLARE lukz INT;
	DECLARE lukp INT;
	DECLARE lukl INT;
	DECLARE allz INT;
	DECLARE allp INT;
	DECLARE att INT;
	DECLARE attp INT;
	DECLARE mtt INT;
	DECLARE mttp INT;
	DECLARE btt INT;
	DECLARE igd INT;
	DECLARE dmg INT;
	DECLARE upg INT;
	DECLARE mhpz INT;
    DECLARE mhpp INT;
	DECLARE cool INT;
	DECLARE cridmg INT;    
    DECLARE option_kind VARCHAR(3);
    DECLARE percent_yn VARCHAR(3);
    DECLARE p_item_option_id INT;
    DECLARE v_item_name VARCHAR(32);
    DECLARE v_item_sell_date VARCHAR(32);
	DECLARE v_item_price VARCHAR(32);
	DECLARE	v_item_option_id INT;
    DECLARE v_option_name VARCHAR(200);
	DECLARE v_first_amt VARCHAR(50);
	DECLARE v_second_amt VARCHAR(50);
	DECLARE v_third_amt VARCHAR(50);
	DECLARE v_forth_amt VARCHAR(50);
    DECLARE v_log VARCHAR(10000);
	DECLARE cursor1 CURSOR FOR 
	select 	si.item_name,
			si.item_sell_date,
			si.item_price,
            si.item_option_id
	from sell_item si
    -- where si.item_option_id BETWEEN 1360 AND 1370
    ;
    
    DECLARE cursor_detail CURSOR FOR
    select sio.option_name, sio.first_amt, sio.second_amt, sio.third_amt, sio.forth_amt
    from sell_item_option sio
    where sio.item_option_id = p_item_option_id
    ;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
	
    OPEN cursor1;
    
    
	item_loop: LOOP
    
		FETCH 	cursor1 
		INTO 	v_item_name,
				v_item_sell_date,
				v_item_price,
				v_item_option_id
				;
                
		INSERT INTO log_table
        VALUES (CONCAT(v_item_name, " " , v_item_sell_Date, " ", v_item_price, " ",v_item_option_id));

		IF done THEN
		  LEAVE item_loop;
		END IF;
				
		SET p_item_option_id = v_item_option_id;
		OPEN cursor_detail;
		SET strz=0;
		SET strp=0;
		SET strl=0;
		SET dexz=0;
		SET dexp=0;
		SET dexl=0;
		SET intz=0;
		SET intp=0;
		SET intl=0;
		SET lukz=0;
		SET lukp=0;
		SET lukl=0;
		SET allz=0;
		SET allp=0;
		SET att=0;
		SET attp=0;
		SET mtt=0;
		SET mttp=0;
		SET btt=0;
		SET igd=0;
		SET dmg=0;
		SET upg=0;
		SET mhpp=0;
        SET mhpz=0;
		SET cool=0;
		SET cridmg=0;
		SET v_log="";
        SET done = FALSE;
        
		detail_loop: LOOP
			FETCH 	cursor_detail
			INTO	v_option_name,
					v_first_amt,
					v_second_amt,
					v_third_amt,
					v_forth_amt
			;
            
            IF done THEN
				SET done = false;
				LEAVE detail_loop;
			END IF;
            
			IF v_option_name = "STR" THEN
				IF substr(v_first_amt,-1) = "%" THEN
					SET strp = strp +SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
				ELSE 
					SET strz = strz + v_first_amt;
				END IF;
			ELSEIF v_option_name = "DEX" THEN
				IF substr(v_first_amt,-1) = "%" THEN
					SET dexp = dexp + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
				ELSE 
					SET dexz = dexz + v_first_amt;
				END IF; 
			ELSEIF v_option_name = "INT" THEN
				IF substr(v_first_amt,-1) = "%" THEN
					SET intp = intp + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
				ELSE 
					SET intz = intz + v_first_amt;
				END IF;
			ELSEIF v_option_name = "LUK" THEN
				IF substr(v_first_amt,-1) = "%" THEN
					SET lukp = lukp + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
				ELSE 
					SET lukz = lukz + v_first_amt;
				END IF;
			ELSEIF v_option_name = "올스탯" THEN
				IF substr(v_first_amt,-1) = "%" THEN
					SET allp = allp + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
				ELSE 
					SET allz = allz + v_first_amt;
				END IF;
			ELSEIF v_option_name = "공격력" THEN
				IF substr(v_first_amt,-1) = "%" THEN
					SET attp = attp + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
				ELSE 
					SET att = att + v_first_amt;
				END IF;
			ELSEIF v_option_name = "데미지" THEN
				SET dmg = dmg + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
			ELSEIF v_option_name = "마력" THEN
				IF substr(v_first_amt,-1) = "%" THEN
					SET mttp = mttp + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
				ELSE 
					SET mtt = mtt + v_first_amt;
				END IF;
			ELSEIF v_option_name = "크리티컬 데미지데미지" THEN
				SET cridmg = cridmg + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
			ELSEIF v_option_name = "캐릭터 기준 10레벨 당10STR" THEN
				SET strl = strl + v_first_amt;
			ELSEIF v_option_name = "캐릭터 기준 10레벨 당10DEX" THEN
				SET dexl = dexl + v_first_amt;
			ELSEIF v_option_name = "캐릭터 기준 10레벨 당10INT" THEN
				SET intl = intl + v_first_amt;
			ELSEIF v_option_name = "캐릭터 기준 10레벨 당10LUK" THEN
				SET lukl = lukl + v_first_amt;
			ELSEIF v_option_name = "모든 스킬 재사용 대기시간2" THEN
				SET cool = cool + 2;
			ELSEIF v_option_name = "모든 스킬 재사용 대기시간1" THEN
				SET cool = cool + 1;
			ELSEIF v_option_name = "보스 몬스터 공격 시 데미지데미지" THEN
				SET btt = btt + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
			ELSEIF v_option_name = '몬스터 방어율 무시' THEN
				SET igd = igd + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
			ELSEIF v_option_name = '최대 HP' THEN
				IF substr(v_first_amt,-1) = "%" THEN
					SET mhpp = mhpp + SUBSTRING(v_first_amt,1,CHAR_LENGTH(v_first_amt)-1);
				ELSE
					SET mhpz = mhpz + v_first_amt;
				END IF;
            END IF;

            
		END LOOP;
        CLOSE cursor_detail;

        
		INSERT INTO search_item_detail(
            item_name,item_sell_date,item_price,item_option_id,
			strz,strp,strl,dexz,dexp,dexl,intz,intp,intl,lukz,lukp,lukl,
			allz,allp,att,attp,mtt,mttp,btt,igd,dmg,
			mhpp,mhpz,cool,cridmg
        ) values(
            v_item_name,v_item_sell_date,v_item_price,v_item_option_id,
            strz,strp,strl,dexz,dexp,dexl,intz,intp,intl,lukz,lukp,lukl,
            allz,allp,att,attp,mtt,mttp,btt,igd,dmg,
            mhpp,mhpz,cool,cridmg
        );
	END LOOP;
    CLOSE cursor1;
END;

