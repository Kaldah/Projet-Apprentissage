import gym
import numpy as np
from gym import spaces

class JumpAIEnv(gym.Env):
    def __init__(self, config):
        super().__init__()

        # Configuration du parcours
        self.start_pos = config.get("start_pos", [0, 0, 0])
        self.goal_block = config.get("goal_block", [0, 0, 0])
        self.death_y_level = config.get("death_y_level", 0)
        self.reward_goal = config.get("reward_goal", 100)
        self.reward_step = config.get("reward_step", -1)
        self.reward_fail = config.get("reward_fail", -100)

        # Espace d'observation et d'action
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(3,), dtype=np.float32)  # Exemple de box 3D pour position
        self.action_space = spaces.Discrete(6)  # Exemple d'espace d'action (déplacement 6 directions)

        self.reset_agent_position()

    def reset_agent_position(self):
        self.agent_position = np.array(self.start_pos)

    def reset(self):
        self.reset_agent_position()
        return self.agent_position

    def step(self, action):
        if action == 0:  # Avancer
            self.agent_position[0] += 1
        elif action == 1:  # Reculer
            self.agent_position[0] -= 1
        elif action == 2:  # Monter
            self.agent_position[1] += 1
        elif action == 3:  # Descendre
            self.agent_position[1] -= 1
        elif action == 4:  # Aller à droite
            self.agent_position[2] += 1
        elif action == 5:  # Aller à gauche
            self.agent_position[2] -= 1

        x, y, z = self.agent_position

        if y < self.death_y_level:
            return self.agent_position, self.reward_fail, True, {}

        if list(self.agent_position) == self.goal_block:
            return self.agent_position, self.reward_goal, True, {}

        return self.agent_position, self.reward_step, False, {}

    def render(self, mode='human'):
        # Affichage basique de la position de l'agent dans la console
        print(f"Position actuelle de l'agent: {self.agent_position}")
