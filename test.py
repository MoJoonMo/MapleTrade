"""
input : 아이템 이름
이름에 따라 필요 주흔 개수, 업횟이 나옴 

output : 15%,30% 완작 기대값

"""
import dic_ItemMaking as di 
import numpy as np
def itemValueByMaking(name):
    dic = di.dicItemMaking()
    #print(dic[name])
    #레벨


    return dic[name]



itemValueByMaking("골든클로버벨트")

    