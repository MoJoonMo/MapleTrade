import cv2 as cv
import numpy as np
import pandas as pd 
import pyautogui as pag
import win32gui 
import time as t
import pymysql as mysql
import pyperclip
from ctypes import *


#키보드 조작 부분
dd_dll = windll.LoadLibrary('G:\\AI\\python\\DD94687.64.dll')

st = dd_dll.DD_btn(0) #classdd 초기설정
if st==1:
    print("OK")
else:
    print("Error")
    exit(101)

mouseleftdown = 1
mouseleftup = 2
mouserightdown = 4
mouserightup = 8
mousewheeldown = 16
mousewheelup = 32

def mouse_move(kind, item_name):
    hwnd = win32gui.FindWindow(None, "MapleStory")
    win32gui.SetForegroundWindow(hwnd) 
    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (x, y))
    x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
    if kind == "find":
        dd_dll.DD_mov(x+105, y+56)
        dd_dll.DD_btn(mouseleftdown)
        t.sleep(0.1)
        dd_dll.DD_btn(mouseleftup)
        t.sleep(0.1)
        dd_dll.DD_btn(mouseleftdown)
        t.sleep(0.1)
        dd_dll.DD_btn(mouseleftup)
        t.sleep(0.1)
        pyperclip.copy(item_name)
        dd_dll.DD_key(600,1)#Ctrl
        dd_dll.DD_key(504,1)#v
        t.sleep(0.1)
        dd_dll.DD_key(504,2)
        dd_dll.DD_key(600,2)
        dd_dll.DD_key(313,1)
        t.sleep(0.1)
        dd_dll.DD_key(313,2)
        t.sleep(0.1)
        dd_dll.DD_key(313,1)
        t.sleep(0.1)
        dd_dll.DD_key(313,2)
        t.sleep(0.1)
        dd_dll.DD_key(313,1)
        t.sleep(0.1)
        dd_dll.DD_key(313,2)
    if kind == "next":
        dd_dll.DD_mov(x+1, y+1)
        t.sleep(0.1)
        dd_dll.DD_mov(x+675, y+135)
        t.sleep(0.1)
        dd_dll.DD_btn(mouseleftdown)
        t.sleep(0.1)
        dd_dll.DD_btn(mouseleftup)
        t.sleep(0.1)

def screenshot(idx):
    dd_dll.DD_mov(0,0)
    t.sleep(0.1)
    hwnd = win32gui.FindWindow(None, "MapleStory")
    if hwnd:   
        win32gui.SetForegroundWindow(hwnd) 
        t.sleep(0.1)
        x, y, x1, y1 = win32gui.GetClientRect(hwnd)
        x, y = win32gui.ClientToScreen(hwnd, (x, y))
        x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
        if idx == -1:
            im = pag.screenshot('price.png',region=(x+580, y, 150, y1))
        elif idx == -2:
            im = pag.screenshot('date.png',region=(x+880, y, 100, y1))
        else:

            dd_dll.DD_mov(x+320, y+200+56*idx)
            t.sleep(0.2)
            dd_dll.DD_mov(x+290, y+200+56*idx)
            im = pag.screenshot('screenshot.png',region=(x, y, x1, y1))
        return x,y,x1,y1
    else:
        print('Window not found!')
        
