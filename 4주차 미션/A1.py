#Q1. 먼저 Pandas에서 지원하는 Series에 대해서 한번 다뤄보겠습니다.아래와 같이 인덱스와 데이터가 주어져있을때 Pandas의 Series 형태로 만들어보세요.
#
#주어진 데이터에서 10이상 20이하의 데이터만 출력하는 Series를 재정의 해보세요.

import pandas as pd

idx = ['HDD', 'SSD', 'USB', 'CLOUD']
data = [19, 11, 5, 97]

print("<1-0>")
series = pd.Series(data, index =idx)
print(series)


# boolean 선택은 condition을 만족하는 데이터의 index에서 True 의 값을 갖습니다.
print()
print("<1-1>")
bool_cond = (series >= 10) & (series <=20)
for data, cond in zip(series,bool_cond):
  print (f"data: {data}, boolean cond: {cond}")

# boolean 선택을 이용하여 원하는 condition을 만족하는 데이터를 필터링합니다.
print()
print("<1-2>")
series_10_to_20 = series[(series >= 10) & (series <=20)]
print(series_10_to_20)
