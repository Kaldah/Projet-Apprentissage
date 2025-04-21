import sys
from utils.course_loader import load_course_config
import minerl
import gym

import minerl_envs


# Récupération de l'ID du parcours
course_id = sys.argv[1] if len(sys.argv) > 1 else "1"
config = load_course_config(course_id)

# Exemple d'utilisation dans la logique
print(f"Loaded course {course_id} config:", config)

# Passer config à l'environnement
# On force l'environnement à utiliser la map copiée dans 'maps/JumpsIA'
config["minecraft_map_path"] = "maps/JumpsAI"

env = gym.make("JumpAI-v0", config=config)
env.reset()

# Logique classique
done = False
total_reward = 0
while not done:
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    total_reward += reward
    env.render()

print(f"Test terminé avec {total_reward} points de récompense.")
env.close()
