from function.calcSpec import getHyperStatSpec as ghs
from function.calcSpec import getLinkSpec as gls
from function.calcSpec import getUnionSpec as gus

#print(ghs.getHyperStatSpec(280))


"""
Input : Level    ==>  Calc : 하이퍼스탯 (getHyperStatSpec.py)
Input : Union Level, Job ==> Calc : 유니온 점령효과 (getUnionSpec.py)
Input : X => Calc : 링크 효과 (getLinkSpec.py)
Input : Job, Level ==> Calc : 패시브스킬(0,1,2,3,4,5차) (getPassiveSkillSpec.py)
Input : Farm Level ==> Calc : 농장 보유효과
Input : Doping ==> Calc : 도핑 종류에 따른 증가치
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
