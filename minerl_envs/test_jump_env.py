import gym
from gym import spaces
import numpy as np

class CustomJumpEnv(gym.Env):
    def __init__(self):
        super(CustomJumpEnv, self).__init__()
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        self.action_space = spaces.Discrete(2)
        self.steps = 0

    def reset(self):
        self.steps = 0
        self.state = np.random.rand(4).astype(np.float32)
        return self.state

    def step(self, action):
        self.steps += 1
        reward = 1.0 if action == 1 else 0.0
        done = self.steps >= 10  # Exemple de fin
        self.state = np.random.rand(4).astype(np.float32)
        return self.state, reward, done, {}

    def render(self, mode='human'):
        print(f"State: {self.state}")
