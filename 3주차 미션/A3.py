#Q3. 3번부터 5번까지의 미션는 Numpy를 이용해서 정답값을 예측해보는 linear regression을 구현해 보는 미션입니다. 첫번째 단계로 데이터를 준비해보도록 하겠습니다. 아래와 같이 데이터가 주어져있을 때, 경사하강법을 위한 데이터를 분리해보세요.
#
#주어진 xy 데이터를 이용해서 학습과 정답 데이터를 준비해보세요. 추가 수정 문제에서 주어진 xy에서 대괄호를 한 번 더 묶어주어야 문제 해결이 가능합니다. (차원 관련) (np.array([[1., 2., 3., 4., 5., 6.], [10., 20., 30., 40., 50., 60.]])

import numpy as numpy

xy = np.array([[1,2,3,4,5,6], [10,20,30,40,50,60]], float)

x_train = xy[0,:]
y_train = xy[1,:]

print(x_train, x_train.shape)
print(y_train, y_train.shape)
