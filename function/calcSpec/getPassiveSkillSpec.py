#직업, 레벨에 따라 스펙이 달라짐
def getPassiveSkillSpec(job,level):
    
    #펫세트효과 - 공마 27
    #매직서킷 - 해방무기 51?
    
    #페이스 - 크뎀10% 공10%
    #여제의 축복 - 공마 30
    

    #1차스킬
    #루디먼트 - 공 30
    #2차스킬
    #마스터리 - 공 30
    #트레인 - 힘 60
    #3차스킬
    #어센트 - 공 30 최종데미지 15%
    #4차스킬 - 컴뱃 통함
    #엑스퍼트 공30
    #데몰리션 최종데미지 30% 방무 20%
    #어테인 공 30 보공 10% > 쓸컴뱃 공32 보공11%

    #메용 15%
    #5차스킬
    #쓸샾 - 올스탯 1
    #블링크 - 공마 30
    #바오스 - 힘 30
    
    #아델
    #str, dex, int, luk, att, mtt, attp, mttp, btt, final_dmg, igd, cridmg, dmg
    if job == "adele":
        return 90, 0, 0, 0, 239, 0, 10, 0, 11, 50.65, 21, 18, 0
    return 90, 0, 0, 0, 239, 0, 10, 0, 11, 50.65, 21, 18, 0