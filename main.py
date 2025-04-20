import gym
import minerl
import numpy as np

# Crée l'environnement personnalisé pour les jumps Minecraft
env = gym.make("CustomJump-v0")  # Remplace par ton nom d'environnement si nécessaire
env.reset()

done = False
total_reward = 0

while not done:
    # L'agent choisit une action aléatoire dans l'espace d'action
    action = env.action_space.sample()

    # L'environnement évolue avec cette action
    obs, reward, done, info = env.step(action)

    # On accumule les récompenses pour le suivi
    total_reward += reward

    # Affichage de l'état courant (facultatif)
    print(f"Step: {env.unwrapped.steps}, Total Reward: {total_reward}")

    # Afficher l'environnement (facultatif, désactiver si ça cause des problèmes)
    env.render()

# Fin du test
print(f"Test terminé avec {total_reward} points de récompense.")
env.close()
