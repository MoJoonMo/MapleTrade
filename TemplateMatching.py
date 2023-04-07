import cv2 as cv
import numpy as np
import pymysql as mysql

from config import db as db
from sql import select_sql as select_sql
from sql import insert_sql as insert_sql
from function import gui as gf
from function import findImage as fi

        #### 경매장
        #시세탭에서 아이템 검색
        #너무 많으면 어쩌고 저쩌고 창닫음
        #특정 날짜에 팔린 아이템인지 확인한다. (반복시작)
        #맞다면 그 아이템에 커서를 올려 아이템 정보를 확인 후, 기록 후 다음 아이템을 본다.
        #만약 다음 아이템이 없다면, 다음페이지로 넘어간 다음 맨위의 아이템을 확인한다. (반복끝)
        #아니라면 다른 이름의 아이템을 검색한다
        #### 템진단
        #im에서 장비창 영역 찾고, 
        #Main 장비탭으로 이동한 다음 
        #각 부위별로 마우스 커서 가져다둬서 아이템 정보 screentshot 찍는다.
con = mysql.connect(host=db.host, user=db.user, password =db.password, db=db.db, charset=db.charset)
cur = con.cursor()

sql = select_sql.search_item_list("Y")
cur.execute(sql)
item_name = cur.fetchall()

for il in item_name:
    print(il[0])

    gf.mouse_move("find",il[0])
    for pages in range(50): #페이지
        ###############페이지 검색
        answer = [] 
    
        jdx = 0
        maple_screen = gf.screenshot(-1)
        maple_screen = gf.screenshot(-2)

        for loops in range(0,9): #한페이지에 9개
            price = gf.getItemData("price",loops)
            sell_date = gf.getItemData("date",loops)
            if int(price) < int(il[3]):
                continue
            idx = -1
            maple_screen = gf.screenshot(loops)
            img_rgb = cv.imread('screenshot.png')
            img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

            arr = []
            standard = []
            standard_mid = [0,0,'0']
            standard_end = [0,0,'0']
            #추옵, 작, 스타포스, 윗잠, 아랫잠

            star_cnt = fi.findImage(img_gray, img_rgb, "starforce") #스타포스 인식
            standard, standard_mid, standard_end = fi.findImage(img_gray, img_rgb, "standard") #옵션 위치 확인

            #이미지에서 find_list math 가져오기
            arr = gf.getItemDetail(img_gray,img_rgb) #추옵, 작, 윗잠, 아랫잠
            answer, poten, addipoten = gf.print_answer(arr,standard,standard_mid,standard_end)
            answer.append(['스타포스',str(star_cnt),"","","","","original"])

            print(str(star_cnt))
            print(answer)
            print(poten)
            print(addipoten)
            
            get_index_sql = select_sql.search_nextval("sell_item_option") 

            
            cur.execute(get_index_sql)
            rslt = cur.fetchone()
            
            for insert_data in answer:
                #print(insert_data)
                #print("INSERT INTO sell_item_option(`item_option_id`, `option_name`, `first_amt`, `second_amt`,`third_amt`,`forth_amt`,`crt_id`,`crt_dt`,`option_kind`) VALUES ('"+str(rslt[0])+"',ifnull('"+insert_data[0] +"','0'),ifnull('"+insert_data[1] +"','0'),ifnull('"+insert_data[2] +"','0'),ifnull('"+insert_data[3] +"','0'),ifnull('"+insert_data[4] +"','0'),'DB',date_format(now(), '%Y%m%d%H%i%s'),ifnull('"+insert_data[5]+"','0') )")
                print(insert_data)
                sql = "INSERT INTO sell_item_option(`item_option_id`, `option_name`, `first_amt`, `second_amt`,`third_amt`,`forth_amt`,`fifth_amt`,`crt_id`,`crt_dt`,`option_kind`) VALUES ('"+str(rslt[0])+"',ifnull('"+insert_data[0] +"','0'),ifnull('"+insert_data[1] +"','0'),ifnull('"+insert_data[2] +"','0'),ifnull('"+insert_data[3] +"','0'),ifnull('"+insert_data[4] +"','0'),ifnull('"+insert_data[5] +"','0'),'DB',date_format(now(), '%Y%m%d%H%i%s'),ifnull('"+insert_data[6]+"','0') )"    
                #insert_data[0] +","+insert_data[1] +","+insert_data[2]+","+insert_data[3]+","+insert_data[4],")"
                cur.execute(sql)
                #rows = cur.fetchall()
                #print(rows)
            for insert_data in poten:
                print(insert_data)
                sql = "INSERT INTO sell_item_option(`item_option_id`, `option_name`, `first_amt`, `second_amt`,`third_amt`,`forth_amt`,`fifth_amt`,`crt_id`,`crt_dt`,`option_kind`) VALUES ('"+str(rslt[0])+"',ifnull('"+insert_data[0] +"','0'),ifnull('"+insert_data[1] +"','0'),ifnull('"+insert_data[2] +"','0'),ifnull('"+insert_data[3] +"','0'),ifnull('"+insert_data[4] +"','0'),ifnull('"+insert_data[5] +"','0'),'DB',date_format(now(), '%Y%m%d%H%i%s'),ifnull('"+insert_data[6]+"','0') )"    
                cur.execute(sql)

            for insert_data in addipoten:
                print(insert_data)
                sql = "INSERT INTO sell_item_option(`item_option_id`, `option_name`, `first_amt`, `second_amt`,`third_amt`,`forth_amt`,`fifth_amt`,`crt_id`,`crt_dt`,`option_kind`) VALUES ('"+str(rslt[0])+"',ifnull('"+insert_data[0] +"','0'),ifnull('"+insert_data[1] +"','0'),ifnull('"+insert_data[2] +"','0'),ifnull('"+insert_data[3] +"','0'),ifnull('"+insert_data[4] +"','0'),ifnull('"+insert_data[5] +"','0'),'DB',date_format(now(), '%Y%m%d%H%i%s'),ifnull('"+insert_data[6]+"','0') )"    
                cur.execute(sql)

            print("INSERT INTO sell_item (`item_name`, `item_sell_date`, `item_price`, `item_option_id`, `crt_id`, `crt_dt`) VALUES ('" + il[0] + "','" + sell_date + "','" + price + "'," + str(rslt[0]) + ",'DB',date_format(now(), '%Y%m%d%H%i%s'))")
            sql = "INSERT INTO sell_item (`item_name`, `item_sell_date`, `item_price`, `item_option_id`, `crt_id`, `crt_dt`) VALUES ('" + il[0] + "','" + sell_date + "','" + price + "'," + str(rslt[0]) + ",'DB',date_format(now(), '%Y%m%d%H%i%s'))"
            cur.execute(sql)
            answer=[]

        con.commit()
        if sell_date <= '20221100':
            break
        gf.mouse_move("next","")
        
con.close()

#dataframe = pd.DataFrame(answer)
#dataframe.to_csv("cstTest.csv", header=False, index=False)
