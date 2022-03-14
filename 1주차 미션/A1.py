# 문제 1:
# num_list 가 홀수인 데이터만 출력하도록 하는 함수를 작성해보세요.

# 주어진 리스트
num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    return list(filter(lambda x: x%2==1, num_list)) # filter함수와 lambda식을 활용해 홀수인 경우만 리스트 형태로 return

print(get_odd_num(num_list))

# 출력
# [1, 5, 7, 15, 29]
