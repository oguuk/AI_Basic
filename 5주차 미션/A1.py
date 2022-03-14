#Q1. 가장 먼저 학습 데이터를 준비해보도록 하겠습니다. MNIST 데이터셋을 직접 Load 해 봅시다. 데이터셋을 로드하고 DataLoader를 구현해보세요.
#
#DataLoader를 이용해 MNIST 데이터셋을 로드해봅시다.

#댕댕이
import torch
# torch.nn 을 nn 이름으로 불러옴
import torch.nn as nn
#PyTorch의 패키지 중 하나인 torchvision에서 데이터 셋이나 모델 아키텍처를 불러올 수 있음
#torchvision패키지 내의 datasets 서브 패키지를 dset의 이름으로 불러옴
import torchvision.datasets as dset
#torch.utils.data패키지의 DataLoader 서브 패키지를 불러옴
from torch.utils.data import DataLoader

#학습 시 전체 training set 사용 횟수 : 15
training_epochs = 15
#학습기 1회 학습 시 사용되는 데이터의 양 : 100
batch_size = 100

#경로 설정
root = './data'
#train: 가져올 데이터 표시 - 테스트용(True) or 학습용(False)
# transform: 불러올 데이터 형태 표시 - 일반 이미지 (0-255사이의 값, (H, W, C) 형태) / pytorch (0-1사이의 값, (C, H, W)의 형태)
# download : True = MNIST 데이터가 없을 시 다운
#MNIST DATA 트레이닝셋 불러옴 (train=True)
mnist_train = dset.MNIST(root=root, train=True, transform=transforms.ToTenser(), download=True)
#MNIST DATA 테스트셋 불러옴 (train=False)
mnist_test = dset.MNIST(root=root, train=False, transform=transforms.ToTenser(), download=True)
