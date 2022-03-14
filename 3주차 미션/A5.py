#Q5. 이제 최종적으로 linear regression을 경사하강법으로 학습하는 코드를 구현해봅시다. 경사하강법 구현을 위한 학습 Loop를 구현해보세요. 최종적으로 1000회 반복했을 시에 결과를 출력하세요.
#
#단, Error는 차이의 제곱을 이용해서 계산해주세요. Gradient 값은 우리가 예측하는 각 변수에 대한 미분값입니다.

import numpy as np

xy = np.array([[1.,2.,3.,4.,5.,6.],[3.,6.,9.,12.,15.,18.]])

x_train = xy[0]
y_train = xy[1]

# beta_gd 는 선형회귀함수의 임의의 기울기
# bias 는 선형회귀함수의 임의의 y절편
beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate =0.001

for i in range(1000):
    # 임의의 w와 b에 의한 기대값(pred)
    # error 오차(실제값-기대값) 제곱의 평균 = 임의의 w와 b에서 평균제곱 오차(MSE)
    pred = (x_train*beta_gd) + bias
    error = ((y_train-pred)**2).mean()


    # gd_w 는 손실(error) 함수를 w에 대해서 편미분하여 얻은, 임의의 beta_w값에서의 기울기
    # gd_b 는 손실(error) 함수를 b에 대해서 편미분하여 얻은, 임의의 bias에서의 기울기
    gd_w =((pred - y_train)*2*x_train).mean()
    gd_b = ((pred - y_train)*2).mean()

    #error가 최소가 될때까지 가중치w와 bias를 찾아감... learning_rate 율 만큼 기울기 방향으로 이동한 새로운 w와 b를 도출
    beta_gd -= learning_rate*gd_w
    bias -= learning_rate*gd_b

    if i%100 ==0:
        print('Epoch ({:10d}/1000) error:{:10f}, W: {:10f}, b:{:10f}'.format(i, error, beta_gd.item(), bias.item()))
