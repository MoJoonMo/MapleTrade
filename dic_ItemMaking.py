
from scipy.stats import binom

def dicItemMaking():
    dic = { #필요 주흔 개수, 업횟이 나옴 
            '골든클로버벨트' : [140,240,3]
            ,'b' : 2
            
          }

    return dic

def juhn(upg,probability,juhn): #upg = 업그레이드 가능 횟수, probability = 주문서 확률
    #순백 : 20000 / 이노센트 : 10000
    """
    binom.pmf(k=1, n=8, p=0.59)
    업횟이 n 이라고 했을때,
    최초 발리는게 0 ~ n 까지 가능함.

    이노를 해서 0 이상 되었을 때 멈춰서, 순백을 했을 때의 기댓값
    이노를 해서 1 이상 되었을 때 멈춰서, 순백을 했을 때의 기댓값
    이노를 해서 2 이상 되었을 때 멈춰서, 순백을 했을 때의 기댓값
    ...
    이노를 해서 n-1 이상 되었을 때 멈춰서, 순백을 했을 때의 기댓값
    이노를 해서 n 이상 되었을 때 멈춰서, 순백을 했을 때의 기댓값

    들을 비교해서 제일 적은게 맞다.

    이노를 해서 1 이상 되었을 때 멈춰서, 순백을 했을 때의 기댓값 은 어떻게 구하느냐?
    

    이노를 해서 1 이상 될 확률 을 구한다. ===> 1 - binom.pmf(k=0, n=8, p=0.59)
    1 / 위에서 구한 확률 => 이노센트 쓰는 가격
    나머지 확률을 확률로 분배해서 살려야할 업횟 평균 값을 구한다.  => 살려야할 업횟 평균 값 x 업횟 1회 살리는 가격 
    주흔 사용 개수 = 이노센트 쓰는 가격 + 살려야할 업횟 평균 값 x 업횟 1회 살리는 가격  
    
    """
    bid = [1]
    inno = 0
    purewhite = 0
    answer = []
    ret = 9999999999
    for idx in range(0,upg,1):
        bid.append(bid[idx]-binom.pmf(k=idx,n=upg,p=probability)) # bid[idx]는 이항분포 0이 빠진 값
    for idx in range(0,upg+1,1):
        inno = (1 / bid[idx] - 1) * 10000
        purewhite = (upg-idx) * (20000+juhn) / probability
        answer.append(inno+purewhite)
    for idx in answer:
        if ret >= idx:
            ret = idx
    print(ret)
    return ret

    

    dic = 0



def starforceProbability(oneplusone,fivetenfifteen,preventDestory,starcatch):
    success = [1,0.95,0.90,0.85,0.85,0.80,0.75,0.70,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.03,0.02,0.01]
    fail_remain = [0.0]
    fail_down =[0.0]
    destroy = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

    if starcatch == "Y":
        for idx, s in enumerate(success):
            success[idx] = round(s * 1.05,6)
    if oneplusone == "Y":
        for idx in [2,4,6,8,10,12]:
            success[idx] = 1.0
    if fivetenfifteen == "Y":
        for idx in [6,11,16]:
            success[idx] = 1.0
    if preventDestory == "N":
        destroy[13] = round(0.01*(1.0-success[13]),6)
        destroy[14] = round(0.02*(1.0-success[14]),6)
        destroy[15] = round(0.02*(1.0-success[15]),6)
        destroy[16] = round(0.03*(1.0-success[16]),6)
        destroy[17] = round(0.03*(1.0-success[17]),6)
    destroy[18] = round(0.03*(1.0-success[18]),6)
    destroy[19] = round(0.04*(1.0-success[19]),6)
    destroy[20] = round(0.04*(1.0-success[20]),6)
    destroy[21] = round(0.1*(1.0-success[21]),6)
    destroy[22] = round(0.1*(1.0-success[22]),6)
    destroy[23] = round(0.2*(1.0-success[23]),6)
    destroy[24] = round(0.3*(1.0-success[24]),6)
    destroy[25] = round(0.4*(1.0-success[25]),6)

    for idx in range(1,26,1):
        if  (idx >= 1 and idx <= 11) or (idx == 16) or (idx == 21):
            fail_remain.append( round(1-success[idx]-destroy[idx],6) )
            fail_down.append(0.0)
        else:
            fail_remain.append(0.0)
            fail_down.append( round(1-success[idx]-destroy[idx],6) )
    #print(fail_down)

    
    return success, fail_remain, fail_down, destroy
