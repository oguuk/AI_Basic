#Q5. 학습이 완료되면, 모델이 잘 동작하는지 테스트가 필요합니다. 데이터로드 파트에서 준비했던 테스트 데이터를 이용해 테스트를 진행해봅시다. 아래 테스트 코드를 완성해보세요.


#step5 데이터로드 ~ 모델 작동 테스트
linear.eval()
with torch.no_grad(): #이 범위 내에서 grad계산 안하겠다. 테스트시 사용
  correct = 0
  total = 0
  for i, (imgs, labels) in enumerate(test_loader):
    imgs, labels = imgs.to(device), labels.to(device)
    imgs = imgs.view(-1, 28 * 28)
#예측 결과를 outputs에 저장
    outputs = linear(imgs)
#ouptputs에 저장된 예측 결과를 실제간 계산
    _, argmax = torch.max(outputs, 1) #max()를 통해 최종 출력이 가장 높은 class 선택
    total += imgs.size(0)
    correct += (labels == argmax).sum().item()

  print('Test accuracy for {} images: {:.2f}%'.format(total, correct / total * 100))

  #+++ Visualization

import matplotlib.pyplot as plt
import random

r = random.randint(0, len(mnist_test) - 1)
X_single_data = mnist_test.test_data[r:r + 1].view(-1, 28 * 28).float().to(device)
Y_single_data = mnist_test.test_labels[r:r + 1].to(device)

print("Label: ", Y_single_data.item())
single_prediction = linear(X_single_data)
print("Prediction: ", torch.argmax(single_prediction, 1).item())

plt.imshow(mnist_test.test_data[r:r + 1].view(28, 28),
           cmap="Greys", interpolation="nearest")
plt.show()
