import numpy as np
import matplotlib.pyplot as plt
from process import MarkonChain

p = np.array([[0.8, 0.1, 0.1, 0],
              [0.7, 0, 0.3, 0],
              [0.6, 0.1, 0.1, 0.2],
              [0.5, 0.3, 0.1, 0.1]])
mc = MarkonChain(4, np.array([0.25, 0.25, 0.25, 0.25]), p)

N_fin = 40
states = mc.simulate(N_fin)
mat = mc.simulate_distribution(200, N_fin)
print('simulated stationary distribution: ', mat[:, N_fin - 1])
stationary_distribution = mc.stationary()
for d in stationary_distribution:
    print('stationary distribution: ', d)
fig, ax = plt. subplots(nrows=2, ncols=1)
ax[0].plot(range(N_fin), states, marker='o')
im = ax[1].matshow(mat)
fig.colorbar(im, ax=ax[1])
plt.show()
