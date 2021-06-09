import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or("="))

# events

@commands.Cog.listener()
async def on_ready(self):
    print(f"Cog has been loaded")

# make cogs work


class admin(commands.Cog):
    def __init__(self, client):
        self.client = client


# commands
            
    @client.command(name="invite")
    async def invite(self, context):
        Embed = discord.Embed(title="Invite Bill to your own discord server!", description="https://discord.com/api/oauth2/authorize?client_id=760480056790482944&permissions=8&scope=bot", color=0x8cc542)

        await context.send(embed=Embed)

# idk but it is nessecary

def setup(client):
    client.add_cog(admin(client))


