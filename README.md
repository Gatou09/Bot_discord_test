# Discord Test Bot

Ce projet est un **bot Discord** conçu pour tester et développer diverses fonctionnalités de Discord. 

Il permet de créer, expérimenter et intégrer de nouvelles commandes, modules et fonctionnalités au sein d'un serveur Discord.

## Fonctionnalités

- ⚙️ **Modularité** : Ajout de commandes personnalisées via des cogs.
- 🎵 **Musique** : Lecture de musique à partir de sources externes (YouTube, etc.).
- 🛠️ **Développement** : Test de nouvelles fonctionnalités Discord (slash commands, réactions, etc.).
- 🔧 **Personnalisation** : Configuration flexible pour expérimenter divers scénarios.
- 📊 **Logs** : Affichage de logs pour déboguer ou suivre l'activité du bot.

## Installation

### 1. Pré-requis
Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 3.8 ou plus
- Une clé API Discord (token du bot)
- `pip` (gestionnaire de paquets Python)

### 2. Cloner le dépôt
Clonez ce projet dans un répertoire local :
```bash
git clone https://github.com/Gatou09/Bot_discord_test.git
cd discord-test-bot
```

### 3. Créer un environnement virtuel
Créez un environnement virtuel pour isoler les dépendances du projet :
````bash
python -m venv .venv
source .venv/bin/activate  # Sous Linux/Mac
.venv\Scripts\activate     # Sous Windows
````

### 4. Installer les dépendances
Installez les dépendances nécessaires listées dans requirements.txt :
````bash
pip install -r requirements.txt
````

### 5. Ajouter votre token Discord
Créez un fichier .env à la racine du projet et ajoutez votre token Discord :
````dotenv
DISCORD_TOKEN=votre_token_discord
````

### 6. Lancer le bot
Démarrez le bot avec la commande suivante :
````bash
python bot.py
````
Vous devriez voir un message dans la console indiquant que le bot est connecté.

### Structure du projet

````bash
Bot_discord_test/
│
├── bot.py              # Script principal du bot
├── config.py           # Configuration générale du bot
├── cogs/               # Dossier contenant les cogs (modules)
│   ├── general.py      # Exemple de commandes générales
│   └── music.py        # Exemple de commandes musicales
│
├── utils/              # Dossier contenant les utilitaires
├── .env                # Fichier contenant le token Discord (à ne pas partager)
├── requirements.txt    # Liste des dépendances Python
└── README.md           # Documentation du projet

````
