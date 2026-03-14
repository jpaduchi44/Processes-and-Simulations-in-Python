import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.animation as mpla

'''def ising(n: int, beta: float, N_fin: int):
    bf = np.exp(-2 * beta)
    fig, ax = plt.subplots(nrows=1, ncols=2)
    grid = 2 * np.random.randint(2, size=(n, n)) - 1
    ax[0].matshow(grid)
    for _ in range(N_fin):
        i = np.random.randint(n)
        j = np.random.randint(n)
        neighbour_sum = grid[i, j] * (grid[(i+1)%n,j] + grid[(i-1)%n,j] + grid[i,(j+1)%n] + grid[i,(j-1)%n])
        if neighbour_sum <= 0 or np.random.rand() < bf ** neighbour_sum:
            grid[i, j] = - grid[i, j]
    ax[1].matshow(grid)
    plt.show()'''

class Isisng2D:
    def __init__(self, n: int, beta: float):
        self.n = n
        self.boltzman_factor = np.exp(-2 * beta)
        self.config = 2 * np.random.randint(2, size=(n, n)) - 1
        self.cmap = ListedColormap(['k', 'w'])

    def set_config(self, config: np.ndarray):
        self.config = config

    def initialize_with(self, initialization):
        config = np.ones((self.n, self.n))
        if initialization == 'half':
            config[:, self.n // 2 :] = -config[:, self.n // 2 :]
        if initialization == 'blobs':
            for _ in range(30):
                i = np.random.randint(self.n)
                j = np.random.randint(self.n)
                config[i, j] = -config[i, j]
                config[(i+1)%self.n, j] = -config[(i+1)%self.n, j]
                config[(i-1)%self.n, j] = -config[(i-1)%self.n, j]
                config[i, (j+1)%self.n] = -config[i, (j+1)%self.n]
                config[i, (j-1)%self.n] = -config[i, (j-1)%self.n]
                config[(i+1)%self.n, (j+1)%self.n] = -config[(i+1)%self.n, (j+1)%self.n]
                config[(i-1)%self.n, (j+1)%self.n] = -config[(i-1)%self.n, (j+1)%self.n]
                config[(i+1)%self.n, (j-1)%self.n] = -config[(i+1)%self.n, (j-1)%self.n]
                config[(i-1)%self.n, (j-1)%self.n] = -config[(i-1)%self.n, (j-1)%self.n]
        self.set_config(config)

    def step(self):
        i = np.random.randint(self.n)
        j = np.random.randint(self.n)
        neighbour_sum = self.config[i, j] * (self.config[(i+1)%self.n,j] + self.config[(i-1)%self.n,j] + self.config[i,(j+1)%self.n] + self.config[i,(j-1)%self.n])
        if neighbour_sum <= 0 or np.random.rand() < self.boltzman_factor ** neighbour_sum:
            self.config[i, j] = - self.config[i, j]

    def simulate(self, N_fin: int):
        for i in range(N_fin):
            self.step()

    def plot_config(self):
        plt.matshow(self.config, cmap=self.cmap)
        plt.show()

    def animate(self, N_fin):
        def animate_frame(i): 
            if i == 0:
                self.set_config(np.copy(initial_config)) 
            else: 
                self.step()
            config_plot.set_array(self.config)
            ax.set_title(f't = {i}')

        fig, ax = plt.subplots()
        ax.set_title('t = 0')
        initial_config = np.copy(self.config)
        self.set_config(np.copy(initial_config))
        config_plot = ax.matshow(self.config, cmap=self.cmap)
        anim = mpla.FuncAnimation(fig, func=animate_frame, frames=N_fin, interval=80)
        plt.show()

model = Isisng2D(28, 0.33)
model.initialize_with('blobs')
model.animate(2000)
