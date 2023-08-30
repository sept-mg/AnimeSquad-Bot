import discord, env
from discord.ext import commands

TOKEN = env.token

class BOT(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'Logged in as {self.user} (ID: {self.user.id})')

intents = discord.Intents.all()
bot = BOT(intents=intents)
tree = discord.app_commands.CommandTree(bot)

@tree.command(name='ping', description='Replies with Pong!')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!')

if __name__ == "__main__":
    bot.run(TOKEN)