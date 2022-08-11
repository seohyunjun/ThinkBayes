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

print(f'은행원의 수 : {len(banker)}') # 728
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

conditional(liberal, given=female) # 진보성향 중 여성일 경우 0.27
 
 