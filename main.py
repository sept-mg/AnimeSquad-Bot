import discord, json, requests
from discord import app_commands
from env import Env

env = Env()

TOKEN = env.var['TOKEN']

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
   channel_id, message = int(env.var["WELCOME_CHANNEL_ID"]), env.var["WELCOME_MESSAGE"]
   await bot.get_channel(channel_id).send(message.replace("<@>", "<@"+str(member.id) + ">"))


@tree.command(name='ping', description='Replies with Pong!')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!')

@tree.command(name='setwelcome', description='set the welcome channel, (set <@> in the message to tag the new member)')
@app_commands.checks.has_permissions(administrator=True)
async def setWelcome(interaction: discord.Interaction, channel: discord.TextChannel, message: str):
    if (message == "" or message == " " or message == None):
        message = "Welcome <@>"
    await interaction.response.send_message("welcome channel : <#" + str(channel.id) + ">, info : (set <@> in the message to tag the new member), " +  " message :arrow_right: " + message.replace("<@>", "<@"+str(interaction.user.id) + ">"))
    env.set_env({"WELCOME_CHANNEL_ID" : channel.id, "WELCOME_MESSAGE" : message})

# @tree.command(name='setannonce', description='set annonce channel')
# @app_commands.checks.has_permissions(administrator=True)
# async def setting(interaction: discord.Interaction, channel: discord.TextChannel):
#     await interaction.response.send_message("annonce channel : <#" + str(channel.id) + ">")
#     env.set_env({"ANNONCE_CHANNEL_ID" : channel.id})

# @tree.command(name='annonce', description='dispatch an annonce')
# async def annonce(interaction: discord.Interaction, annonce: str):
#     annonce_channel = bot.get_channel(int(env.var["ANNONCE_CHANNEL_ID"]))
#     if annonce_channel.permissions_for(interaction.user).send_messages:
        
#         await annonce_channel.send(annonce)


    
#         await interaction.response.send_message("Annonce envoyée")
    
#     else:
#         await interaction.response.send_message("You don't have permission to send messages in this channel")


@tree.command(name='anime', description='donne un anime aléatoire')
async def anime(interaction: discord.Interaction):
    resp = requests.get(env.var["ANIME_API_URL"])
    await interaction.response.send_message(resp.json())

@tree.error
async def on_error(interaction: discord.Interaction, error):
    await interaction.response.send_message(error, ephemeral=True)

if __name__ == "__main__":
    bot.run(TOKEN)