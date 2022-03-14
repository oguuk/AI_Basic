#Q2. 두번째로는 numpy에서 자주 사용하는 concatenate 연산에 대한 미션을 수행해보겠습니다. 이제 Numpy에서 사용하는 2개의 numpy array가 있을때, 두 numpy array의 concatenate 연산을 구해보세요.
#
#axis는 0, 1 두개로 연산한 결과를 출력해보세요.
#각 데이터가 어떤 형태로 더해지는지 확인해보세요.

# 2-1
arr1 = np.array([[5,7],[9,10]], float)
arr2 = np.array([[2,4],[ 6,8]], float)
print(arr1)
print(arr2)

np.concatenate((arr1, arr2), axis = 0)
np.concatenate((arr1, arr2), axis = 1)
