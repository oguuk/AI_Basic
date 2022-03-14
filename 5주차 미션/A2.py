#Q2.데이터가 준비가 되었다면, 이제 그 데이터를 학습할 모델을 구현할 차례입니다. 그후 모델 안의 가중치를 초기화시켜보세요. 입력 데이터 형태에 맞도록 linear한 모델을 구성해보세요.
#
#MNIST 입력의 크기는 28x28입니다.
#여기서 구현하는 linear 모델은 입력이 1차원이기 때문에 입력 차원을 맞춰보세요.

#step2 데이터 학습 모델 구현
#모델 안 가중치 초기화 -- linear ~ 모델 구성
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#MNIST data image of shape 28*28
#linear(input개수: mnist가 28*28개의 값을 가짐, output개수: (mnist가 0~9 레이블을 가짐 ~ 10개))
linear = torch.nn.Linear(784, 10, bias=True).to(device)
#weight init
torch.nn.init.normal_(linear.weight)
