import numpy as np

class MarkonChain:
    def __init__(self, n_states: int, initial_prob: np.ndarray, transition: np.ndarray):
        try:
            np.random.choice(n_states, p=initial_prob)
        except ValueError:
            print('Initial probability does not sum to 1!')
        try:
            for i in range(n_states):
                np.random.choice(n_states, p=transition[i, :])
        except ValueError:
            print(f'Row {i} does not sum to 1!')

        self.n_states = n_states
        self.initial_prob = initial_prob
        self.transition = transition

    def simulate(self, N_fin: int):
        simulated_states = np.repeat(-1, N_fin)
        simulated_states[0] = np.random.choice(self.n_states, p=self.initial_prob)
        for i in range(1, N_fin):
            prev_state = simulated_states[i - 1]
            simulated_states[i] = np.random.choice(self.n_states, p=self.transition[prev_state, :])
        return simulated_states
    
    def eig(self):
        eigvals, eigvecs = np.linalg.eig(self.transition.T)
        return eigvals, eigvecs
    
    def simulateDistribution(self, n_samples, N_fin):
        dist_mat = np.zeros((self.n_states, N_fin))
        for i in range(n_samples):
            states = self.simulate(N_fin)
            for j, state in enumerate(states):
                dist_mat[state, j] += 1
        return dist_mat / np.sum(dist_mat, axis=0, keepdims=True) 