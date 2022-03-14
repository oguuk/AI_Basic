#Q2. 두번째로 Pandas에서 지원하는 Dataframe을 다뤄보도록 하겠습니다. 다음과 같이 과일과 야채 각각 정리된 데이터가 있습니다. 이 두 데이터를 따로 보기엔 효율성이 떨어지니, 각 표에 정리된 데이터를 각각 하나의 데이터 프레임으로 생성한 후 다음 세부 구현을 진행해보세요.

# empty DataFrame을 생성합니다.
# 컬럼명은 자주 사용되니 변수로 저장합니다.
df1 = pd.DataFrame()
colume_name = ['Name', 'Type', 'Price']

# 빈 DataFrame df1에 'Name' 컬럼의 정보를 업데이트 합니다.
# 새로운 colume인 "Name"이 생성되었습니다.
df1['Name'] = ["cherry", "mango", "potato"]
df1

# 나머지 column도 추가합니다.
df1['Type'] = ['Fruit', 'Fruit', 'Vegetable']
df1['Price'] = [100,110,60]
df1

# 컬럼은 모두 추가되었으니 마지막 로우를 추가하기 위해 하나의 row를 가지는 dataframe을 생성합니다.
# df1에 append를 추가하여 저장하기 위해서는 append한 결과를 다시 df1에 저장해야 합니다.
# 이 때 새롭게 추가되는 로우는 기존의 index를 유지하기 때문에 dataframe의 index를 다시 생성하기 위해 ignore_index = True를 사용합니다.
df1_lastrow = pd.DataFrame([['onion', 'Vegetable', 80]], columns = ["Name", "Type", "Price"])
df1 = df1.append(df1_lastrow, ignore_index = True)
df1

# 두 번째 DataFrame은 바로 생성합니다.
df2 = pd.DataFrame([['peper',   'Vegetable',  50],
                    ['carror',  'Vegetable',  70],
                    ['banana',  'Fruit',      90],
                    ['kiwi',    'Fruit',      120]],
                   columns = colume_name)
df2

# df1, df2를 columns를 이용해 결합
df3 = pd.concat([df1, df2], axis=0)
df3

# index를 새롭게 만들기 위해서 ignore_index를 true로 사용합니다.
df3_reindexed = pd.concat([df1, df2], axis=0, ignore_index=True)
df3_reindexed

# Fruit와 Vegetable의 type에 따라서 정렬하고, 각각의 정렬 결과의 가격을 내림차순으로 정리
df_fruit = df3.loc[(df3['Type'] == 'Fruit') |  (df3['Type'] == 'Vegetable')]
sorted_df = df_fruit.sort_values(by='Price', ascending=False)
sorted_df

# groupby를 이용하여 type을 묶고 price 정보를 .apply()를 이용하여 sorting함
g = df3_reindexed.groupby('Type')['Price']
g_sorted =g.apply(lambda x: x.sort_values(ascending=False))
g_sorted

print(f"Sum of Top 2 Fruit Price : {g_sorted['Fruit'].iloc[0:2].sum()}")
print(f"Sum of Top 2 Vegetable Price : {g_sorted['Vegetable'].iloc[0:2].sum()}")

# Pivot table
p = df3_reindexed.pivot(values='Price', columns='Type')
p

sorted_p = p.sort_values(by=['Fruit'], ascending = False)
print(f"Sum of Top 2 Fruit Price : {sorted_p['Fruit'].iloc[0:2].sum()}")
sorted_p

sorted_p = p.sort_values(by=['Vegetable'], ascending = False)
print(f"Sum of Top 2 Vegetable Price : {sorted_p['Vegetable'].iloc[0:2].sum()}")

# sorted_df는 type이 'Fruit'인 로우와 'Vegetable'인 로우가 합쳐진 dataframe입니다.
# 따라서 fruit 로우만 필터링하기 위해 sorted_df['Type'] == 'Fruit' 를 사용합니다.
# 그리고 그 결과에 'Price'컬럼으로 다시 필러링하기위해 ['Price'] 를 사용합니다.
print(f"Sum of Top 2 Fruit Price : {sorted_df[sorted_df['Type'] == 'Fruit']['Price'].iloc[0:2].sum()}")
print(f"Sum of Top 2 Vegetable Price : {sorted_df[sorted_df['Type'] == 'Vegetable']['Price'].iloc[0:2].sum()}")
