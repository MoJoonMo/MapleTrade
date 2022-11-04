import cv2 as cv
import numpy as np
import pymysql as mysql

from function import gui as gf

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
con = mysql.connect(host='database-1.caeooxqk7wut.us-west-2.rds.amazonaws.com', user='midadm', password ='!dlatl00', db='maple_db',charset='utf8')
cur = con.cursor()

sql = "select * from search_item_list where ifnull(use_yn,'Y') = 'Y' "
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
            edge_list = ['center','center_archer','center_chief','center_chief','center_knight','center_magician','center_pirate','center_xenon','potenability','upg','potenoption']
            starforce_list = ['star']
            #스타포스 인식
            star_cnt = 0
            for sf in starforce_list:
                w, h, loc = gf.matchTemplate(img_gray,sf, 0.9) 
                for pt in zip(*loc[::-1]):
                    break_yn = 'N'
                    value_kind = "none"
                    for xloc in range(w):
                        for yloc in range(h):
                            (b, g, r) = img_rgb[pt[1]+xloc, pt[0]+yloc]
                            #print(pt[1]+xloc,pt[0]+yloc,b,g,r)
                            if b <=2 and g>= 220 and g<=222 and r>= 254:
                                star_cnt = star_cnt + 1
                                break_yn = "Y"
                                break
                        if break_yn == "Y":
                            break
            
            for eg in edge_list: 
                w, h, loc = gf.matchTemplate(img_gray,'edge/' + eg, 0.6) 
                for pt in zip(*loc[::-1]):
                    if eg == "upg" or eg == "potenability":
                        standard_mid = [pt[1],pt[0],eg]
                    elif eg == "potenoption":
                        standard_end = [pt[1],pt[0],eg]
                    else:
                        standard = [pt[1],pt[0],eg] # y,x,name
                    
            y_loc = 0

            #이미지에서 find_list math 가져오기
            arr = gf.getItemDetail(img_gray,img_rgb)
            answer = gf.print_answer(arr,standard,standard_mid,standard_end)
            answer.append('스타포스',star_cnt,"","","","original")
            get_index_sql = "SELECT nextval('sell_item_option')"
            cur.execute(get_index_sql)
            rslt = cur.fetchone()
            
            for insert_data in answer:
                #print(insert_data)
                print("INSERT INTO sell_item_option(`item_option_id`, `option_name`, `first_amt`, `second_amt`,`third_amt`,`forth_amt`,`crt_id`,`crt_dt`,`option_kind`) VALUES ('"+str(rslt[0])+"',ifnull('"+insert_data[0] +"','0'),ifnull('"+insert_data[1] +"','0'),ifnull('"+insert_data[2] +"','0'),ifnull('"+insert_data[3] +"','0'),ifnull('"+insert_data[4] +"','0'),'DB',date_format(now(), '%Y%m%d%H%i%s'),ifnull('"+insert_data[4]+"','0') )")
                sql = "INSERT INTO sell_item_option(`item_option_id`, `option_name`, `first_amt`, `second_amt`,`third_amt`,`forth_amt`,`crt_id`,`crt_dt`,`option_kind`) VALUES ('"+str(rslt[0])+"',ifnull('"+insert_data[0] +"','0'),ifnull('"+insert_data[1] +"','0'),ifnull('"+insert_data[2] +"','0'),ifnull('"+insert_data[3] +"','0'),ifnull('"+insert_data[4] +"','0'),'DB',date_format(now(), '%Y%m%d%H%i%s'),ifnull('"+insert_data[4]+"','0') )"    
                #insert_data[0] +","+insert_data[1] +","+insert_data[2]+","+insert_data[3]+","+insert_data[4],")"
                cur.execute(sql)
                #rows = cur.fetchall()
                #print(rows)
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
