import os

# Récupère le token depuis les variables d'environnement
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Le token du bot n'a pas été configuré dans les variables d'environnement.")
