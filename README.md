# 🎮 Projet Apprentissage — IA Jump Minecraft

Ce projet a pour objectif de concevoir une **intelligence artificielle** capable de réussir des parcours de type *jump* dans **Minecraft**, en utilisant l'apprentissage par renforcement (*Reinforcement Learning*).

---

## 📁 Arborescence du projet

Projet-Apprentissage/
│
├── notebooks/         # Tests et exploration
├── maps/              # Maps Minecraft customisées
├── minerl_envs/       # Scripts pour customiser les environnements MineRL
├── agent/             # Code IA (entraîneur, modèles)
├── main.py            # Point d'entrée du projet
├── requirements.txt   # Dépendances
└── README.md          # Présentation


---

## 🚀 Objectif pédagogique

- Maîtriser les bases de l’**apprentissage par renforcement (RL)**.
- Exploiter l’environnement **Minecraft** comme banc d’expérimentation IA.
- Concevoir, entraîner et tester une IA capable de réussir des parcours personnalisés.

---

## ⚙️ Installation rapide

### 🔸 Sous Linux/macOS

```
setup.sh
```

### 🔸 Sous Windows
Lancer depuis WSL ou Git Bash
```
WSL doit posséder java 8 sinon :
sudo apt update
sudo apt install openjdk-8-jdk

setup.bat

```



🧠 Technologies utilisées

    🐍 Python 3.8

    🎮 MineRL

    🧪 OpenAI Gym

    🤖 Stable-Baselines3

🗺️ Personnalisation des parcours

Les parcours personnalisés doivent être :

    créés sous Minecraft 1.12.2

    ajoutés dans le dossier maps/

    déclarés dans un environnement personnalisé dans minerl_envs/


👥 Équipe projet

	Corentin COUSTY

	Hermas OBOU

	Ignacio ARROYO
	
	Le Multi-Scaled