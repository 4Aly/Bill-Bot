# discord package
import discord
import random
from discord.ext import commands
import asyncio
import datetime
import os

# client
client = commands.Bot(command_prefix=commands.when_mentioned_or("="))

# Events

@client.event
async def on_ready():
    print("Bot is online!")
    user = await client.fetch_user(537714749492690975)
    await user.send('yo I am back')


#load/unload cogs
@client.command()
@commands.is_owner()
async def load(context, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(context, extension):
    client.unload_extension(f'cogs.{extension}')


#Help command

client.remove_command('help')

@client.command(name="help")
async def help(context):
    
    Embed = discord.Embed(title="list of commands", color=0x7289da)
    Embed.set_author(name="Bill Bot")
    Embed.add_field(name="Fun", value="`=fun`", inline=False)
    Embed.add_field(name="Admin Commands", value="`=admin`", inline=False)
    
    await context.send(embed=Embed)


@client.command(name="admin")
async def reaction_help(context):
    
    Embed = discord.Embed(title="list of commands", color=0x7289da)
    Embed.set_author(name="Bill Bot")
    Embed.add_field(name="Kick a member", value="=kick (@member)", inline=False)
    Embed.add_field(name="Start a giveaway", value="=startgive", inline=False)
    await context.send(embed=Embed)
    

@client.command(name="fun")
async def reaction_help(context):
    
    Embed = discord.Embed(title="list of commands", color=0x7289da)
    Embed.set_author(name="Bill Bot")
    Embed.add_field(name="Say something as Bill", value="=say \"message\"", inline=False)
    Embed.add_field(name="8ball", value="=8ball \"message\"", inline=False)
    Embed.add_field(name="roast", value="=roast", inline=False)
    Embed.add_field(name="pp size machine", value="=pp", inline=False)
    await context.send(embed=Embed)

# ping command

@client.command(name="ping")
async def ping(context):
    Embed = discord.Embed(title="Pong!", description=f"{round(client.latency * 1000)} ms", color=0x8cc542)

    await context.send(embed=Embed)

# random shit

@client.command(name="8ball")
async def _8ball(context, *, question):
    responses = ["mhm",
                 "Yes.",
                 "of course",
                 "definitely",
                 "I say yes",
                 "most likely",
                 "I am too tired now, ask again later"
                 "It is certain."
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes – definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "No.",
                 "Very doubtful."]

    await context.send(embed = discord.Embed(title = "8ball", description = f'{random.choice(responses)}', color=0x8cc542))

@client.command(name="invite")
async def invite(context):
    Embed = discord.Embed(title="Invite Bill to your own discord server!", description="https://discord.com/api/oauth2/authorize?client_id=760480056790482944&permissions=8&scope=bot", color=0x8cc542)

    await context.send(embed=Embed)

@client.command(name="roast")
async def roast(context):
    roasts = ["You're as useless as the \"ueue\" in \"queue\".",
             "Mirrors can't talk. Lucky for you, they can't laugh either.",
             "If I had a face like yours I'd sue my parents.",
             "You must've been born on a highway, cuz that's where most accidents happen.",
             "If laughter is the best medecine, your face must be curing the world.",
             "When you were born the doctor threw you out of the window and the window threw you back.",
             "Your face makes onions cry.",
             "You are more disappointing than an unsalted pretzel.",
             "You are like a cloud. When you disappear it’s a beautiful day.",
             "I don't think you need roasting, your life is miserable enough."]

    await context.send(embed = discord.Embed(title = "get roasted, lol", description = f'{random.choice(roasts)}', color=0x8cc542))

@client.command(name="say")
async def say(context, *, text):
    message = context.message
    await message.delete()

    await context.send(embed = discord.Embed(description = f'{text}', color=0x8cc542))

@client.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):
    await member.kick()
    await context.send(embed = discord.Embed(description = 'User ' + member.display_name + ' has been kicked!', color=0xb22222))
    
# run the client on the server
client.run("Token")
