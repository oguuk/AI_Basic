#Q1. 본격적으로 Numpy와 친해지기 위해서 다양한 연산을 연습해볼 예정입니다. 무작위의 데이터를 가 진 5x3의 행렬을 가지는 numpy array와 3x2 행렬을 가지는 numpy array를 만든 후 행열곱 연산을 진행해보세요.

import numpy as np

arr1 = np.arange(1,16).reshape(5,3)
arr2 = np.array([[1,1/4],[1/2,1/5],[1/3,1/6]], float)
print(arr1)
print(arr2)
print(arr1.shape)

# 행렬의 곱연산
# 1. numpy.dot() : 두 벡터(vector)의 내적, 내적곱
# - dot는 행렬과 상수(constant)의 곱셈을 허용하지만, matmul은 Error를 일으킨다.
# 2. numpy.matmul (@ operator)
# - 만약 배열이 2차원보다 클 경우, 마지막 2개의 축으로 이루어진 행렬을 나머지 축에 따라 쌓아놓은 것이라고 생각한다.
# 3. element-wise multiplication (* operator)

ans = np.dot(arr1, arr2)
print(ans)
print(ans.shape)

ans = np.matmul(arr1, arr2)
print(ans)
print(ans.shape)
