import numpy as np
import matplotlib.pyplot as plt
from markov_chain import MarkonChain

p = np.array([[0.8, 0.1, 0.1, 0],
              [0.7, 0, 0.3, 0],
              [0.6, 0.1, 0.1, 0.2],
              [0.5, 0.3, 0.1, 0.1]])
mc = MarkonChain(4, np.array([0.25, 0.25, 0.25, 0.25]), p)
#print(mc.eig())
N_fin = 30
states = mc.simulate(N_fin)
mat = mc.simulateDistribution(60, N_fin)
fig, ax = plt. subplots(nrows=2, ncols=1)
ax[0].plot(range(N_fin), states)
im = ax[1].matshow(mat)
fig.colorbar(im, ax=ax[1])
plt.show()
