#하이퍼 스탯 스펙
"""
Input : Level    ==>  Calc : 하이퍼스탯 (getHyperStatSpec.py)
"""

def getHyperStatSpec(level):
    
    if level >= 285:
        main_stat, sub_stat, cridmg, igd, dmg, btt, att = 120, 90, 13, 33, 39, 51, 21
    elif level >= 280:
        main_stat, sub_stat, cridmg, igd, dmg, btt, att = 90,60,13,30,39,51,18
    elif level >= 275:
        main_stat, sub_stat, cridmg, igd, dmg, btt, att = 150,120,12,33,36,51,18
    elif level >= 270:
        main_stat, sub_stat, cridmg, igd, dmg, btt, att = 120,60,12,30,36,51,18
    elif level >= 265:
        main_stat, sub_stat, cridmg, igd, dmg, btt, att = 150,90,3,11,33,36,47,21
    elif level >= 260:
        main_stat, sub_stat, cridmg, igd, dmg, btt, att = 180,60,3,11,33,33,47,18
    elif level >= 255:
        main_stat, sub_stat, cridmg, igd, dmg, btt, att = 150,90,11,33,33,43,21
    else:
        main_stat, sub_stat, cridmg, igd, dmg, btt, att = 120,60,10,33,30,35,9
    
    return main_stat, sub_stat, cridmg, igd, dmg, btt, att

    # 로직 짜는건 나중에 중요하지 않음
    """
    index = [3,34,75,126,187,258,339,430,531,642,763,894,1035,1186,1347,1518]
    ts = 0 #total stat
    if level > 300:
        ts = 1698
    elif level >= 140:
        ts = index[(int)(level/10)-14] + ((int)(level/10)-11) * (level % 10)
    else:
        ts = 0

    expectedStatByLevel = [0,1,2,4,8,10,15,20,25,30,35,50,65,80,95,110]

    for idx, stat in enumerate(expectedStatByLevel):
        if ts / 4 < stat: # 하이퍼스탯 4개를 전부 idx 만큼 찍을 수 없다면,


        else:
            continue
    


    return ts
    """

#print(getHyperStatSpec(280))

    
    