def getPrice(level, oneplusone, fivetenfifteen, preventDestroy, Discount1, Discount2):
    #Discount1 L: 30%할인, Discount2 : 10%할인
    price=[0]
    price_noprevent =[0]
    for idx in range(1,26,1):
        if oneplusone == "Y" and (idx == 2 or idx == 4 or idx == 6 or idx == 8 or idx == 10 or idx == 12): # 1+1
            price.append(0)
            price_noprevent.append(0)
        elif idx >= 13 and idx <= 15 and preventDestroy == "Y": # 파방 13~15
            price.append(round(1000+pow(idx,2.7)/400*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2) + 1) )
            price_noprevent.append( round(1000+pow(idx,2.7)/400*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2)) )
        elif idx == 16 and fivetenfifteen == "Y": # 파방이지만 5/10/15 이벤일경우
            price.append(round(1000+pow(idx,2.7)/200*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2)) )
            price_noprevent.append( round(1000+pow(idx,2.7)/200*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2)) )
        elif idx >= 16 and idx <= 17 and preventDestroy == "Y": # 파방 16~18
            price.append(round(1000+pow(idx,2.7)/200*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2) + 1) )
            price_noprevent.append( round(1000+pow(idx,2.7)/200*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2) ) )
        elif idx >= 11 and idx <= 15:
            price.append(round(1000+pow(idx,2.7)/400*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2)) )
            price_noprevent.append( round(1000+pow(idx,2.7)/400*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2)) )
        elif idx <= 10:
            price.append(round(1000+pow(level,3)*idx/25,-2) * ( (1-Discount1) * (1-Discount2)) )
            price_noprevent.append( round(1000+pow(level,3)*idx/25,-2) * ( (1-Discount1) * (1-Discount2)) )
        elif idx >= 16 and idx <= 17:
            price.append(round(1000+pow(idx,2.7)/200*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2)) )
            price_noprevent.append( round(1000+pow(idx,2.7)/200*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2)) )
        elif idx >= 18:
            price.append(round(1000+pow(idx,2.7)/200*pow(level,3),-2) * ( (1-Discount1)) )
            price_noprevent.append( round(1000+pow(idx,2.7)/200*pow(level,3),-2) * ( (1-Discount1) ) )
        else:
            price.append(round(1000+idx^2.7/400*level*3,-2) * (1-Discount1) * (1-Discount2) ) 
            price_noprevent.append( round(1000+idx^2.7/400*level*3,-2) * (1-Discount1) * (1-Discount2) ) 
        price[idx] = round(price[idx],6)
        price_noprevent[idx] = round(price_noprevent[idx],6)
    
    return price, price_noprevent

def getStarforcePrice(level,itemPrice,oneplusone, fivetenfifteen,preventDestroy,starcatch,Discount1,Discount2):
    success, fail_remain, fail_down, destroy = starforceProbability(oneplusone,fivetenfifteen,preventDestroy,starcatch)
    price, price_noprevent = getPrice(level,oneplusone,fivetenfifteen,preventDestroy,Discount1,Discount2) # 30% 할인 / 10% 할인
                   
    twelve_price = round(1000+pow(12,2.7)/400*pow(level,3),-2) * ( (1-Discount1) * (1-Discount2))
    expectedValue = [0]
    totalValue = [0]

    for idx in range(1,13):
        if idx == 1:
            ev_temp = (price[idx] + fail_down[idx] * price[idx-1] + fail_down[idx] * fail_remain[idx-1] * expectedValue[idx-1] + fail_down[idx] * fail_down[idx-1] * (price_noprevent[idx-1] + expectedValue[idx-1]) ) / success[idx] 
        else:
            ev_temp = (price[idx] + fail_down[idx] * price[idx-1] + fail_down[idx] * fail_remain[idx-1] * expectedValue[idx-1] + fail_down[idx] * fail_down[idx-1] * (price_noprevent[idx-2] + expectedValue[idx-1]) ) / success[idx] 
        totalValue.append(round(totalValue[idx-1] + ev_temp, 0))
        expectedValue.append(round(ev_temp,0))
    #print(expectedValue)

    for idx in range(13,26):
        #print(idx, price[idx],fail_down[idx],price[idx-1],fail_remain[idx-1],fail_down[idx-1])
        if idx == 13 and oneplusone == "Y":
            temp = 0.55
            if starcatch == "Y":
                temp = 0.5275 #11 > 12성 실패 확률 1+1 에서 10>12바로가지만 11로 떨어졌을땐 바로가지 않아서 따로 넣음
            ev_temp = (price[idx] + fail_down[idx] * twelve_price + fail_down[idx] * 0 * expectedValue[idx-1] + fail_down[idx] * temp * (price_noprevent[idx-2] + expectedValue[idx-1]) + ( destroy[idx] + fail_down[idx] * 0 ) * ( itemPrice - totalValue[12] + totalValue[idx-1] ) ) / success[idx] 
        elif idx == 14:
            ev_temp = (price[idx] + fail_down[idx] * price[idx-1] + fail_down[idx] * fail_remain[idx-1] * expectedValue[idx-1] + fail_down[idx] * fail_down[idx-1] * (twelve_price           + expectedValue[idx-1]) + ( destroy[idx] + fail_down[idx] * destroy[idx-1] ) * ( itemPrice - totalValue[12] + totalValue[idx-1] ) ) / success[idx] 
        else:
            ev_temp = (price[idx] + fail_down[idx] * price[idx-1] + fail_down[idx] * fail_remain[idx-1] * expectedValue[idx-1] + fail_down[idx] * fail_down[idx-1] * (price_noprevent[idx-2] + expectedValue[idx-1]) + ( destroy[idx] + fail_down[idx] * destroy[idx-1] ) * ( itemPrice - totalValue[12] + totalValue[idx-1] ) ) / success[idx] 
        totalValue.append(round(totalValue[idx-1] + ev_temp, 0))
        expectedValue.append(round(ev_temp,0))

    for idx, ev in enumerate(expectedValue):
        print(idx, ev, totalValue[idx])

#샤타포스 + 스타캐치 + MVP
level, itemPrice, oneplusone, fivetenfifteen, preventDestroy, starcatch, Discount1, Discount2 = 160, 0, "N", "Y", "N", "Y", 0.3, 0.1
getStarforcePrice(level,itemPrice,oneplusone,fivetenfifteen,preventDestroy,starcatch, Discount1, Discount2)
juhn(4,0.59,240)

"""
name=골든클로버벨트, star=17, 
"""

#for idx in range(0,25,1):
#    print(idx, success[idx],fail_remain[idx],fail_down[idx],destroy[idx], price[idx], price_noprevent[idx])