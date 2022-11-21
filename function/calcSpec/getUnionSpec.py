#Union Level과 직업을 입력하면, 그에 맞는 Union 스펙을 반환한다

"""
Union Level 6000 / 6500 / 7000 / 7500

직업 늘어나면 벞지 들어갈 수 있음.

"""

def getUnionSpec(level,job):
    if level >= 6000 and level < 6500:
        return 25,5,5,4,40,20 #main_stat, sub_stat, att, boss_dmg, igd, cridmg
    elif level >= 6500 and level < 7000:
        return 25,5,5,9,40,20
    elif level >= 7000 and level < 7500:
        return 25,5,5,13,40,20
    elif level >= 7500 and level < 8000:
        return 25,5,5,17,40,20
    elif level >= 8000 and level < 8500:
        return 25,5,5,40,40,20
    elif level >= 8500 and level < 9000:
        return 50,5,5,40,40,20
    elif level >= 9000 and level < 9500:
        return 75,5,5,40,40,20
    elif level >= 5500 and level < 6000:
        return 25,5,5,20,30,15
    elif level >= 5000 and level < 5500:
        return 40,5,5,21,21,10.5
    elif level >= 4500 and level < 5000:
        return 25,5,5,21,21,10.5
    elif level >= 4000 and level < 4500:
        return 25,5,5,18,21,10.5
    elif level >= 3500 and level < 4000:
        return 60,5,5,13,13,6.5
    else:
        return 25,5,0,0,0,5
