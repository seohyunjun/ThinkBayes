# http://gss.norc.org

### 

# 제너럴 소셜 서베이의 직업 데이터 사용
import pandas as pd
import os
os.chdir("/Users/hyunjunseo/Desktop/STUDY/ThinkBayes")

gss = pd.read_csv('data/gss_bayes.csv',index_col=0)
gss.head()

gss.columns # ['year', 'age', 'sex', 'polviews', 'partyid', 'indus10']

# 1974 ~ 2016 설문지

## "indus10" == 은행원
banker = gss[gss['indus10']==6870]

print(f'은행원의 수 : {len(banker   )}') # 728
print(f'은행원의 비율 : {len(banker)/len(gss)*100}%') # 1.47%


bank = gss['indus10']==6870 # 직업 : 은행원
female = gss['sex']==2 # 성별 : 여
liberal = gss['polviews']<=3 # 정치 성향(0~7점 척도 진보 - 보수) : 진보 성향
democrat = gss['partyid']<=1 # 적극적 민주당원(0~7점 척도 적극적 민주당원 - 다른 정당원) : 민주당원

def prob(A):
    """주어진 A의 확률을 구함."""
    return A.mean()

prob(bank) # 0.014
prob(female) # 0.537
prob(liberal) # 0.273
prob(democrat) # 0.36

# prob(female) * prob(bank) == sum((gss['indus10']==6870) & (gss['sex']==2))/len(gss)

# 조건부 확률 구하기
selected = democrat[liberal] # 진보성향을 가진 민주당원의 비율
prob(selected) # 0.52

selected = female[bank] # 은행원 중 여자일 경우
prob(selected)

def conditional(proposition, given):
    return prob(proposition[given])

conditional(liberal, given=female) # 여성 중 은행원 경우 0.27
 
 
# 조건부확률은 교환이 가능하지 않다
conditional(female, given=bank) # 0.77
conditional(bank, given=female) # 0.021 

## 조건과 논리곱
conditional(female, given=liberal&democrat) # 0.57 진보성형+민주당원 중 여성 
conditional(liberal&democrat, given=bank) # 0.10 은행원 중 진보성형+민주당원

## 확률 법칙
# 1. 논리 곱을 사용한 조건부확률 계산
# 2. 조건부확률을 사용한 논리곱 계산
# 3. conditional(A,B)를 사용한 conditional(B,A) 계산

# P(A)는 명제 A에 대한 확률이다
# P(A and B)는 A와 B의 논리곱의 확률이다. 즉 A와 B 모두 참일 확률이다.
# P(A|B)는 B가 주어졌을 때 A가 참일 확률이다. A와 B 사이 세로선은 'given'으로 읽는다.

## Theorem 1 
# Q1. 은행가 중 몇 %나 여성일까? 
# case 1
female[bank].mean() # 0.77
# case 2
conditional(female, given=bank) # 0.77
# case 3 응답자 중 여성 은행원 비율을 구하고, 응답자 중 은행원의 비율을 구한다.
prob(female & bank) / prob(bank) # 0.77

## Theorem 2
# P(A and B) = P(B)*P(A|B)
prob(liberal & democrat) # 0.14
prob(democrat) * conditional(liberal, given=democrat)

## Theorem 3
# P(A and B) = P(B and A)
## ** Con : P(B)P(A|B)=P(A)P(B|A)
conditional(liberal, given=bank)
prob(liberal)*conditional(bank, given=liberal)/prob(bank)

## 전체확률의 법칙
# P(A) = P(B_1 and A) + P(B_2 and A)

# 상호 배제, 이는 전체 B 중 하나만 참인 경우다.
# 전체 포괄, 이는 전체 B 중 하나는 반드시 참이다.


male = (gss['sex']==1) 
prob(bank) # 0.014 
prob(male&bank) + prob(female&bank) # 0.014 
prob(bank) == prob(male&bank) + prob(female&bank) # True

## con : P(A) = P(B_1)P(A|B_1) + P(B_2)P(A|B_2) 

prob(bank) == prob(male).mean()*conditional(bank, given=male) + prob(female).mean()*conditional(bank, given=female) # True

# P(A) = Sum_i{P(B_i)P(A|B_i)}
B = gss['polviews']
B.value_counts().sort_index()
# 4 = 정치 성향 중도
i = 4 
prob(B==i) * conditional(bank, B==i)

prob(B) * conditional(bank, B) == sum(prob(B==i) * conditional(bank, B==i) for i in range(1,8)) # True


prob(female&bank)


conditional(liberal, given=democrat)
conditional(democrat, given=liberal)