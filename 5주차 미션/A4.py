#Q4. 3번 문제까지 해결하셨다면, 이제 학습을 위한 준비는 거의 끝났다고 볼 수 있습니다. 위 구현 함수들을 이용해 학습 Loop를 구현해보세요.
#위에서 구현한 모델, optimzer, loss fn 등을 이용해 학습을 구현해주세요.


for epoch in range(training_epochs):
    for i, (imgs, labels) in enumerate(train_loader):
        #input 데이터 얻음
        imgs, labels = imgs.to(device), labels.to(device)
        # MNIST 이미지 : 흑백이미지 / 채널 1개를 가짐
        #imgs는 처음에 (batch_size, 1, 28, 28)의 형태 - view함수를 통해 (28*28) 형태로 변형
        #-1은 데이터를 수정하고 복사본을 만들지 않음을 의미
        imgs = imgs.view(-1, 28 * 28)

        #input 데이터에 대한 y=wx+b 형태의 선형 변환 수행, prediction한 값 출력
        outputs = linear(imgs)
        #loss 계산
        loss = criterion(outputs, labels)
        
        # loss 이용해 모델 개선
        #gradient를 0으로 초기화
        optimizer.zero_grad()
        #loss function을 미분해 gradient 계산, backward 연산
        loss.backward()
        # 가중치, 편향 업데이트
        optimizer.step()

        #각 배치별로 가장 높은 가능성의 숫자 클래스를 뽑아줌
        _, argmax = torch.max(outputs, 1)
        #labels == argmax 둘이 일치하는 개수 평균의 정확도
        accuracy = (labels == argmax).float().mean()
        
        #100번마다 출력
        if (i+1) % 100 == 0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%'.format(
                epoch+1, training_epochs, i+1, len(train_loader), loss.item(), accuracy.item() * 100))
