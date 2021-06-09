# discord package
import discord
import random
from discord.ext import commands
import asyncio
import datetime

# client
client = commands.Bot(command_prefix=commands.when_mentioned_or("="))

reaction_title=()
reactions = {}
reaction_message_id = ""

def convert(time):
    pos = ['s', 'm', 'h', 'd']
    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val + time_dict[unit]

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
    Embed.add_field(name="Set Title", value="=reaction_set_title \"New Title\"", inline=False)
    Embed.add_field(name="Add Role", value="=reaction_add_role @role EMOJI_HERE", inline=False)
    Embed.add_field(name="Remove Role", value="=reaction_remove_role @role EMOJI_HERE", inline=False)
    Embed.add_field(name="send creation post", value="=reaction_send", inline=False)
    Embed.add_field(name="Kick a member", value="=kick (@member)", inline=False)
    Embed.add_field(name="Start a giveaway", value="=startgive", inline=False)
    await context.send(embed=Embed)
    

@client.command(name="fun")
async def reaction_help(context):
    
    Embed = discord.Embed(title="list of commands", color=0x7289da)
    Embed.set_author(name="Bill Bot")
    Embed.add_field(name="8ball", value="=8ball \"message\"", inline=False)
    Embed.add_field(name="roast", value="=roast", inline=False)
    await context.send(embed=Embed)
    

@client.command(name="reaction_set_title")
@commands.has_permissions(manage_roles=True)
async def reaction_set_title(context, new_title):

    global reaction_title
    reaction_title = new_title
    await context.send("`title for the message is now " + reaction_title + "!`")
    await context.message.delete()

@client.command(name="reaction_add_role")
@commands.has_permissions(manage_roles=True)
async def reaction_add_role(context, role: discord.Role, reaction):

    if role != None:
        reactions[role.name] = reaction
        await context.send("`Role " + role.name + " has been added with the emoji " + reaction + "!`")
        await context.message.delete()
    
    else:
        await context.send("`please try again!`")

    print(reactions)

@client.command(name="reaction remove role")
@commands.has_permissions(manage_roles=True)
async def reaction_remove_role(context, role: discord.Role):

    if role.name in reactions:
        del reactions[role.name]
        await context.send("`Role " + role.name + " has been deleted!`")
        await context.message.delete()
    else:
        await context.send("`that role was not added!`")
    
    print(reactions)

@client.command(name="reaction_send")
@commands.has_permissions(manage_roles=True)
async def reaction_send(context):

    description = "react to add the roles!\n"

    for role in reactions:
        description+= role + " - " + reactions[role] + "\n"
    
    Embed = discord.Embed(title=reaction_title, description=description, color=0x8cc542)
    Embed.set_author(name="Reaction roles")

    message = await context.send(embed=Embed)

    global reaction_message_id
    reaction_message_id = str(message.id)

    for role in reactions:
        await message.add_reaction(reactions[role]) 

    await context.message.delete()

@client.command(name="ping")
async def ping(context):
    Embed = discord.Embed(title="Pong!", description=f"{round(client.latency * 1000)} ms", color=0x8cc542)

    await context.send(embed=Embed)

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

@client.command(name="startgive")
@commands.has_permissions(ban_members=True)
async def startgive(context):
    await context.send("Ok! Let's start this giveaway! Answer the following question in 15 seconds.")

    questions = ["Where should the Giveaway be hosted? (channel)", 
                 "How much time should the giveaway last? (s|m|h|d)",
                 "What are you giving away? (prize)"]
    answers = []

    def check(m):
        return m.author == context.author and m.channel == context.channel
    for i in questions:
        await context.send(i)

        try:
            msg = await client.wait_for("message", timeout=15.0, check=check)
        
        except asyncio.TimeoutError:
            await context.send("You didn\'t answer in time! Please be quicker next time. ")
            return
        else:
            answers.append(msg.content)
    try:
        c_id = int(answers[0][2:-1])
    except:
        await context.send(f"You didn't mention a channel properly. Do it like this {context.channel.mention} next time.")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await context.send(f"You  didn't answer with a proper unit. Use these (s|m|h|d)")
        return
    elif time == -2:
        await context.send(f"The time must be an integer. please enter an integer next time.")
        return

    prize = answers[2]

    await context.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")
    Embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = 0xffffff)

    end = datetime.datetime.utcnow() + datetime.timedelta()

    Embed.add_field(name = "Ends At:", value = f"{end} GMT")
    Embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await context.send(embed = Embed)
    await my_msg.add_reaction("🎉")
    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)
    

    await context.send("GG! " f"{winner.mention}" " won " f"{prize}!")

    @client.command(name=pp)
    async def pp(self, user : discord.Member):
        #"""Detects user's penis length
        #This is 100% accurate."""
        random.seed(user.id)
        p = "8" + "="*random.randint(0, 30) + "D"
        await context.send("Size: " + p)


# events

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("You can type `=help` for more info")
    await client.process_commands(message)

@client.event
async def on_message(message):

    if message.content == "hi":
        await message.channel.send("hi!")
    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):

    if not user.bot:

        message = reaction.message
        if str(message.id) == reaction_message_id:
            
            # add roles to members

            role_to_give = ""

            for role in reactions:
                if reactions[role] == reaction.emoji:
                    role_to_give = role
            role_for_reaction = discord.utils.get(user.guild.roles, name=role_to_give)
            await user.add_roles(role_for_reaction)

@client.event
async def on_ready():
    print("Bot is online!")
    user = await client.fetch_user(537714749492690975)
    await user.send('yo I am back')

    guild_count = 0
    for guild in client.guilds:

	    print(f"- {guild.id} (name: {guild.name})")
	    guild_count = guild_count + 1
	    print(f"Bill is in {guild_count} guilds.")

    activity = discord.Activity(name = f'over {guild_count} servers!', type=discord.ActivityType.watching)
    await client.change_presence(activity = activity, status = discord.Status.do_not_disturb)

# run the client on the s erver
client.run("NzYwNDgwMDU2NzkwNDgyOTQ0.X3MqPg.g1mJdz1gXpV_OzEKTOVySso-fRQ")