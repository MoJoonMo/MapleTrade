

import cv2 as cv
import numpy as np

from function import gui as gf



#(b, g, r) = cv2_image[0, 0]        
img_rgb = cv.imread('maple_5.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

find_list_name = ['STR','DEX','INT','LUK','공격력','마력','몬스터 방어율 무시','방어력','보스 몬스터 공격 시 데미지','업그레이드 가능 횟수','올스탯','점프력','최대 HP','최대 MP','1','2','3','4','5','6','7','8','9','0','(',')','+','%','%','데미지','가위 사용 가능 횟수','모든 스킬 재사용 대기시간','캐릭터 기준 10레벨 당','크리티컬 데미지']
find_list = ['STR','DEX','INT','LUK','att','mtt','igd','def','btt','upg','all','jmp','mhp','mmp','1','2','3','4','5','6','7','8','9','0','open_bracket','close_bracket','plus','percent','percent2','dmg','scissors','cool','perlevel','cridmg']

arr = []
standard = []
standard_mid = []
standard_end = []
edge_list = ['center','center_archer','center_chief','center_chief','center_knight','center_magician','center_pirate','center_xenon','potenability','upg','potenoption']

starforce_list = ['star']
#스타포스 인식
star_cnt =0
for sf in starforce_list:
    template = cv.imread('image_data_original/'+sf+'.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.90
    loc = np.where( res >= threshold)
    
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

#능력치 부분 위치 찾기 standard 에 넣음
for eg in edge_list:
    template = cv.imread('image_data_original/edge/'+eg+'.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.60
    loc = np.where( res >= threshold) 

    for pt in zip(*loc[::-1]):
        if eg == "upg" or eg == "potenability":
            standard_mid = [pt[1],pt[0],eg]
        elif eg == "potenoption":
            standard_end = [pt[1],pt[0],eg]
        else:
            standard = [pt[1],pt[0],eg] # y,x,name
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        
    cv.imwrite('res.png',img_rgb)

"""
upg, potenability
업그레이드 가능 횟수 or 잠재능력 부분 찾기 => 그 윗부분이 메인 옵션
potenoption
잠재옵션 찾기, 있으면 그 밑으로 잠재옵션
addipotenoption
에디셔널잠재옵션 찾기, 있으면 여기까지 잠재옵션, 여기부터 에디셔널 잠재옵션
"""
for index, fl in enumerate(find_list):
    template = cv.imread('image_data_original/'+fl+'.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where( res >= threshold) 
    
    for pt in zip(*loc[::-1]):
        #cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        #print(pt[0],pt[1])
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
        #print(find_list_name[index],b,g,r,pt[0],pt[1],w,h,value_kind)

#데이터 넣는 부분

arr.sort()

answer = gf.print_answer(arr,standard,standard_mid,standard_end) # 0 : name / 1 : total / 2 : basic / 3 : chuop / 4 : starforce + scroll
answer.append(["스타포스",str(star_cnt),"","",""])
for ii in answer:
    print(ii)
"""
answer = []
idx = -1
jdx = 0
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
                if jdx == 3 and a[3] == "scroll":
                    jdx = 4
            else:
                #jdx = 1,4 : scroll / 2 : none / 3 : chuop
                
                answer[idx][jdx] = answer[idx][jdx] + a[2]
"""
