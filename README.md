# Projet Apprentissage RL Minecraft Jump

## Description
Dans ce projet de fin de semestre N8EN18B ## Utilisation du Notebook Jupyter

Le notebook principal `Projet_apprentissage.ipynb` contient le code pour entraîner un agent RL qui apprend à réaliser des parcours de jump dans Minecraft.

### Structure du notebook

Le notebook est organisé en plusieurs sections :

1. **Environment Setup & Imports** - Configuration initiale et importation des bibliothèques
2. **Bot Connection Helper** - Fonctions utilitaires pour connecter un bot Mineflayer au serveur
3. **Gym-Style Environment Class** - Implémentation de l'environnement d'apprentissage au format Gym
4. **Observation Utility Functions** - Fonctions pour traiter les observations du monde
5. **Reward & Done Logic** - Logique de récompense et de fin d'épisode
6. **Visualization Helpers** - Outils de visualisation pour déboguer
7. **Wrapping with Stable-Baselines3** - Intégration avec la bibliothèque d'apprentissage
8. **Training Loop** - Boucle d'entraînement du modèle
9. **Training Logs & Plots** - Visualisation des métriques d'apprentissage
10. **Evaluation & Demo Episodes** - Évaluation du modèle entraîné
11. **Hyperparameter Tuning Tips** - Conseils pour optimiser les hyperparamètres

### Exécution du notebook

Pour exécuter le notebook :

1. Assurez-vous que le serveur Minecraft est en cours d'exécution
2. Lancez le notebook avec la commande `jupyter notebook Projet_apprentissage.ipynb`
3. Exécutez les cellules dans l'ordre, de haut en bas
4. Vous pouvez modifier les paramètres du modèle ou de l'environnement selon vos besoins

### Modification du notebook

Pour adapter le notebook à vos besoins :

1. **Personnalisation de l'environnement** : Modifiez la classe `MinecraftRL` pour adapter l'espace d'observation, les récompenses ou les actions disponibles
2. **Ajustement des paramètres d'apprentissage** : Modifiez les hyperparamètres du modèle PPO pour optimiser l'apprentissage
3. **Visualisation** : Adaptez les fonctions de visualisation pour mieux comprendre le comportement de votre agent

### Exemples supplémentaires

Consultez les notebooks dans le dossier `examples_notebooks/` pour des exemples plus spécifiques et des tutoriels.

## Contact
Pour toute question ou problème, ouvrez une issue sur GitHub ou contactez directement un des membres du groupe.

Bonne exploration et bons parkours ! 🚀ntrôle et Apprentissage, nous développons une IA capable de terminer des parcours “Jump” sur Minecraft, en utilisant des algorithmes de renforcement (RL). Un “jump” est un parcours demandant une grande précision de saut et parfois d’autres actions (échelles, mécaniques Minecraft). L’IA perçoit la configuration du monde (type et position des blocs) sans reconnaissance d’image, et apprend par essais et récompenses à atteindre des checkpoints et finir le parcours.

## Membres du groupe
- Corentin COUSTY
- Hermas OBOU
- Ignacio ARROYO
- Wilkens JOSEPH

## Prérequis
- Java 17+
- Python 3.10+
- Node.js 18+
- Jupyter Notebook
- pip & npm

## Installation et setup

1. **Cloner le dépôt**
   ```bash
   git clone <URL_DU_REPO>
   cd <NOM_DU_REPO>
   ```

2. **Configurer l’environnement Python & Node.js**
   ```bash
   # (optionnel) créer et activer un environnement virtuel Python
   python -m venv .venv
   # Linux/macOS
   source .venv/bin/activate
   # Windows
   .venv\Scripts\activate

   # Installer les dépendances Python
   pip install -r requirements.txt

   # Installer les modules Node.js pour Mineflayer
   npm install mineflayer mineflayer-pathfinder
   ```

3. **Lancer le notebook Jupyter**
   ```bash
   jupyter-notebook .\Projet_apprentissage.ipynb
   ```

## Démarrage du serveur Minecraft

### Se placer dans le dossier du serveur
```bash
cd minecraft-server\
```

### Commande de lancement principale (avec interface graphique)
```bash
java -Xms1G -Xmx2G -jar .\paper-1.19.4-550.jar
```

### Lancement sans interface graphique
```bash
java -Xms1G -Xmx2G -jar .\paper-1.19.4-550.jar nogui
```

### Alternative pour détacher le processus sous Linux
```bash
nohup java -Xms1G -Xmx2G -jar ./paper-1.19.4-550.jar nogui &
```


## Ajouter un opérateur (“op”)
```text
op <votre_nom_d_utilisateur>
```

## Structure du dépôt
```
├── .ipynb_checkpoints/         # Checkpoints Jupyter
├── docs/                       # Documentation du projet
│   ├── cea_final_project.pdf
│   ├── Groupe Apprentissage - IA Minecraft.txt
│   └── infos.txt               # Positions de spawn, types de blocs, etc.
├── examples_notebooks/         # Exemples de notebooks
│   └── exemple_notebook_mineflayer.ipynb
├── logs/                       # Fichiers de logs
├── minecraft-server/           # Fichiers du serveur PaperMC
│   ├── paper-1.19.4-550.jar    # Executable du serveur
│   ├── server.properties       # Configuration du serveur
│   ├── plugins/                # Plugins du serveur
│   ├── N7Jumps/                # Monde principal avec parcours de jump
│   ├── N7Jumps_nether/         # Dimension Nether
│   ├── N7Jumps_the_end/        # Dimension The End
│   └── ...
├── Projet_apprentissage.ipynb  # Notebook principal du projet
├── requirements.txt            # Dépendances Python
├── package.json                # Dépendances Node.js
└── README.md                   # Ce fichier
```

## Contact
Pour toute question ou problème, ouvrez une issue sur GitHub ou contactez directement un des membres du groupe.

Bonne exploration et bons parkours ! 🚀
