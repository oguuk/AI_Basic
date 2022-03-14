# 문제:
# string 연산을 이용해서 문자열을 자르는 연산을 사용해보세요.

inputs = "cat32dog16cow"

def find_string(inputs: str):
    return "".join([i if not i.isdigit() else " " for i in inputs ]).split() # 숫자인 경우만 띄어쓰기로 str를 변경, 띄어쓰기 단위로 split한 리스트 return

string_list = find_string(inputs)
print(string_list)

# 출력
# ['cat', 'dog', 'cow']
