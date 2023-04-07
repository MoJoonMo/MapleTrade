#템진단 Main 프로그램
from function import gui as gf
from function import findImage as fi
import cv2 as cv

#아이템의 정보를 전부 받아온다.
"""
레벨/하이퍼스탯 아이템 링크 유니온 농장 패시브스킬(0,1,2,3,4,5차) 도핑

스탯 = (주스탯 X 4 + 부스탯) X 0.01 
 1) 기본 : (level * 5 + 18)*4 + 4 
 2) 아이템
 3) 

공/마 = (공/마 총합) X (1+공%/마%)
데미지% = 1 + 데미지% 합
방어율 보정

아래 는 고정

최종데미지 = 최종데미지 곱
무기 상수
평균 숙련도 보정
스킬 데미지%

크리티컬 보정
속성 내성 보정 = 1 - 몬스터의 속성내성 X (1 - 속성 내성 무시%)


"""
#전체 아이템의 능력치의 합을 보고, 스탯별 가중치를 측정한다. (ex) str = 1, dex = 0.1, str% = 8, all% = 9 등 )

#가중치를 통해 전체 아이템의 가격 및 을 측정한다.

#밸런스 계산 => 템 상황
#원하는보스까지 => 필요한 총 스탯 계산
#필요한 총 스탯을 맞추기 위해 => 얼마나 템을 바꿔야 하는지 계산


def doReadSpec():
    gf.screenshot(-3)
