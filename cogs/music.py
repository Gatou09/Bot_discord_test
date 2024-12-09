import discord
from discord.ext import commands
from utils.ytdl import YTDLSource
import asyncio


class MusicControls(discord.ui.View):
    def __init__(self, interaction, cog):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.cog = cog

    @discord.ui.button(label="⏸ Pause", style=discord.ButtonStyle.primary)
    async def pause(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_playing():
            interaction.guild.voice_client.pause()
            await interaction.response.send_message("Musique mise en pause.", ephemeral=True)

    @discord.ui.button(label="▶️ Reprendre", style=discord.ButtonStyle.success)
    async def resume(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_paused():
            interaction.guild.voice_client.resume()
            await interaction.response.send_message("Musique reprise.", ephemeral=True)

    @discord.ui.button(label="⏹ Skip", style=discord.ButtonStyle.danger)
    async def stop(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_playing():
            interaction.guild.voice_client.stop()
            await interaction.response.send_message("Musique arrêtée.", ephemeral=True)
        self.cog.music_queue.clear()


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.music_queue = []  # File d'attente

    @discord.app_commands.command(name="join", description="Faire rejoindre le bot dans un canal vocal")
    async def join(self, interaction: discord.Interaction):
        if not interaction.user.voice:
            await interaction.response.send_message("Vous devez être dans un canal vocal pour utiliser cette commande.", ephemeral=True)
            return

        channel = interaction.user.voice.channel
        if interaction.guild.voice_client is not None:
            await interaction.guild.voice_client.move_to(channel)
        else:
            await channel.connect()

        await interaction.response.send_message(f"Connecté au canal vocal : {channel.name}")

    @discord.app_commands.command(name="play", description="Jouer une musique à partir d'une URL")
    async def play(self, interaction: discord.Interaction, url: str):
        if not interaction.guild.voice_client:
            await interaction.response.send_message("Le bot doit être dans un canal vocal pour jouer de la musique. Utilisez la commande /join.", ephemeral=True)
            return

        self.music_queue.append(url)
        await interaction.response.send_message(f"Ajouté à la file d'attente : {url}")

        if not interaction.guild.voice_client.is_playing():
            await self.play_next(interaction)

    async def play_next(self, interaction: discord.Interaction):
        if self.music_queue:
            next_url = self.music_queue.pop(0)
            player = await YTDLSource.from_url(next_url, loop=self.bot.loop)
            interaction.guild.voice_client.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(interaction), self.bot.loop))

            # Créer un embed avec les informations de la musique
            embed = discord.Embed(
                title="🎶 Musique en cours",
                description=f"Lecture de : [{player.title}]({player.url})",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url="https://i.imgur.com/example.jpg")  # URL de la miniature (facultatif)
            embed.add_field(name="File d'attente", value=f"{len(self.music_queue)} musique(s) restante(s)", inline=False)

            # Ajouter les boutons interactifs
            view = MusicControls(interaction, self)
            await interaction.channel.send(embed=embed, view=view)

        else:
            await interaction.followup.send("La file d'attente est vide. Déconnexion.")
            await interaction.guild.voice_client.disconnect()


async def setup(bot):
    await bot.add_cog(Music(bot))
