import win32gui 
import pyperclip
import pandas as pd 
import pyautogui as pag
import time as t
from ctypes import *
import cv2 as cv
import numpy as np


mouseleftdown = 1
mouseleftup = 2
mouserightdown = 4
mouserightup = 8
mousewheeldown = 16
mousewheelup = 32

num_list = ['0','1','2','3','4','5','6','7','8','9','1_2','4_2','7_2','2_2']
num_list_name = ['0','1','2','3','4','5','6','7','8','9','1','4','7','2']

dd_dll = windll.LoadLibrary('./DD94687.64.dll')

st = dd_dll.DD_btn(0) #classdd 초기설정
if st==1:
    print("OK")
else:
    print("Error")
    exit(101)

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
  #  if kind == "equip":
        
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
        
        elif idx == -3: #장비창 screenshot
            #일단 전체 screenshot
            pag.screenshot('screenshot.png',region=(x,y,x1,y1))
            #장비창 상단(equip_inven_main)을 찾는다. 
            img_rgb = cv.imread('screenshot.png')
            img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
            w, h, loc = matchTemplate(img_gray,'equip/equip_inven_main',0.95)
            equip_x = 0
            equip_y = 0
            for pt in zip(*loc[::-1]):
                #cv.rectangle(img2_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                equip_x = (int)(x + pt[0])
                equip_y = (int)(y + pt[1])

            for index, l in enumerate([[118,71,'ahwk'],[118,111,'djfwkd'],[118,151,'snswkd'],[118,191,'tkddml'],[118,231,'gkdml'],[118,271,'tlsqkf'],[32,71,'qkswl1'],[32,111,'qkswl2'],[32,151,'qkswl3'],[32,191,'qkswl4'],[32,231,'vhzpt'],[75,111,'ahrrjfdl1'],[75,151,'ahrrjfdl2'],[75,191,'anrl'],[75,231,'qpfxm'],[161,151,'rnlrjfdl'],[161,191,'ruswkd'],[161,231,'wkdrkq'],[204,71,'dpaqmffpa'],[204,111,'qotwl'],[204,151,'cldgh'],[204,191,'qhwh'],[204,231,'akdxh'],[204,271,'tlawkd']]):
                dd_dll.DD_mov((int)(equip_x+ l[0]), (int)(equip_y + l[1]))    
                if index == 0:
                    t.sleep(1)
                t.sleep(0.4)
                pag.screenshot('screenshot/'+l[2]+'.png',region=(equip_x+l[0],y,264,y1))
                t.sleep(0.4)
            
            #장비창 하단(equip_show_decoration)을 찾는다
            #w, h, loc = matchTemplate(img_gray,'equip/equip_show_decoration',0.95)

            #여기를 기준으로 장비창 하나씩 스크린샷을 찍는다.            

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

def getItemDetail(img_gray,img_rgb):
    arr=[]
    find_list_name = ['STR','DEX','INT','LUK','공격력','마력','몬스터 방어율 무시','방어력','보스 몬스터 공격 시 ','업그레이드 가능 횟수','올스탯','점프력','최대 HP','최대 MP','1','2','3','4','5','6','7','8','9','0','(',')','+','%','%','데미지','가위 사용 가능 횟수','모든 스킬 재사용 대기시간','캐릭터 기준 10레벨 당','크리티컬 ']
    find_list = ['STR','DEX','INT','LUK','att','mtt','igd','def','btt','upg','all','jmp','mhp','mmp','1','2','3','4','5','6','7','8','9','0','open_bracket','close_bracket','plus','percent','percent2','dmg','scissors','cool','perlevel','cridmg']
    
    for index, fl in enumerate(find_list):
        w, h, loc = matchTemplate(img_gray,fl, 0.95) #threshold 
        for pt in zip(*loc[::-1]):
            break_yn = 'N'
            value_kind = "none"
            
            for xloc in range(w):
                for yloc in range(h):
                    (b, g, r) = img_rgb[pt[1]+yloc, pt[0]+xloc]
                    #print(pt[1]+yloc,pt[0]+xloc,b,g,r)
                    if (b >= 254 and g >= 254 and r >= 101 and r <= 103):
                        value_kind = "scroll"
                        break_yn = "Y"
                        break
                    elif b <= 2 and g >= 254 and r >= 203 and r <= 205:
                        value_kind = "chuop"
                        break_yn = "Y"
                        break
                    elif b >= 101 and b <= 103 and r >= 254 and g <= 2:
                        value_kind = "scroll_minus"
                        break_yn = "Y"
                        break
                if break_yn == "Y":
                    break
            arr.append([pt[1],pt[0],find_list_name[index],value_kind]) # y,x,name
    #데이터 넣는 부분

    arr.sort()
    return arr

def print_answer(arr,standard,standard_mid,standard_end):

    answer = []
    poten = []
    addipoten = []
    idx = -1
    jdx = 0
    idx_poten = -1
    idx_addipoten = -1
    y_loc = 0
    kind = 0
    for a in arr:
        #print(standard)
        if a[0] > standard[0] and a[1] < standard[1] + 240 and standard[1] - 40< a[1]:
            if a[0] > y_loc + 6 :
                if a[2] != "(" and a[2] != "+" and a[2] != ")":
                    y_loc = a[0]
                    kind = 0
                    jdx = 0
                    if a[2] == "업그레이드 가능 횟수" or a[2] == "가위 사용 가능 횟수":
                        jdx = 1
                    if a[0] < standard_mid[0]:
                        answer.append([a[2],"","","","","original"])
                        idx = idx + 1
                        kind = 0
                    elif a[0] < standard_end[0]:
                        poten.append([a[2],"","","","","poten"])
                        idx_poten = idx_poten + 1
                        kind = 1
                    elif a[0] >= standard_end[0]:
                        addipoten.append([a[2],"","","","","addipoten"])
                        idx_addipoten = idx_addipoten + 1
                        kind = 2

            else:
                if a[2] == "(" or a[2] == "+" or a[2] == ")":
                    jdx = jdx + 1
                    if jdx >= 3 and a[3] == "scroll":
                        jdx = 4
                    
                else:
                    #jdx = 1,4 : scroll / 2 : none / 3 : chuop
                    if a[3] == "scroll_minus" and jdx < 4:
                        jdx = 4
                        answer[idx][jdx] = "-"    
                    if kind == 0:
                        answer[idx][jdx] = answer[idx][jdx] + a[2]
                    elif kind == 1:
                        poten[idx_poten][jdx] = poten[idx_poten][jdx] + a[2]
                    elif kind == 2:
                        addipoten[idx_addipoten][jdx] = addipoten[idx_addipoten][jdx] + a[2]

    return answer, poten, addipoten

def matchTemplate(img_gray,eg,threshold):
    template = cv.imread('image_data_original/'+eg+'.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold) 
    return w, h, loc

