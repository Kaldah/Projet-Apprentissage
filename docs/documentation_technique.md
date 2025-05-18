# Documentation Technique - Agent Jump Minecraft

## Architecture du système

L'architecture du système est composée de plusieurs éléments clés:

1. **L'environnement JumpAI** (jumpai_env.py)
2. **Le système d'entraînement** (train_agent.py)
3. **Le système d'évaluation** (eval_agent.py)
4. **Le système d'exécution** (run_agent.py)

## JumpAI Environment

### Principes généraux

L'environnement JumpAI est une implémentation personnalisée d'un environnement Gym qui s'interface avec Minecraft via MineRL. Il simule un parcours de type "jump" avec les caractéristiques suivantes:

- Bloc de départ (or) : Position initiale du joueur
- Blocs du parcours (fer) : Les plateformes sur lesquelles l'agent doit sauter
- Bloc d'arrivée (diamant) : L'objectif à atteindre
- Zone de chute : Si l'agent tombe en dessous d'une certaine hauteur, il échoue

### Espace d'observation

L'espace d'observation est un vecteur qui contient:

1. **Position de l'agent** (3 valeurs) : Coordonnées x, y, z
2. **Vitesse de l'agent** (3 valeurs) : Vecteur de vitesse
3. **Blocs environnants** (27 valeurs) : Cube 3×3×3 autour de l'agent avec les IDs des blocs

Cela donne à l'agent les informations nécessaires pour comprendre sa position par rapport au parcours et aux blocs proches.

### Espace d'action

L'espace d'action est discret avec 7 actions possibles:

| ID | Action |
|----|--------|
| 0 | Ne rien faire |
| 1 | Avancer |
| 2 | Avancer + Sauter |
| 3 | Sauter |
| 4 | Avancer + Courir + Sauter |
| 5 | Se tourner à gauche |
| 6 | Se tourner à droite |

### Système de récompenses

Le système de récompenses est conçu pour guider l'agent vers l'objectif:

- **Récompense d'objectif** (+100 par défaut) : Attribuée lorsque l'agent atteint le bloc d'arrivée
- **Récompense par étape** (-1 par défaut) : Petite pénalité à chaque étape pour encourager l'efficacité
- **Pénalité de chute** (-100 par défaut) : Grande pénalité si l'agent tombe sous le niveau défini
- **Récompense de proximité** : Bonus proportionnel à la réduction de la distance par rapport à l'objectif

## Système d'entraînement

### Algorithmes supportés

Le système d'entraînement utilise Stable-Baselines3 et supporte trois algorithmes principaux:

1. **PPO (Proximal Policy Optimization)**
   - Avantages: Stable, performant, bon compromis exploration/exploitation
   - Hyperparamètres clés: learning_rate, n_steps, batch_size, n_epochs, clip_range
   
2. **A2C (Advantage Actor Critic)**
   - Avantages: Rapide, moins gourmand en ressources
   - Hyperparamètres clés: learning_rate, n_steps, gamma
   
3. **DQN (Deep Q-Network)**
   - Avantages: Efficace pour les espaces d'actions discrets
   - Hyperparamètres clés: learning_rate, buffer_size, learning_starts, exploration_fraction

### Vectorisation des environnements

Pour accélérer l'entraînement, le système peut exécuter plusieurs environnements en parallèle avec:
- **SubprocVecEnv**: Environnements exécutés dans des processus séparés
- **DummyVecEnv**: Environnement unique pour les tests ou machines limitées

### Callbacks utilisés

Plusieurs callbacks sont implémentés pour suivre et sauvegarder l'entraînement:

- **CheckpointCallback**: Sauvegarde périodique du modèle
- **EvalCallback**: Évaluation périodique du modèle et sauvegarde du meilleur modèle

## Évaluation et Exécution de l'agent

### Métriques d'évaluation

L'évaluation de l'agent utilise plusieurs métriques:

- **Taux de réussite**: Pourcentage d'épisodes où l'agent atteint l'objectif
- **Récompense moyenne**: Moyenne des récompenses cumulées par épisode
- **Nombre d'étapes moyen**: Moyenne du nombre d'étapes par épisode

### Mode déterministe vs stochastique

L'évaluation peut être effectuée en mode:
- **Déterministe**: L'agent choisit toujours l'action la plus probable
- **Stochastique**: L'agent échantillonne les actions selon leur distribution de probabilité (utile pour tester la robustesse)

## Configuration des parcours

Les parcours sont configurés via des fichiers JSON qui contiennent:

```json
{
  "start_pos": [x, y, z],         // Position de départ
  "goal_block": [x, y, z],        // Position d'arrivée
  "death_y_level": y_min,         // Niveau Y minimum (chute)
  "reward_goal": 100,             // Récompense d'objectif
  "reward_step": -1,              // Récompense par étape
  "reward_fail": -100,            // Pénalité de chute
  "max_steps": 500,               // Nombre maximum d'étapes
  "distance_reward_factor": 0.1   // Facteur de récompense de proximité
}
```

## Intégration avec MineRL

Dans l'implémentation actuelle, l'interface avec Minecraft via MineRL est simulée. Pour une intégration complète, il faudrait:

1. Utiliser les méthodes MineRL pour observer l'environnement Minecraft
2. Convertir les observations en vecteurs compatibles avec l'agent
3. Traduire les actions de l'agent en commandes Minecraft
4. Récupérer les retours de Minecraft (position, état des blocs, etc.)

## Améliorations futures

Plusieurs améliorations pourraient être apportées:

1. **Intégration complète avec MineRL/Malmo** pour l'interaction avec Minecraft
2. **Observation visuelle** (utiliser des images de l'environnement comme entrée)
3. **Curriculum learning** (progression de difficulté des parcours)
4. **Apprentissage par imitation** (démonstrations humaines au début)
5. **Optimisation des hyperparamètres** via recherche par grille ou algorithmes génétiques
