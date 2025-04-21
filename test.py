import gym
import minerl
import numpy as np

# Importe ton package pour enregistrer l’environnement grâce au __init__.py du package
import minerl_envs

# Crée ton environnement
env = gym.make("TestJump-v0")
env.reset()

done = False
total_reward = 0

while not done:
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    total_reward += reward
    print(f"Step: {env.unwrapped.steps}, Total Reward: {total_reward}")
    env.render()

print(f"Test terminé avec {total_reward} points de récompense.")
env.close()
