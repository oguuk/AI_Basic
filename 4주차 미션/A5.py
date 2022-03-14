#Q5. Matplotlib을 이용해서 아래와 같은 데이터가 주어졌을때, 출력 예시와 같은 형태로 그래프를 출력해보세요.
#
#각 그룹별 데이터를 다른 형식의 그래프로 생성해보세요. 각각 막대, 점, 선 그래프입니다.

names = ['ground_a', 'ground_b', 'ground_c']
values = [1, 10, 100]

plt.figure(figsize = (9,3))
plt.subplot(1, 3, 1)
plt.bar(names, values)
plt.subplot(1, 3, 2)
plt.plot(names, values, 'bo')
plt.subplot(1, 3, 3)
plt.plot(names, values, '-')
plt.show()
