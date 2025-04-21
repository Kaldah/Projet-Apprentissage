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
|--- courses/		# Fichiers de configurations des parcours
├── main.py            # Point d'entrée du projet
├── requirements.txt   # Dépendances
└── README.md          # Présentation


---

## 🚀 Objectif pédagogique

- Maîtriser les bases de l’**apprentissage par renforcement (RL)**.
- Exploiter l’environnement **Minecraft** comme banc d’expérimentation IA.
- Concevoir, entraîner et tester une IA capable de réussir des parcours personnalisés.

---


## Préparer l'environnement conda "minerl"

Penser à utiliser java JDK 8 dans cet environnement.
Vérifier bien avec la commande : java -version

```
conda update -n base -c defaults conda -y
conda init
```
Redémarrer le terminal pour que les modifications soient prises en compte

```
conda create -n minerl python=3.8 -y
```

## ⚙️ Installation rapide
D'après ce tuto :
https://minerl.readthedocs.io/en/latest/tutorials/index.html

### 🔸 Sous Linux/macOS

```
setup.sh
```

### 🔸 Sous Windows
Utiliser les fichiers dans "./Fichiers Setup" pour activer java JDK 8 uniquement dans cet environnement.

```
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