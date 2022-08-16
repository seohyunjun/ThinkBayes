# 확률 질량 함수
## PMF(probability.mass.function)는 각 가능한 결괏값에 각각의 확률을 연결해 주는 함수

# empiricaldist는 확률질량함수를 나타내는 Pmf라는 클래스를 제공한다.
from os import popen
from sklearn.covariance import log_likelihood
from transformers import PROPHETNET_PRETRAINED_MODEL_ARCHIVE_LIST
from empiricaldist import Pmf

coin = Pmf()
coin['heads'] = 1/2
coin['tails'] = 1/2
coin
#heads    0.5
#tails    0.5

die = Pmf.from_seq([1,2,3,4,5,6])
die
# 1    0.166667
# 2    0.166667
# 3    0.166667
# 4    0.166667
# 5    0.166667
# 6    0.166667

# 결과값이 한 번 이상 나타나는 경우
letters = Pmf.from_seq(list('Mississippi'))
letters
# M    0.090909
# i    0.363636
# p    0.181818
# s    0.363636

letters('s')
# 0.363636
letters('t')
# 0

die([1,4,7]) # 시퀀스를 넣어 확률의 시퀀스를 얻기도 가능하다.
# array([0.16666667, 0.16666667, 0.])

## Cookie A : V x 30 + C x 10 B : V x 20 + C x 20
# 박스에서 하나를 선택해서 쿠키를 집을때 바닐라 쿠키였다면, A 박스 일 확률
prior = Pmf.from_seq(['Bow1 1','Bow1 2'])
prior

likelihood_vanilla = [0.75, 0.5]
posterior = prior * likelihood_vanilla
posterior
# Bow1 1    0.375
# Bow1 2    0.250

posterior.normalize()
# 0.625

posterior('Bow1 1')
# 사후 확률 값
# 0.6

# 꺼냇던 쿠리를 다시 넣고 같은 그릇에서 쿠키를 꺼냈을때 이 쿠키가 바닐라라면
posterior *= likelihood_vanilla
posterior.normalize()
posterior

# Bow1 1    0.692308
# Bow1 2    0.307692

# 꺼냇던 쿠리를 다시 넣고 같은 그릇에서 쿠키를 꺼냈을때 이 쿠키가 초콜릿이라면
likelihood_chocolate = [0.25, 0.5]
posterior *= likelihood_chocolate
posterior.normalize()
posterior
# Bow1 1    0.529412
# Bow1 2    0.470588

