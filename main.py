import discord, env, guild_settings_manager
from discord import app_commands

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
tree = app_commands.CommandTree(bot)

@bot.event
async def on_member_join(member):
   (channel_id, message) = guild_settings_manager.getGuildWelcome(member.guild.id)
   if (channel_id == None or message == None):
       return
   await bot.get_channel(channel_id).send(message.replace("<@>", "<@"+str(member.id) + ">"))


@tree.command(name='ping', description='Replies with Pong!')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!')

@tree.command(name='setwelcome', description='set the welcome channel, (set <@> in the message to tag the new member)')
@app_commands.checks.has_permissions(administrator=True)
async def setWelcome(interaction: discord.Interaction, channel: discord.TextChannel, message: str):
    if (message == "" or message == " " or message == None):
        message = "Welcome <@>"
    if(channel == None):
        await interaction.response.send_message("you must specify a channel")
        return
    await interaction.response.send_message("welcome channel : <#" + str(channel.id) + ">, info : (set <@> in the message to tag the new member), " +  " message :arrow_right: " + message.replace("<@>", "<@"+str(interaction.user.id) + ">"))
    guild_settings_manager.setGuildWelcome(interaction.guild_id, channel.id, message)

@tree.error
async def on_error(interaction: discord.Interaction, error):
    await interaction.response.send_message(error, ephemeral=True)

if __name__ == "__main__":
    bot.run(TOKEN)