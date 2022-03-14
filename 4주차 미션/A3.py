#Q3. 총 5명에서 게임을 진행했습니다. 총 5개 라운드를 진행했고, 각각 참여자당 5개의 점수를 받았습니다. 주어진 데이터를 dataframe의 형태로 만든 후 각 세부 구현을 진행해보세요.
#
#참여자의 이름을 index로 해서 각 라운드의 columns를 추가해 데이터를 정리해보세요. 6번째 라운드의 점수가 아래와 같을 때, 이를 추가해보세요. 각 데이터의 mean, max, min 값을 출력해보세요.

idx = ['Sue', 'Ryan', 'Jay', 'Jane', 'Anna']
col = ['round_1', 'round_2', 'round_3', 'round_4', 'round_5']
data = [[55,65,60,66,57],
        [64,77,71,79,67],
        [88,81,79,89,77],
        [45,35,30,46,47],
        [91,96,90,97,99]]

# 위 데이터를 이용해 dataframe을 구성해보세요
df = pd.DataFrame(data = data, index = idx, columns = col)
df

# df에 새로운 column인 round_6의 데이터 [11,15,13,17,19]를 추가해 보세요

# 새로운 column을 넣을 때 index를 확인해야 합니다. 생성한 dataframe의 index가 기본으로 생성된 index가 아니기 때문에
# index를 지정하지 않고 새로운 'round_6' column을 추가한 경우 정보가 업데이트 되지 않았습니다.
df['round_6'] = pd.Series([11,15,13,17,19])
df

# data frame과 동일한 index로 정의하여 값을 추가하면 column이 추가됨을 확인할 수 있습니다.
df['round_6'] = pd.Series([11,15,13,17,19], index = idx)
df

df.describe()

# 각 데이터의 mean, max, min값을 구해 출력해 보세요.
# 데이터는 row로 표현되고 각 데이터의 특성이 열로 표현되도록 transpose를 수행했습니다.
mean_max_min = df.describe().loc[['mean', 'max', 'min']].T
mean_max_min
