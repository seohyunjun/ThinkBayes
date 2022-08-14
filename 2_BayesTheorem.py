
# 베이즈 테이블

import pandas as pd
table = pd.DataFrame(index = ['Bowl 1','Bowl 2'])

# P(H|D)

# P(H)
# 사전 확률 추가
table['prior'] = 1/2, 1/2
table

# 가능도 추가 P(D|H)
table['liklihood'] = 3/4, 1/2
table
#         prior
# Bowl 1    0.5
# Bowl 2    0.5

# P(H)*P(D|H) = P(H and D) 
table['unnorm'] = table['prior'] * table['liklihood']
#         prior  liklihood  uniform
# Bowl 1    0.5       0.75    0.375
# Bowl 2    0.5       0.50    0.250

# 사후 확률 P(D) = P(D_1)*P(H|D_1) + P(D_2)*P(H|D_2) 
prob_data = table['unnorm'].sum()
prob_data # 0.625


# 사전 확률 P(H|D) = P(H)*P(D_1|H) / P(D) + P(H)*P(D_2|H) / P(D)
table['posterior'] = table['unnorm'] / prob_data
table


# Dice Problem
table2 = pd.DataFrame([6,8,12])

# 사전 확률과 가능도 추가
from fractions import Fraction
table2['prior'] = Fraction(1,3)
table2['likelihood'] = Fraction(1,6), Fraction(1,8), Fraction(1,12)
#     0 prior likelihood
# 0   6   1/3        1/6
# 1   8   1/3        1/8
# 2  12   1/3       1/12

# 사전 확률 구하기
def update(table):
    """사후 확률 계산"""
    table['unnorm'] = table['prior'] * table['likelihood']
    prob_data = table['unnorm'].sum()
    table['posterior'] = table['unnorm'] / prob_data
    return prob_data
    
    
prob_data = update(table2)
print(table2)
#     0 prior likelihood unnorm posterior
# 0   6   1/3        1/6   1/18       4/9
# 1   8   1/3        1/8   1/24       1/3
# 2  12   1/3       1/12   1/36       2/9

# 몬티홀 문제
table3 = pd.DataFrame(['Door 1', 'Door 2', 'Door 3'])
table3['prior'] = Fraction(1,3)

# 몬티 3번 방은 염소 꽝
table3['likelihood'] = Fraction(1,2), 1, 0
table3 

update(table3)
table3
#         0 prior likelihood unnorm posterior
# 0  Door 1   1/3        1/2    1/6       1/3
# 1  Door 2   1/3          1    1/3       2/3
# 2  Door 3   1/3          0      0         0
