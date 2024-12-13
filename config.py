import os
from dotenv import load_dotenv

load_dotenv()
# Récupère le token depuis les variables d'environnement
TOKEN = os.getenv("discord_token")

if not TOKEN:
    raise ValueError("Le token du bot n'a pas été configuré dans les variables d'environnement.")
