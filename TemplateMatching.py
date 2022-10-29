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

#############경매장검색



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
            if int(price) <16000000:
                continue
            idx = -1
            maple_screen = gf.screenshot(loops)
            img_rgb = cv.imread('screenshot.png')
            img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

            find_list_name = ['STR','DEX','INT','LUK','공격력','마력','몬스터 방어율 무시','방어력','보스 몬스터 공격 시 데미지','업그레이드 가능 횟수','올스탯','점프력','최대 HP','최대 MP','1','2','3','4','5','6','7','8','9','0','(',')','+','%','%','데미지','가위 사용 가능 횟수','모든 스킬 재사용 대기시간','캐릭터 기준 10레벨 당','크리티컬 데미지']
            find_list = ['STR','DEX','INT','LUK','att','mtt','igd','def','btt','upg','all','jmp','mhp','mmp','1','2','3','4','5','6','7','8','9','0','open_bracket','close_bracket','plus','percent','percent2','dmg','scissors','cool','perlevel','cridmg']

            arr = []
            standard = []
            edge_list = ['center']
            for eg in edge_list:
                template = cv.imread('image_data_original/edge/'+eg+'.png',0)
                w, h = template.shape[::-1]
                res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
                threshold = 0.70
                loc = np.where( res >= threshold) 

                for pt in zip(*loc[::-1]):
                    standard = [pt[1],pt[0],eg] # y,x,name
                    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
                    
                cv.imwrite('res.png',img_rgb)
                
            y_loc = 0
            for index, fl in enumerate(find_list):
                template = cv.imread('image_data_original/'+fl+'.png',0)
                w, h = template.shape[::-1]
                res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
                threshold = 0.95
                loc = np.where( res >= threshold) 
                
                for pt in zip(*loc[::-1]):
                    arr.append([pt[1],pt[0],find_list_name[index]]) # y,x,name
                    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

                cv.imwrite('res.png',img_rgb)

            #데이터 넣는 부분

            arr.sort()

            for a in arr:
                if a[0] > standard[0] and a[1] < standard[1] + 240 and standard[1] - 40< a[1]:
                    if a[0] > y_loc + 6 :
                        if a[2] != "(" and a[2] != "+" and a[2] != ")":
                            y_loc = a[0]
                            idx = idx + 1
                            jdx = 0
                            if a[2] == "업그레이드 가능 횟수":
                                jdx = 1
                            answer.append([a[2],"","","",""])
                    else:
                        if a[2] == "(" or a[2] == "+" or a[2] == ")":
                            jdx = jdx + 1
                        else:
                            answer[idx][jdx] = answer[idx][jdx] + a[2]
            

            #answer.append(["price",arr_num,"","",""])
            get_index_sql = "SELECT nextval('sell_item_option')"
            cur.execute(get_index_sql)
            rslt = cur.fetchone()
            
            for insert_data in answer:
                
                #print(insert_data)
                #print("INSERT INTO sell_item_option(`item_option_id`, `option_name`, `first_amt`, `second_amt`,`third_amt`,`forth_amt`) VALUES (nextval('sell_item_option'),ifnull('"+insert_data[0] +"','0'),ifnull('"+insert_data[1] +"','0'),ifnull('"+insert_data[2] +"','0'),ifnull('"+insert_data[3] +"','0'),ifnull('"+insert_data[4] +"','0'))" )
                sql = "INSERT INTO sell_item_option(`item_option_id`, `option_name`, `first_amt`, `second_amt`,`third_amt`,`forth_amt`,`crt_id`,`crt_dt`) VALUES ('"+str(rslt[0])+"',ifnull('"+insert_data[0] +"','0'),ifnull('"+insert_data[1] +"','0'),ifnull('"+insert_data[2] +"','0'),ifnull('"+insert_data[3] +"','0'),ifnull('"+insert_data[4] +"','0'),'DB',date_format(now(), '%Y%m%d%H%i%s') )"    
                #insert_data[0] +","+insert_data[1] +","+insert_data[2]+","+insert_data[3]+","+insert_data[4],")"
                cur.execute(sql)
                #rows = cur.fetchall()
                #print(rows)
            print("INSERT INTO sell_item (`item_name`, `item_sell_date`, `item_price`, `item_option_id`, `crt_id`, `crt_dt`) VALUES ('" + il[0] + "','" + sell_date + "','" + price + "'," + str(rslt[0]) + ",'DB',date_format(now(), '%Y%m%d%H%i%s'))")
            sql = "INSERT INTO sell_item (`item_name`, `item_sell_date`, `item_price`, `item_option_id`, `crt_id`, `crt_dt`) VALUES ('" + il[0] + "','" + sell_date + "','" + price + "'," + str(rslt[0]) + ",'DB',date_format(now(), '%Y%m%d%H%i%s'))"
            cur.execute(sql)
            answer=[]

        con.commit()
        if sell_date <= '20221000':
            break
        gf.mouse_move("next","")

        
con.close()










#dataframe = pd.DataFrame(answer)
#dataframe.to_csv("cstTest.csv", header=False, index=False)

# y,x,name 으로 받은다음

# y로 정렬
# y같은것끼리 가져온다음, x로 정렬
# 그 다음 name 읽는다

"""
import numpy as np
arr = np.array([[4, 3, 5], [6, 1, 2], [9, 7, 8], [11, 10, 12]])
print(np.sort(arr, axis=0)[::-1])

결과값: 
[[11 10 12]
[ 9  7  8]
[ 6  3  5]
[ 4  1  2]] 
"""

