# Documentation Technique — Projet IA Jump Minecraft

## 1. Vue d'ensemble

Ce projet utilise la plateforme **MineRL** pour entraîner une intelligence artificielle à réussir des parcours *jump* dans Minecraft. L’environnement est basé sur **OpenAI Gym**, et s’appuie sur des maps personnalisées.

## 2. Fonctionnement de MineRL

### a. MineRL et Malmo

MineRL est construit sur la plateforme **Malmo** (Microsoft), qui permet d’interfacer Minecraft avec des agents IA. Il offre des environnements compatibles OpenAI Gym.

### b. Structure d’un environnement

Un environnement MineRL repose sur :

- un fichier de **mission XML** (définition du monde, objectifs, observations...)
- un environnement Gym personnalisé (classe Python dérivée de `gym.Env`)
- une map Minecraft spécifique (placée dans `maps/`)

## 3. Ajouter un nouveau parcours

### a. Créer la map Minecraft

1. Ouvrir Minecraft 1.12.2.
2. Créer votre parcours dans un monde solo.
3. Sauvegarder le monde et le récupérer dans le dossier `maps/` sous un nouveau nom (`maps/NomDuParcours`).

### b. Ajouter le fichier de configuration JSON

Placer un fichier `.json` dans `courses/`, exemple :

```json
{
  "start_pos": [100, 65, 200],
  "goal_block": [120, 65, 200],
  "death_y_level": 60,
  "reward_goal": 100,
  "reward_step": -1,
  "reward_fail": -100
}
```

### c. Enregistrer un nouvel environnement

Dans `minerl_envs/`, créer un script (ou modifier `test_jump_env.py`) pour :

- charger la map depuis `maps/`
- charger le fichier de configuration
- enregistrer un environnement Gym (`gym.register(...)`)

## 4. Scripts et utilitaires

### a. `utils/course_loader.py`

Permet de charger dynamiquement les configurations de parcours (`courses/*.json`).

### b. `utils/Fichiers Setup`

Contient les scripts pour activer automatiquement Java 8 (nécessaire pour MineRL) uniquement dans l’environnement `conda minerl`.

### c. Scripts à venir

Des scripts pour **exporter** et **importer** des maps Minecraft seront ajoutés dans `utils/`. Ils faciliteront le backup, la duplication ou le déploiement.

## 5. Bonnes pratiques

- Toujours tester les maps manuellement dans Minecraft avant d'entraîner l'IA.
- Vérifier que les coordonnées de départ/arrivée sont cohérentes.
- Utiliser un niveau Y bas pour `death_y_level` ou de la lave afin de détecter les chutes.
- Utiliser des blocs différents pour marquer les étapes passées et pouvoir donner des récompenses selon le bloc atteint sans avoir à préciser toutes les coordonnées.

## 6. À venir

- Intégration Stable-Baselines3
- Ajout d’un visualiseur des trajectoires
- Benchmark multi-courses

---

**Équipe projet :** Corentin Cousty, Hermas Obou, Ignacio Arroyo, Wilkens Joseph

