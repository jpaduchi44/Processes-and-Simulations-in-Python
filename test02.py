import numpy as np
from process import MarkonChain

p = np.array([[0.5, 0.5, 0, 0],
              [0.5, 0.5, 0, 0],
              [0, 0, 0.5, 0.5],
              [0, 0, 0.5, 0.5]])
mc = MarkonChain(4, np.array([0.5, 0, 0.5, 0]), p)

stationary_distribution = mc.stationary()
for d in stationary_distribution:
    print('stationary distribution: ', d)
print(mc.eig())