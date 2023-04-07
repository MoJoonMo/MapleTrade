# -*- coding: utf-8 -*-
from function.calcSpec import getHyperStatSpec as ghs
from function.calcSpec import getLinkSpec as gls
from function.calcSpec import getUnionSpec as gus
from function.calcSpec import getPassiveSkillSpec as gpss
from function.calcSpec import getMonsterFarmSpec as gmfs
from function.calcSpec import getCharacteristicSpec as gcs
import math as math
def itemDiagnosis(level, job, union_level, farm_level, total, ability):
    #level = 280
    #job = "adele"
    setting_kind = "boss"
    arcane_stat = 13200
    authentice_stat = 6100

    union_pure_str = 620
    union_pure_dex = 400
    union_pure_int = 0
    union_pure_luk = 0
    maple_yongsa = (int)((level*5+18)*0.16) # 쓸오더
    item_str, item_dex, item_int, item_luk = 0,0,0,0

    item_att, item_mtt = 0,0
    item_attp, item_mttp = 0,0
    item_cridmg = 0
    item_dmg, item_btt, item_igd = 0,0,0
    item_strp, item_dexp, item_intp, item_lukp, item_allp = 0,0,0,0,0

    plevel = (int)(level / 10)
    item_lvl_str, item_lvl_dex, item_lvl_int, item_lvl_luk = 0,0,0,0
    f_weapon_constant = 1.3

    #item set효과 봐야함

    #루타 : 힘덱 20 / 보장 : 올 10 / 아케인 : 올 50 / 레헬른 : 15
    item_set_str, item_set_dex,item_set_int,item_set_luk, item_set_att, item_set_btt = 20 + 10 + 50 + 15, 20 + 10 + 50 + 15, 0, 0, 190, 60

    cooldown = 3
    #Null Check
    if "STR" in total:
        item_str = total["STR"]
    if "DEX" in total:
        item_dex = total["DEX"]
    if "INT" in total:
        item_int = total["INT"]
    if "LUK" in total:
        item_luk = total["LUK"]
    if "공격력" in total:
        item_att = total["공격력"]
    if "마력" in total:
        item_mtt = total["마력"]
    if "공격력p" in total:
        item_attp = total["공격력p"]
    if "마력p" in total:
        item_mttp = total["마력p"]
    if "크리티컬 데미지p" in total:
        item_cridmg = total["크리티컬 데미지p"]
    if "데미지p" in total:
        item_dmg = total["데미지p"]
    if "보스 몬스터 공격 시 데미지p" in total:
        item_btt = total["보스 몬스터 공격 시 데미지p"]
    if "몬스터 방어율 무시p" in total:
        item_igd = total["몬스터 방어율 무시p"]
    if "STRp" in total:
        item_strp = total["STRp"]
    if "DEXp" in total:
        item_dexp = total["DEXp"]
    if "INTp" in total:
        item_intp = total["INTp"]
    if "LUKp" in total:
        item_lukp = total["LUKp"]
    if "올스탯p" in total:
        item_allp = total["올스탯p"]
    if "캐릭터 기준 10레벨 당10STR" in total:
        item_lvl_str = total["캐릭터 기준 10레벨 당10STR"] * plevel
    if "캐릭터 기준 10레벨 당10DEX" in total:
        item_lvl_dex = total["캐릭터 기준 10레벨 당10DEX"] * plevel
    if "캐릭터 기준 10레벨 당10INT" in total:
        item_lvl_int = total["캐릭터 기준 10레벨 당10INT"] * plevel
    if "캐릭터 기준 10레벨 당10LUK" in total:
        item_lvl_luk = total["캐릭터 기준 10레벨 당10LUK"] * plevel
    if job == "adele":
        f_weapon_constant = 1.3 


    #print(ghs.getHyperStatSpec(level=level))
    hyperstat_main_stat, hyperstat_sub_stat, hyperstat_cridmg, hyperstat_igd, hyperstat_dmg, hyperstat_btt, hyperstat_att = ghs.getHyperStatSpec(level=level)
    print(gls.getLinkSpec(job=job, kind=setting_kind))
    link_btt, link_dmg, link_igd, link_cridmg, link_all, link_att, link_mtt = gls.getLinkSpec(job=job, kind=setting_kind)
    #print(gus.getUnionSpec(level=union_level, job=job))

    level_str_stat, level_dex_stat, level_int_stat, level_luk_stat = 4, 4, 4, 4
    hyperstat_str,hyperstat_des,hyperstat_int,hyperstat_luk = 0, 0, 0, 0

    #유니온
    union_main_stat, union_sub_stat, union_att, union_btt, union_igd, union_cridmg = gus.getUnionSpec(level=union_level, job=job)
    union_str_stat, union_dex_stat, union_int_stat, union_luk_stat,union_mtt_stat = 0,0,0,0,0
    if job == "adele":
        union_str_stat, union_dex_stat = union_main_stat, union_sub_stat
        hyperstat_str, hyperstat_dex = hyperstat_main_stat, hyperstat_sub_stat 
        level_str_stat= level * 5 + 18
        
        

    #print(gpss.getPassiveSkillSpec(job=job, level=level))
    passive_str, passive_dex, passive_int, passive_luk, passive_att, passive_mtt, passive_attp, passive_mttp, passive_btt, passive_final_dmg, passive_igd, passive_cridmg, passive_dmg= gpss.getPassiveSkillSpec(job=job, level=level)
    mf_strz, mf_strp, mf_pure_str, mf_dexz, mf_dexp, mf_pure_dex, mf_intz, mf_intp, mf_pure_int, mf_lukz, mf_lukp, mf_pure_luk, mf_att, mf_mtt, mf_dmg, mf_btt, mf_finaldmg, mf_igd, mf_cridmg = gmfs.getMonsterFarmSpec(job=job) 
    #print(gmfs.getMonsterFarmSpec(job=job))
    c_igd, c_buff = gcs.getCharacteristicSpec()
    #print(gcs.getCharacteristicSpec())
    #print(level_str_stat,item_str, item_set_str, union_str_stat, mf_strz, passive_str, item_lvl_str )
    #print(item_strp + item_allp + mf_strp + maple_yongsa)
    #print(arcane_stat + authentice_stat + hyperstat_str + union_pure_str)


    f_str = ( level_str_stat + item_str + union_str_stat + mf_strz + item_set_str + passive_str + item_lvl_str + maple_yongsa + 40) * (item_strp + item_allp + mf_strp + 100 ) / 100 + arcane_stat + authentice_stat + hyperstat_str + union_pure_str  # 40은 길드
    f_dex = ( level_dex_stat + item_dex + union_dex_stat + mf_dexz + item_set_dex + passive_dex + item_lvl_dex + maple_yongsa + 40) * (item_dexp + item_allp + mf_dexp + 100 ) / 100 + hyperstat_dex + union_pure_dex 
    f_int = ( level_int_stat + item_int + union_int_stat + mf_intz + item_set_int + passive_int + item_lvl_int + maple_yongsa + 40) * (item_intp + item_allp + mf_intp + 100 ) / 100 + hyperstat_int + union_pure_int
    f_luk = ( level_luk_stat + item_luk + union_luk_stat + mf_lukz + item_set_luk + passive_luk + item_lvl_luk + maple_yongsa + 40) * (item_lukp + item_allp + mf_lukp + 100 ) / 100 + hyperstat_luk + union_pure_luk
    #도핑에 성향 없음
    f_att = (item_att + union_att + passive_att + hyperstat_att + link_att + mf_att + item_set_att + 20 + 51 + 98 + 15) * (1 + (item_attp +passive_attp) * 0.01) + 14 #20은 모바일 유니온 / 51은 매직서킷 / 14는 농장 이퀄 / 98은 펫장비 / 15는 길드
    
    f_dmg = item_dmg + hyperstat_dmg + passive_dmg + link_dmg   
    f_final_dmg = 149.5 * 131/130 * 1.1
    f_btt = item_btt + hyperstat_btt + passive_btt + link_btt + union_btt + mf_btt + item_set_btt + 10 + 7 + 9 #핑아일체, 소울, 어빌

    
    print(item_btt)
    print(f_btt)

    print("스공 : " + ((str) (math.floor( (f_str * 4 + f_dex) * 0.01 * ((int)(f_att)) * f_weapon_constant * (1+f_dmg/100) * (f_final_dmg/100)))) )
    print("공격력 스공 : " + ((str) (math.floor( (65445 * 4 + 7179) * 0.01 * ((int)(f_att)) * f_weapon_constant * (1+f_dmg/100) * (f_final_dmg/100)))) )    
    print(f_str)
    print(f_dex)
    print(f_att)
    

    #print(f_str, f_dex)
    #

    """
    Input : Level    ==>  Calc : 하이퍼스탯 (getHyperStatSpec.py)
    Input : Union Level, Job ==> Calc : 유니온 점령효과 (getUnionSpec.py)
    Input : X => Calc : 링크 효과 (getLinkSpec.py)
    Input : Job, Level ==> Calc : 패시브스킬(0,1,2,3,4,5차) (getPassiveSkillSpec.py)
    Input : Farm Level ==> Calc : 농장 보유효과 (getMonsterFarmSpec.py)

    Input : Doping ==> Calc : 도핑 종류에 따른 증가치
    Input : X => Calc : 성향 만렙 (getCharacteristicSpec.py)
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
total = {'STR': 3931, 'DEX': 2738, 'LUK': 1481, '최대 HP': 15055, '최대 MP': 6915, '공격력': 2567, '마력': 1380, '방어력': 10478, '몬스터 방어율 무시p': 95, '올스탯p': 115, '업그레이드 가능 횟수': 0, '가위 사용 가능 횟수': 56, '모든 스킬 재사용 대기시간': 3, 'STRp': 509, '3': 0, '점프력': 78, 'INTp': 17, 'INT': 1452, '캐릭터 기준 10레벨 당10STR': 9, '최대 HPp': 29, '최대 MPp': 22, '보스 몬스터 공격 시 데미지p': 168, '데미지p': 5, '공격력p': 105, '크리티컬 데미지p': 19, 'DEXp': 4}

ability = {'ahwk': {'totalvalue': {}, 'total': {'STR': '309', 'DEX': '157', 'LUK': '20', '최대 HP': '2055', '최대 MP': '360', '공격력': '94', '마력': '85', '방어력': '1511', '몬스터 방어율 무시': '10%', '올스탯': '6%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': '9'}, 'basic': {'STR': '40', 'DEX': '40', 'LUK': '0', '최대 HP': '360', '최대 MP': '', '공격력': '2', '마력': '0', '방어력': '390', '몬스터 방어율 무시': '', '올스탯': '0%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': ''}, 'chuop': {'STR': '68', 'DEX': '', 'LUK': '20', '최대 HP': '', '최대 MP': '', '공격력': '6', '마력': '', '방어력': '', '몬스터 방어율 무시': '', '올스탯': '6%', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'scroll': {'STR': '201', 'DEX': '117', 'LUK': '', '최대 HP': '1695', '최대 MP': '', '공격력': '86', '마력': '85', '방어력': '1121', '몬스터 방어율 무시': '', '올스탯': '', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'poten': ['모든 스킬 재사용 대기시간2', '10', '10%5', '', 'STR', '12%', 'STR', '9%'], 'addipoten': ['모든 스킬 재사용 대기시간1', '10', '5%5', '', '최대 HP', '240', 'STR', '5%', '1', '']}, 'djfwkd': {'totalvalue': {}, 'total': {'STR': '81', 'DEX': '82', '공격력': '57', '마력': '45', '방어력': '101', '3': '0', '점프력': '8', '올스탯': '3%', '업그레이드 가능 횟수': '0'}, 'basic': {'STR': '3', 'DEX': '3', '공격력': '3', '마력': '0', '방어력': '26', '3': '2', '점프력': '0', '올스탯': '0%', '업그레이드 가능 횟수': '0'}, 'chuop': {'STR': '', 'DEX': '', '공격력': '', '마력': '', '방어력': '', '3': '', '점프력': '3', '올스탯': '3%', '업그레이드 가능 횟수': ''}, 'scroll': {'STR': '78', 'DEX': '79', '공격력': '54', '마력': '45', '방어력': '75', '3': '1', '점프력': '5', '올스탯': '', '업그레이드 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['STR', '5%', 'INT', '4%', 'STR', '4%', '1', '']}, 'snswkd': {'totalvalue': {}, 'total': {'STR': '141', 'DEX': '101', 'INT': '91', 'LUK': '89', '공격력': '70', '마력': '58', '방어력': '374', '점프력': '18', '올스탯': '6%', '업그레이드 가능 횟수': '0'}, 'basic': {'STR': '7', 'DEX': '7', 'INT': '7', 'LUK': '7', '공격력': '1', '마력': '1', '방어력': '120', '점프력': '0', '올스탯': '0%', '업그레이드 가능 횟수': '0'}, 'chuop': {'STR': '44', 'DEX': '16', 'INT': '', 'LUK': '', '공격력': '', '마력': '', '방어력': '', '점프력': '6', '올스탯': '6%', '업그레이드 가능 횟수': ''}, 'scroll': {'STR': '90', 'DEX': '78', 'INT': '84', 'LUK': '82', '공격력': '69', '마력': '57', '방어력': '254', '점프력': '12', '올스탯': '', '업그레이드 가능 횟수': ''}, 'poten': ['올스탯', '9%', '올스탯', '6%', '올스탯', '6%'], 'addipoten': ['올스탯', '2%', '공격력', '10', 'INT', '10']}, 'tkddml': {'totalvalue': {}, 'total': {'STR': '291', 'DEX': '167', 'LUK': '20', '최대 HP': '1215', '공격력': '88', '마력': '85', '방어력': '867', '몬스터 방어율 무시': '5%', '올스탯': '5%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': '6'}, 'basic': {'STR': '30', 'DEX': '30', 'LUK': '0', '최대 HP': '0', '공격력': '2', '마력': '0', '방어력': '210', '몬스터 방어율 무시': '', '올스탯': '0%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': ''}, 'chuop': {'STR': '88', 'DEX': '20', 'LUK': '20', '최대 HP': '', '공격력': '', '마력': '', '방어력': '', '몬스터 방어율 무시': '', '올스탯': '5%', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'scroll': {'STR': '173', 'DEX': '117', 'LUK': '', '최대 HP': '1215', '공격력': '86', '마력': '85', '방어력': '657', '몬스터 방어율 무시': '', '올스탯': '', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['STR', '5%', 'STR', '4%', '8', '', '1', '']}, 'gkdml': {'totalvalue': {}, 'total': {'STR': '275', 'DEX': '171', '최대 HP': '1215', '공격력': '92', '마력': '85', '방어력': '867', '몬스터 방어율 무시': '5%', '올스탯': '6%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': '3'}, 'basic': {'STR': '30', 'DEX': '30', '최대 HP': '0', '공격력': '2', '마력': '0', '방어력': '210', '몬스터 방어율 무시': '', '올스탯': '0%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': ''}, 'chuop': {'STR': '72', 'DEX': '24', '최대 HP': '', '공격력': '4', '마력': '', '방어력': '', '몬스터 방어율 무시': '', '올스탯': '6%', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'scroll': {'STR': '173', 'DEX': '117', '최대 HP': '1215', '공격력': '86', '마력': '85', '방어력': '657', '몬스터 방어율 무시': '', '올스탯': '', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '12%', 'STR', '9%'], 'addipoten': ['공격력', '12', 'INT', '14', 'STR', '4%', '1', '']}, 'tlsqkf': {'totalvalue': {}, 'total': {'STR': '362', 'DEX': '221', 'LUK': '30', '최대 HP': '960', '공격력': '116', '마력': '106', '방어력': '986', '28': '10', '점프력': '25', '올스탯': '5%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': '8'}, 'basic': {'STR': '40', 'DEX': '40', 'LUK': '0', '최대 HP': '0', '공격력': '9', '마력': '0', '방어력': '250', '28': '18', '점프력': '7', '올스탯': '0%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': ''}, 'chuop': {'STR': '121', 'DEX': '36', 'LUK': '30', '최대 HP': '', '공격력': '', '마력': '', '방어력': '', '28': '', '점프력': '', '올스탯': '5%', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'scroll': {'STR': '201', 'DEX': '145', 'LUK': '', '최대 HP': '960', '공격력': '107', '마력': '106', '방어력': '736', '28': '', '점프력': '18', '올스탯': '', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', '올스탯', '6%'], 'addipoten': ['캐릭터 기준 10레벨 당10STR', '2', 'STR', '5%', 'STR', '16', '1', '']}, 'qkswl1': {'totalvalue': {}, 'total': {'STR': '137', 'DEX': '142', 'INT': '141', 'LUK': '143', '최대 HP': '475', '최대 MP': '230', '공격력': '112', '마력': '100', '방어력': '26', '업그레이드 가능 횟수': '0'}, 'basic': {'STR': '5', 'DEX': '5', 'INT': '5', 'LUK': '5', '최대 HP': '200', '최대 MP': '200', '공격력': '2', '마력': '2', '방어력': '0', '업그레이드 가능 횟수': '0'}, 'chuop': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '', '마력': '', '방어력': '', '업그레이드 가능 횟수': ''}, 'scroll': {'STR': '132', 'DEX': '137', 'INT': '136', 'LUK': '138', '최대 HP': '275', '최대 MP': '30', '공격력': '110', '마력': '98', '방어력': '26', '업그레이드 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['STR', '5%', '공격력', '11', '8', '']}, 'qkswl2': {'totalvalue': {}, 'total': {'STR': '113', 'DEX': '110', 'INT': '110', 'LUK': '108', '최대 HP': '475', '최대 MP': '230', '공격력': '91', '마력': '82', '방어력': '491', '업그레이드 가능 횟수': '0'}, 'basic': {'STR': '5', 'DEX': '5', 'INT': '5', 'LUK': '5', '최대 HP': '200', '최대 MP': '200', '공격력': '1', '마력': '1', '방어력': '150', '업그레이드 가능 횟수': '0'}, 'chuop': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '', '마력': '', '방어력': '', '업그레이드 가능 횟수': ''}, 'scroll': {'STR': '108', 'DEX': '105', 'INT': '105', 'LUK': '103', '최대 HP': '275', '최대 MP': '30', '공격력': '90', '마력': '81', '방어력': '341', '업그레이드 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['캐릭터 기준 10레벨 당10STR', '2', 'STR', '5%', '캐릭터 기준 10레벨 당10STR', '1', '1', '']}, 'qkswl3': {'totalvalue': {}, 'total': {'STR': '40', 'DEX': '40', 'INT': '40', 'LUK': '40', '최대 HP': '4000', '최대 MP': '4000', '공격력': '25', '마력': '25', '업그레이드 가능 횟수': '0'}, 'basic': {'STR': '10', 'DEX': '10', 'INT': '10', 'LUK': '10', '최대 HP': '1000', '최대 MP': '1000', '공격력': '10', '마력': '10', '업그레이드 가능 횟수': '0'}, 'chuop': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '', '마력': '', '업그레이드 가능 횟수': ''}, 'scroll': {'STR': '30', 'DEX': '30', 'INT': '30', 'LUK': '30', '최대 HP': '3000', '최대 MP': '3000', '공격력': '15', '마력': '15', '업그레이드 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['STR', '7%', '공격력', '12', '최대 HP', '240']}, 'qkswl4': {'totalvalue': {}, 'total': {'STR': '4', 'DEX': '4', 'INT': '4', 'LUK': '4', '공격력': '4', '마력': '4'}, 'basic': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': ''}, 'chuop': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': ''}, 'scroll': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': ''}, 'poten': [], 'addipoten': ['공격력마력', '', '4', '', '데미지', '']}, 'vhzpt': {'totalvalue': {}, 'total': {'STR': '90', 'DEX': '35', 'INT': '10', 'LUK': '10', '최대 HP': '100', '최대 MP': '100', '공격력': '15', '마력': '10', '올스탯': '5%'}, 'basic': {'STR': '20', 'DEX': '10', 'INT': '', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '10', '마력': '', '올스탯': '0%'}, 'chuop': {'STR': '70', 'DEX': '25', 'INT': '', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '5', '마력': '', '올스탯': '5%'}, 'scroll': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '', '마력': '', '올스탯': ''}, 'poten': [], 'addipoten': []}, 'ahrrjfdl1': {'totalvalue': {}, 'total': {'STR': '229', 'DEX': '161', 'INT': '161', 'LUK': '141', '최대 HP': '10%', '최대 MP': '10%', '공격력': '99', '마력': '99', '방어력': '748', '18': '0', '점프력': '12', '올스탯': '6%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': '5'}, 'basic': {'STR': '20', 'DEX': '20', 'INT': '20', 'LUK': '20', '최대 HP': '', '최대 MP': '', '공격력': '3', '마력': '3', '방어력': '100', '18': '18', '점프력': '0', '올스탯': '0%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': ''}, 'chuop': {'STR': '88', 'DEX': '20', 'INT': '20', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '', '마력': '', '방어력': '', '18': '', '점프력': '', '올스탯': '6%', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'scroll': {'STR': '121', 'DEX': '121', 'INT': '121', 'LUK': '121', '최대 HP': '', '최대 MP': '', '공격력': '96', '마력': '96', '방어력': '648', '18': '', '점프력': '12', '올스탯': '', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '12%'], 'addipoten': ['STR', '7%', '캐릭터 기준 10레벨 당10STR', '1', '공격력', '12', '1', '', '202310312155', '']}, 'ahrrjfdl2': {'totalvalue': {}, 'total': {'STR': '132', 'DEX': '75', 'INT': '85', 'LUK': '75', '최대 HP': '545', '최대 MP': '230', '공격력': '62', '마력': '45', '방어력': '527', '점프력': '6', '올스탯': '4%', '업그레이드 가능 횟수': '0'}, 'basic': {'STR': '16', 'DEX': '0', 'INT': '0', 'LUK': '0', '최대 HP': '180', '최대 MP': '180', '공격력': '0', '마력': '0', '방어력': '185', '점프력': '0', '올스탯': '0%', '업그레이드 가능 횟수': '0'}, 'chuop': {'STR': '36', 'DEX': '', 'INT': '8', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '', '마력': '', '방어력': '', '점프력': '3', '올스탯': '4%', '업그레이드 가능 횟수': ''}, 'scroll': {'STR': '80', 'DEX': '75', 'INT': '77', 'LUK': '75', '최대 HP': '365', '최대 MP': '50', '공격력': '62', '마력': '45', '방어력': '342', '점프력': '3', '올스탯': '', '업그레이드 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['캐릭터 기준 10레벨 당10STR', '2', '공격력', '12', '캐릭터 기준 10레벨 당10STR', '1', '1', '']}, 'anrl': {'totalvalue': {}, 'total': {'STR': '371', 'DEX': '295', '최대 HP': '255', '최대 MP': '255', '공격력': '828', '보스 몬스터 공격 시 데미지': '38%', '몬스터 방어율 무시': '20%', '데미지': '5%'}, 'basic': {'STR': '150', 'DEX': '150', '최대 HP': '0', '최대 MP': '0', '공격력': '340', '보스 몬스터 공격 시 데미지': '30%', '몬스터 방어율 무시': '', '데미지': '0%'}, 'chuop': {'STR': '44', 'DEX': '', '최대 HP': '', '최대 MP': '', '공격력': '163', '보스 몬스터 공격 시 데미지': '8%', '몬스터 방어율 무시': '', '데미지': '5%'}, 'scroll': {'STR': '177', 'DEX': '145', '최대 HP': '255', '최대 MP': '255', '공격력': '325', '보스 몬스터 공격 시 데미지': '', '몬스터 방어율 무시': '', '데미지': ''}, 'poten': ['공격력', '12%', '보스 몬스터 공격 시 데미지', '30%', '보스 몬스터 공격 시 데미지', '30%'], 'addipoten': ['공격력', '12%', '공격력', '9%', 'INT', '9%', '%', '', '3', '', '2', '', '1', '', '1200', '']}, 'qpfxm': {'totalvalue': {}, 'total': {'STR': '175', 'DEX': '128', 'INT': '127', 'LUK': '123', '최대 HP': '465', '최대 MP': '260', '공격력': '97', '마력': '90', '방어력': '481', '점프력': '9', '올스탯': '6%', '업그레이드 가능 횟수': '0'}, 'basic': {'STR': '15', 'DEX': '15', 'INT': '15', 'LUK': '15', '최대 HP': '150', '최대 MP': '150', '공격력': '1', '마력': '1', '방어력': '150', '점프력': '0', '올스탯': '0%', '업그레이드 가능 횟수': '0'}, 'chuop': {'STR': '48', 'DEX': '', 'INT': '', 'LUK': '', '최대 HP': '', '최대 MP': '', '공격력': '5', '마력': '', '방어력': '', '점프력': '4', '올스탯': '6%', '업그레이드 가능 횟수': ''}, 'scroll': {'STR': '112', 'DEX': '113', 'INT': '112', 'LUK': '108', '최대 HP': '315', '최대 MP': '110', '공격력': '91', '마력': '89', '방어력': '331', '점프력': '5', '올스탯': '', '업그레이드 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['공격력', '12', '최대 HP', '5%', 'STR', '4%']}, 'rnlrjfdl': {'totalvalue': {}, 'total': {'STR': '215', 'DEX': '152', 'INT': '133', 'LUK': '154', '최대 HP': '800', '최대 MP': '770', '공격력': '123', '마력': '95', '방어력': '246', '올스탯': '5%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': '10'}, 'basic': {'STR': '7', 'DEX': '7', 'INT': '7', 'LUK': '7', '최대 HP': '750', '최대 MP': '750', '공격력': '5', '마력': '5', '방어력': '75', '올스탯': '0%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': ''}, 'chuop': {'STR': '84', 'DEX': '20', 'INT': '', 'LUK': '24', '최대 HP': '', '최대 MP': '', '공격력': '', '마력': '', '방어력': '', '올스탯': '5%', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'scroll': {'STR': '124', 'DEX': '125', 'INT': '126', 'LUK': '123', '최대 HP': '50', '최대 MP': '20', '공격력': '118', '마력': '90', '방어력': '171', '올스탯': '', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'poten': ['STR', '12%', '올스탯', '9%', 'STR', '9%'], 'addipoten': ['최대 MP', '240', '공격력', '11', 'STR', '4%', '1', '', '1100', '']}, 'ruswkd': {'totalvalue': {}, 'total': {'STR': '183', 'DEX': '188', 'INT': '147', 'LUK': '146', '최대 HP': '255', '공격력': '138', '마력': '132', '방어력': '899', '업그레이드 가능 횟수': '0'}, 'basic': {'STR': '35', 'DEX': '35', 'INT': '35', 'LUK': '35', '최대 HP': '0', '공격력': '20', '마력': '20', '방어력': '300', '업그레이드 가능 횟수': '0'}, 'chuop': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '최대 HP': '', '공격력': '', '마력': '', '방어력': '', '업그레이드 가능 횟수': ''}, 'scroll': {'STR': '148', 'DEX': '153', 'INT': '112', 'LUK': '111', '최대 HP': '255', '공격력': '118', '마력': '112', '방어력': '599', '업그레이드 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['STR', '7%', '올스탯', '4%', '20%', '', '1', '']}, 'wkdrkq': {'totalvalue': {}, 'total': {'STR': '373', 'DEX': '243', 'INT': '163', 'LUK': '156', '공격력': '162', '마력': '106', '방어력': '786', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': '7'}, 'basic': {'STR': '40', 'DEX': '40', 'INT': '0', 'LUK': '0', '공격력': '9', '마력': '0', '방어력': '250', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': ''}, 'chuop': {'STR': '168', 'DEX': '36', 'INT': '30', 'LUK': '36', '공격력': '', '마력': '', '방어력': '', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'scroll': {'STR': '165', 'DEX': '167', 'INT': '133', 'LUK': '120', '공격력': '153', '마력': '106', '방어력': '536', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'poten': ['크리티컬 데미지', '8%', '최대 MP', '12%', '크리티컬 데미지', '8%'], 'addipoten': ['크리티컬 데미지', '3%', '최대 HP', '7%', '올스탯', '4%', '1', '']}, 'dpaqmffpa': {'totalvalue': {}, 'total': {'STR': '10', 'DEX': '10', 'INT': '10', 'LUK': '10', '공격력': '2', '마력': '2'}, 'basic': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': ''}, 'chuop': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': ''}, 'scroll': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': ''}, 'poten': ['몬스터 방어율 무시', '35%', '공격력', '9%', '공격력', '9%'], 'addipoten': ['공격력', '12%', '최대 HP', '7%', '공격력', '9%']}, 'qotwl': {'totalvalue': {}, 'total': {'STR': '7', 'DEX': '7', 'INT': '7', 'LUK': '7', '공격력': '7', '마력': '7', '몬스터 방어율 무시': '10%'}, 'basic': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': '', '몬스터 방어율 무시': ''}, 'chuop': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': '', '몬스터 방어율 무시': ''}, 'scroll': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': '', '몬스터 방어율 무시': ''}, 'poten': [], 'addipoten': []}, 'cldgh': {'totalvalue': {}, 'total': {'STR': '7', 'DEX': '7', 'INT': '7', 'LUK': '7', '공격력': '7', '마력': '7', '몬스터 방어율 무시': '10%'}, 'basic': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': '', '몬스터 방어율 무시': ''}, 'chuop': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': '', '몬스터 방어율 무시': ''}, 'scroll': {'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '공격력': '', '마력': '', '몬스터 방어율 무시': ''}, 'poten': [], 'addipoten': ['1153', '', '9', '']}, 'qhwh': {'totalvalue': {}, 'total': {'STR': '10', 'DEX': '10', '공격력': '3'}, 'basic': {'STR': '', 'DEX': '', '공격력': ''}, 'chuop': {'STR': '', 'DEX': '', '공격력': ''}, 'scroll': {'STR': '', 'DEX': '', '공격력': ''}, 'poten': ['보스 몬스터 공격 시 데미지', '30%', '보스 몬스터 공격 시 데미지', '40%', '공격력', '12%'], 'addipoten': ['공격력', '12%', '공격력', '9%', 'STR', '9%']}, 'akdxh': {'totalvalue': {}, 'total': {'STR': '338', 'DEX': '210', 'INT': '170', 'LUK': '176', '최대 HP': '1215', '공격력': '113', '마력': '112', '방어력': '1568', '올스탯': '6%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': '8'}, 'basic': {'STR': '35', 'DEX': '35', 'INT': '35', 'LUK': '35', '최대 HP': '0', '공격력': '6', '마력': '6', '방어력': '450', '올스탯': '0%', '업그레이드 가능 횟수': '0', '가위 사용 가능 횟수': ''}, 'chuop': {'STR': '102', 'DEX': '30', 'INT': '30', 'LUK': '36', '최대 HP': '', '공격력': '', '마력': '', '방어력': '', '올스탯': '6%', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'scroll': {'STR': '201', 'DEX': '145', 'INT': '105', 'LUK': '105', '최대 HP': '1215', '공격력': '107', '마력': '106', '방어력': '1118', '올스탯': '', '업그레이드 가능 횟수': '', '가위 사용 가능 횟수': ''}, 'poten': ['STR', '12%', '올스탯', '6%', 'STR', '9%'], 'addipoten': ['STR', '5%', 'STR', '4%', 'DEX', '4%', '1', '']}, 'tlawkd': {'totalvalue': {}, 'total': {'5': '', 'STR': '22', 'DEX': '22', 'INT': '22', 'LUK': '22', '최대 HP': '50', '공격력': '50', '업그레이드 가능 횟수': '0'}, 'basic': {'5': '', 'STR': '3', 'DEX': '3', 'INT': '3', 'LUK': '3', '최대 HP': '', '공격력': '0', '업그레이드 가능 횟수': '0'}, 'chuop': {'5': '', 'STR': '', 'DEX': '', 'INT': '', 'LUK': '', '최대 HP': '', '공격력': '', '업그레이드 가능 횟수': ''}, 'scroll': {'5': '', 'STR': '19', 'DEX': '19', 'INT': '19', 'LUK': '19', '최대 HP': '', '공격력': '50', '업그레이드 가능 횟수': ''}, 'poten': ['STR', '12%', 'STR', '9%', 'STR', '9%'], 'addipoten': ['INT', '4%', '공격력', '10', '공격력', '10']}}
itemDiagnosis(280,"adele",9000,40,total,ability)