def doCalcSpec():
    total = dict() #능력치의 합을 담는 배열
    ability = dict() #모든 부위의 능력치를 담는 배열 key = orginal, poten, addipoten 의 value = dict() => key = strz, dexz, intz, lukz, strp ... 
    
    for idx, equip_kind in enumerate(['ahwk','djfwkd','snswkd','tkddml','gkdml','tlsqkf','qkswl1','qkswl2','qkswl3','qkswl4','vhzpt','ahrrjfdl1','ahrrjfdl2','anrl','qpfxm','rnlrjfdl','ruswkd','wkdrkq','dpaqmffpa','qotwl','cldgh','qhwh','akdxh','tlawkd']):
        stat_temp = {'totalvalue': dict(), 'total': dict(), 'basic': dict(), 'chuop': dict(), 'scroll': dict(), 'poten': list(), 'addipoten': list()} # 여기에 데이터 담아서 ability에 추가

        img_rgb = cv.imread('screenshot/' + equip_kind + '.png')
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

        #추옵, 작, 스타포스, 윗잠, 아랫잠
        star_cnt = fi.findImage(img_gray, img_rgb, "starforce") #스타포스 인식
        standard, standard_mid, standard_end = fi.findImage(img_gray, img_rgb, "standard") #옵션 위치 확인

        #이미지에서 find_list math 가져오기
        arr = gf.getItemDetail(img_gray,img_rgb) #추옵, 작, 윗잠, 아랫잠
        answer, poten, addipoten = gf.print_answer(arr, standard, standard_mid, standard_end)
        #answer.append(['스타포스',str(star_cnt),"","","","original"])

        #전체 아이템의 능력치의 합을 보고, 스탯별 가중치를 측정한다. (ex) str = 1, dex = 0.1, str% = 8, all% = 9 등 )

        """
            총 능력치 합 total[0]
            그 
            STR DEX INT LUK 공격력 마력 보공 방무 올스탯% STR% DEX% INT% LUK%
        """
        
        total_temp = dict()
        basic_temp = dict()
        chuop_temp = dict()
        scroll_temp = dict()
        poten_temp = list()
        addipoten_temp = list()
        totalvalue_temp = dict()
        print(answer,poten,addipoten)
        for i in answer:
            total_temp[i[0]] = i[1]
            basic_temp[i[0]] = i[2]
            chuop_temp[i[0]] = i[3]
            scroll_temp[i[0]] = i[4]
            if i[0] in {'STR','DEX','INT','LUK','공격력','마력','몬스터 방어율 무시','방어력','보스 몬스터 공격 시 데미지','업그레이드 가능 횟수','올스탯','점프력','최대 HP','최대 MP','1','2','3','4','5','6','7','8','9','0','(',')','+','%','%','데미지','가위 사용 가능 횟수','모든 스킬 재사용 대기시간2','모든 스킬 재사용 대기시간1','캐릭터 기준 10레벨 당10STR','캐릭터 기준 10레벨 당10DEX','캐릭터 기준 10레벨 당10INT','캐릭터 기준 10레벨 당10LUK','크리티컬 데미지'}:
                if len(i[1]) >= 1:
                    if i[0] == "모든 스킬 재사용 대기시간2":
                        if total.get("모든 스킬 재사용 대기시간") == None:
                            total["모든 스킬 재사용 대기시간"] = 2
                        else:                
                            total["모든 스킬 재사용 대기시간"] = total["모든 스킬 재사용 대기시간"] + 2
                    elif i[0] == "모든 스킬 재사용 대기시간1":
                        if total.get("모든 스킬 재사용 대기시간") == None:
                            total["모든 스킬 재사용 대기시간"] = 1
                        else:                
                            total["모든 스킬 재사용 대기시간"] = total["모든 스킬 재사용 대기시간"] + 1
                            
                    elif i[1][-1] == "%":
                        if total.get(i[0]+"p") == None:
                            total[i[0]+"p"] = (int)(i[1][0:-1])
                        else:                
                            total[i[0]+"p"] = total[i[0]+"p"] + (int)(i[1][0:-1])
                            
                    else:
                        if total.get(i[0]) == None:
                            total[i[0]] = (int)(i[1])
                        else:                
                            total[i[0]] = total[i[0]] + (int)(i[1])

        for i in poten:
            poten_temp.append(i[0])
            poten_temp.append(i[1])
            if i[0] in {'STR','DEX','INT','LUK','공격력','마력','몬스터 방어율 무시','방어력','보스 몬스터 공격 시 데미지','업그레이드 가능 횟수','올스탯','점프력','최대 HP','최대 MP','1','2','3','4','5','6','7','8','9','0','(',')','+','%','%','데미지','가위 사용 가능 횟수','모든 스킬 재사용 대기시간2','모든 스킬 재사용 대기시간1','캐릭터 기준 10레벨 당10STR','캐릭터 기준 10레벨 당10DEX','캐릭터 기준 10레벨 당10INT','캐릭터 기준 10레벨 당10LUK','크리티컬 데미지'}:
                if len(i[1]) >= 1:
                    if i[0] == "모든 스킬 재사용 대기시간2":
                        if total.get("모든 스킬 재사용 대기시간") == None:
                            total["모든 스킬 재사용 대기시간"] = 2
                        else:                
                            total["모든 스킬 재사용 대기시간"] = total["모든 스킬 재사용 대기시간"] + 2
                    elif i[0] == "모든 스킬 재사용 대기시간1":
                        if total.get("모든 스킬 재사용 대기시간") == None:
                            total["모든 스킬 재사용 대기시간"] = 1
                        else:                
                            total["모든 스킬 재사용 대기시간"] = total["모든 스킬 재사용 대기시간"] + 1
                            
                    elif i[1][-1] == "%":
                        if total.get(i[0]+"p") == None:
                            total[i[0]+"p"] = (int)(i[1][0:-1])
                        else:                
                            total[i[0]+"p"] = total[i[0]+"p"] + (int)(i[1][0:-1])
                            
                    else:
                        if total.get(i[0]) == None:
                            total[i[0]] = (int)(i[1])
                        else:                
                            total[i[0]] = total[i[0]] + (int)(i[1])
        for i in addipoten:
            addipoten_temp.append(i[0])
            addipoten_temp.append(i[1])
            if i[0] in {'STR','DEX','INT','LUK','공격력','마력','몬스터 방어율 무시','방어력','보스 몬스터 공격 시 데미지','업그레이드 가능 횟수','올스탯','점프력','최대 HP','최대 MP','1','2','3','4','5','6','7','8','9','0','(',')','+','%','%','데미지','가위 사용 가능 횟수','모든 스킬 재사용 대기시간2','모든 스킬 재사용 대기시간1','캐릭터 기준 10레벨 당10STR','캐릭터 기준 10레벨 당10DEX','캐릭터 기준 10레벨 당10INT','캐릭터 기준 10레벨 당10LUK','크리티컬 데미지'}:
                if len(i[1]) >= 1:
                    if i[0] == "모든 스킬 재사용 대기시간2":
                        if total.get("모든 스킬 재사용 대기시간") == None:
                            total["모든 스킬 재사용 대기시간"] = 2
                        else:                
                            total["모든 스킬 재사용 대기시간"] = total["모든 스킬 재사용 대기시간"] + 2
                    elif i[0] == "모든 스킬 재사용 대기시간1":
                        if total.get("모든 스킬 재사용 대기시간") == None:
                            total["모든 스킬 재사용 대기시간"] = 1
                        else:                
                            total["모든 스킬 재사용 대기시간"] = total["모든 스킬 재사용 대기시간"] + 1
                            
                    elif i[1][-1] == "%":
                        if total.get(i[0]+"p") == None:
                            total[i[0]+"p"] = (int)(i[1][0:-1])
                        else:                
                            total[i[0]+"p"] = total[i[0]+"p"] + (int)(i[1][0:-1])
                            
                    else:
                        if total.get(i[0]) == None:
                            total[i[0]] = (int)(i[1])
                        else:                
                            total[i[0]] = total[i[0]] + (int)(i[1])

        
        stat_temp['total'] = total_temp
        stat_temp['basic'] = basic_temp
        stat_temp['chuop'] = chuop_temp
        stat_temp['scroll'] = scroll_temp
        stat_temp['poten'] = poten_temp
        stat_temp['addipoten'] = addipoten_temp

        ability[equip_kind] = stat_temp
        
        #print(equip_kind)
        #print(standard,standard_mid,standard_end)
    print("total")
    print(total)
    return total, ability #능력치의 합을 담는 배열 / 모든 부위의 능력치를 담는 배열 key = orginal, poten, addipoten 의 value = dict() => key = strz, dexz, intz, lukz, strp ... 
    """
    for key, value in ability.items():
        print("[" + key + "]" )
        print(value['total'])
        print(value['basic'])
        print(value['chuop'])
        print(value['scroll'])
        print(value['poten'])
        print(value['addipoten'])
    """