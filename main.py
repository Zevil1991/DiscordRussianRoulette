import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

chosen = 0
current = 0
group = []

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")

@bot.command()
async def ins(ctx):
    await ctx.message.channel.send("Welcome to Zevil's Russian Roulette Game")
    time.sleep(3)
    await ctx.message.channel.send("In this game, you are tasked with shuffling your cartridge and taking turns shooting")
    time.sleep(3)
    await ctx.message.channel.send("Whoever's the unlucky one will get kicked out of the server. Last one alive wins~")
    time.sleep(3)
    await ctx.message.channel.send("To start, type $join to enter into the game and then $order to figure out the order of who gets to play")
    time.sleep(3)
    await ctx.message.channel.send("After that, the one whose turn it is to play has to shuffle the numbers, then each person will take turns shooting using $shoot")
    time.sleep(3)
    await ctx.message.channel.send("Enjoy~")

@bot.command()
async def join(ctx):
    global group
    if (ctx.message.author.name in group):
        await ctx.message.channel.send("You're already in the game")
    else:
        group.append(ctx.message.author.name)
        print(group)
        await ctx.message.channel.send(f"{ctx.message.author.name} has joined!")

@bot.command()
async def ng(ctx):
    global group
    group = []
    await ctx.message.channel.send("The game has been reset. Please invite the memebers that have died")

@bot.command()
async def order(ctx):
    global group
    random.shuffle(group)
    size = len(group)
    x = " > ".join(group)
    await ctx.message.channel.send(f"The order of the group is as follows: {x}")

@bot.command()
async def shuffle(ctx):
    global chosen
    global current
    current = 0
    chosen = random.randint(1,10)
    await ctx.message.channel.send("Cartridge has been shuffled")

@bot.command()
async def shoot(ctx):
    global chosen, current
    current+=1
    if(current == chosen):
        await ctx.message.author.kick(reason="Died")
        await ctx.message.channel.send(f"{ctx.message.author.name} has been killed")
        await ctx.message.channel.send("Please use $shuffle to start once more")
    elif(current > chosen):
        await ctx.message.channel.send("I can't shoot without reloading the cartridge.")
    else:
        await ctx.message.channel.send("You're safe, for now.")

@bot.command
def kill(ctx):
    exit()

bot.run("ENTER BOT TOKEN HERE")
