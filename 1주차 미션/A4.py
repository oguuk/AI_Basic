# 문제:
# 중복되는 물품은 합쳐서 표시하세요.
# 각 딕셔너리 데이터의 데이터의 키값을 이용해 중복을 확인해보세요.

dict_first = {'사과':30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dict(dict_first: dict, dict_second: dict):
    for k in dict_second.keys(): # 두번째 딕셔너리에 있는 키에 대해 반복
        if k in dict_first: # 두번째 딕셔너리의 키가 첫번째 딕셔너리에도 있으면
            dict_first[k] += dict_second[k] # 값을 더해서 저장
        else: # 두번째 딕셔너리의 키가 첫번째 딕셔너리에 없으면
            dict_first[k] = dict_second[k] # 새로운 키, 값 쌍 생성
    return dict_first # 딕셔너리 return

print(merge_dict(dict_first, dict_second))

# 출력
# {'사과': 35, '배': 30, '감': 35, '포도': 10, '귤': 25}