def getItemData(kind, loops):
    price = ""
    brr = []

    img2_rgb = cv.imread(kind + '.png')
    img2_gray = cv.cvtColor(img2_rgb, cv.COLOR_BGR2GRAY)

    for index, fl in enumerate(num_list):
        template = cv.imread('image_data_original/'+fl+'.png',0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img2_gray,template,cv.TM_CCOEFF_NORMED)
        threshold = 0.95
        loc = np.where( res >= threshold) 

        for pt in zip(*loc[::-1]):
            if pt[1] >= 190+loops*56 and pt[1] <= 203+loops*56:
                brr.append([pt[1],pt[0],num_list_name[index]]) # y,x,name
                cv.rectangle(img2_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv.imwrite('res2.png',img2_rgb)
    brr.sort()
    for index in brr:
        price = price + index[2]
    return price


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





#dd_dll.DD_btn(mouseleftdown)
#이 사이에 딜레이 주면 오래 누르고 있기 가능
#dd_dll.DD_btn(mouseleftup)
"""
pyperclip.copy("lemon7z.tistory.com") -- ctrl + c
dd_dll마이스터링
.DD_key(600,1)#Ctrl
dd_dll.DD_key(504,1)#v
dd_dll.DD_key(504,2)
dd_dll.DD_key(600,2)
"""





#############경매장검색
item_name = "가디언 엔젤 링"
mouse_move("find",item_name)
#페이지끝까지 펼치기

########페이지 검색

for pages in range(10):
    ###############페이지 검색
    answer = [] # [["name","first","second","third","forth"]]

    jdx = 0
    maple_screen = screenshot(-1)
    maple_screen = screenshot(-2)


    con = mysql.connect(host='database-1.caeooxqk7wut.us-west-2.rds.amazonaws.com', user='midadm', password ='!dlatl00', db='maple_db',charset='utf8')
    cur = con.cursor()





    for loops in range(0,9):
        idx = -1
        maple_screen = screenshot(loops)
        img_rgb = cv.imread('screenshot.png')
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

        find_list_name = ['STR','DEX','INT','LUK','공격력','마력','몬스터 방어율 무시','방어력','보스 몬스터 공격 시 데미지','업그레이드 가능 횟수','올스탯','점프력','최대 HP','최대 MP','1','2','3','4','5','6','7','8','9','0','(',')','+','%','%','데미지','가위 사용 가능 횟수','모든 스킬 재사용 대기시간','캐릭터 기준 10레벨 당','크리티컬 데미지']
        find_list = ['STR','DEX','INT','LUK','att','mtt','igd','def','btt','upg','all','jmp','mhp','mmp','1','2','3','4','5','6','7','8','9','0','open_bracket','close_bracket','plus','percent','percent2','dmg','scissors','cool','perlevel','cridmg']

        num_list = ['0','1','2','3','4','5','6','7','8','9','1_2','4_2','7_2','2_2']
        num_list_name = ['0','1','2','3','4','5','6','7','8','9','1','4','7','2']

        arr = []
        standard = []
        edge_list = ['center']
        for eg in edge_list:
            template = cv.imread('image_data_original/edge/'+eg+'.png',0)
            w, h = template.shape[::-1]
            res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
            threshold = 0.80
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

        #final_text = ""
        #text = ""


        for a in arr:
            if a[0] > standard[0] and a[1] < standard[1] + 240 and standard[1] - 40< a[1]:
                if a[0] > y_loc + 6 :
                    if a[2] != "(" and a[2] != "+" and a[2] != ")":
                        y_loc = a[0]
                        #final_text += text + "\n"
                        #text = a[2] + " "
                        idx = idx + 1
                        jdx = 0
                        if a[2] == "업그레이드 가능 횟수":
                            jdx = 1
                        answer.append([a[2],"","","",""])
                else:
                    #text += a[2]
                    if a[2] == "(" or a[2] == "+" or a[2] == ")":
                        jdx = jdx + 1
                    else:
                        answer[idx][jdx] = answer[idx][jdx] + a[2]
        price = getItemData("price",loops)
        sell_date = getItemData("date",loops)
        

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
        #final_text += text
        print("INSERT INTO sell_item (`item_name`, `item_sell_date`, `item_price`, `item_option_id`, `crt_id`, `crt_dt`) VALUES ('" + item_name + "','" + sell_date + "','" + price + "'," + str(rslt[0]) + ",'DB',date_format(now(), '%Y%m%d%H%i%s'))")
        sql = "INSERT INTO sell_item (`item_name`, `item_sell_date`, `item_price`, `item_option_id`, `crt_id`, `crt_dt`) VALUES ('" + item_name + "','" + sell_date + "','" + price + "'," + str(rslt[0]) + ",'DB',date_format(now(), '%Y%m%d%H%i%s'))"
        cur.execute(sql)
        answer=[]
    con.commit()
    mouse_move("next","")
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

