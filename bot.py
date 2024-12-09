import discord
from discord.ext import commands
import os
from config import TOKEN

# Initialisation du bot
intents = discord.Intents.default()
intents.message_content = True


class MusicBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Charger tous les cogs dans le dossier "cogs"
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")  # Charger chaque cog
        # Synchroniser les commandes slash avec Discord
        await self.tree.sync()
        print("Commandes slash synchronisées.")
        print("Cogs chargés avec succès.")


# Instancier le bot
bot = MusicBot()


# Événement : le bot est prêt
@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")


# Démarrer le bot
bot.run(TOKEN)
