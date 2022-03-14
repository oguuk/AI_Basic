#Q4. 경사 하강법 구현을 위해서 위에서 분리한 x_train 데이터와 계산될 weight, bias 값을 정의해보세요. 여기서 구현한 weight와 bias 는 linear regression 계산을 진행할시 직선의 기울기와 y 절편의 값이 됩니다.
#
#numpy 내의 random 함수를 이용해보세요.

beta_gd = np.random.rand(1)
bias = np.random.rand(1)
print(beta_gd, bias)
