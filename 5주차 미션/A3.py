#Q3. 위에서 구현한 모델을 학습시키기 위해서는 loss 함수와 opitmizer가 필요합니다. 아래 제시된 loss 함수와 optimizer를 구현해보세요. Loss 함수와 optimizer는 모델 안의 가중치를 업데이트 할 때 사용됩니다.
#
#옵티마이저는 SGD, Loss는 Cross Entropy Loss를 사용합니다.


#가중치 초기화 - 초기화 함수: Normal distribution
torch.nn.init.normal_(linear.weight)
#손실함수(Loss function), Linear Model(딥러닝 모델)을 통한 최종값(Score) 구함
#Softmax 함수를 통해 이 값들의 범위는 [0,1], 총 합은 1이 되도록 함
#그 후 1-hot Label(vector) (정답 라벨(vector))과의 Cross Entropy를 통해 Loss를 구함
criterion = torch.nn.CrossEntropyLoss().to(device)
#확률적 경사 하강법(Stochastic Gradient Descent Optimizer) 사용, learning rate:0.1
optimizer = torch.optim.SGD(linear.parameters(), lr=0.1)
