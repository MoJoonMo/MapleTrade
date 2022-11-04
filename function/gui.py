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


def print_answer(arr,standard,standard_mid,standard_end):
    answer = []
    idx = -1
    jdx = 0
    y_loc = 0
    for a in arr:
        #print(standard)

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
                    if jdx >= 3 and a[3] == "scroll":
                        jdx = 4
                    
                else:
                    #jdx = 1,4 : scroll / 2 : none / 3 : chuop
                    if a[3] == "scroll_minus" and jdx < 4:
                        jdx = 4
                        answer[idx][jdx] = "-"    
                    answer[idx][jdx] = answer[idx][jdx] + a[2]
    return answer
