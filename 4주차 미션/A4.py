#Q4. 이번 미션부터는 Matplotlib을 이용해 간단히 그래프를 출력해보도록 하겠습니다. 다음과 같은 데이터 t가 주어져있을때, 출력 예시로 제안된 그래프를 출력해보세요.
#
#Plot 함수 내 각 마커의 색상과 모양을 표현하는 방법을 확인해보세요.

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
y1 = np.exp(t)
y2 = 0.3*np.exp(t)
y3 = 1.1*t
plt.plot(t,y1, 'b^')
plt.plot(t,y2, 'gs')
plt.plot(t,y3, 'r--')

plt.show()
