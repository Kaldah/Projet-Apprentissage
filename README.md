
# 🎮 Projet Apprentissage — IA Jump Minecraft

Ce projet a pour objectif de concevoir une **intelligence artificielle** capable de réussir des parcours de type *jump* dans **Minecraft**, en utilisant l'apprentissage par renforcement (*Reinforcement Learning*).

---

## 📁 Arborescence du projet

```
Projet-Apprentissage/
│
├── agent/              # Code IA (entraîneur, modèles)
├── courses/            # Configs des parcours (.json)
├── docs/               # Documentation technique
├── maps/               # Maps Minecraft customisées
│   └── JumpsAI/        # Exemple de monde Minecraft 1.12.2
├── minerl_envs/        # Environnements personnalisés MineRL
├── notebooks/          # Analyses et tests
├── utils/              # Scripts utilitaires (setup, import/export maps...)
│   └── Fichiers Setup/ # Activation Java JDK 8 (Windows)
├── main.py             # Point d’entrée du projet
├── requirements.txt    # Dépendances Python
└── README.md           # Présentation du projet
```

---

## 🚀 Objectifs pédagogiques

- Maîtriser les bases de l’**apprentissage par renforcement (RL)**.
- Exploiter **Minecraft** comme banc d’expérimentation IA.
- Concevoir, entraîner et tester une IA sur des parcours personnalisés.

---

## ⚙️ Préparation de l’environnement (conda)

Penser à utiliser Java JDK 8 dans l’environnement `minerl`.

```bash
conda create -n minerl python=3.8 -y
conda activate minerl
```

Sous Windows, utiliser les scripts de `utils/Fichiers Setup` pour activer Java JDK 8 à l’entrée/sortie de l’environnement.

---

## 🔁 Ajout d’un parcours personnalisé

1. Créez un monde Minecraft avec **Minecraft 1.12.2**.
2. Copiez-le dans `maps/` (ex: `maps/NomDuParcours/`).
3. Créez un fichier de config JSON dans `courses/`, avec les infos suivantes :
```json
{
  "start_pos": [x, y, z],
  "goal_block": [x, y, z],
  "death_y_level": y_min,
  "reward_goal": 100,
  "reward_step": -1,
  "reward_fail": -100
}
```
4. Le monde est ensuite utilisé via un environnement MineRL personnalisé dans `minerl_envs/`.

---

## 📤 Scripts utilitaires

Le dossier `utils/` contient :
- `course_loader.py` : charge dynamiquement les configs JSON de parcours.
- `import_map.py` / `export_map.py` *(à venir)* : scripts pour automatiser l’import/export de maps Minecraft.
- `Fichiers Setup/` : pour configurer l’environnement Java sur Windows (activation automatique du JDK 8).

---

## 🧠 Technologies utilisées

- 🐍 Python 3.8
- 🎮 MineRL
- 🤖 Stable-Baselines3
- 🧪 OpenAI Gym

---

## 👥 Équipe projet

- Corentin COUSTY  
- Hermas OBOU  
- Ignacio ARROYO  
- Le Multi-Scaled
