import os
import random

import discord
from discord import client
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from dotenv import load_dotenv

DISCORD_TOKEN = 'MTA0NDgyMjk5OTYxMTc1MjQ1OA.GmDbGm.RC7czVPuqdVB1Z7XJrBZ2jq3N4vmWmExBJTwd0'

load_dotenv()
TOKEN = os.getenv(DISCORD_TOKEN)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents= intents)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name= 'percent', help = 'Gives Percent')
async def percent(ctx):
    response_p = str(random.randrange(1, 100))
    await ctx.send(response_p + '%')

@bot.command(name = 'roll', help= 'Rolls a dice')
async def roll(ctx):
    rr = str(random.randint(1,6))
    await ctx.send(rr)

@bot.command(name = 'hello', help = 'Says Hello')
async def hello(ctx):
    hello = 'Hey Guys, Gabe Itch 2 here'
    await ctx.send(hello)

@bot.command(name = 'lucky_number', help = 'Random Lucky number 1-100' )
async def lucky_number(ctx):
    ln = str(random.randint(1,100))
    await ctx.send(ln)

@bot.command(name = 'fbi', help = 'FBI Open Up')
async def fbi(ctx):
    fbi = 'FBI OPEN UP!!!'
    await ctx.send(fbi)

@bot.command(name= 'percent_gay', help= 'Says how gay someone is. Remember to add the name of the person after the command')
async def percent_gay(ctx, who):
    p_gay = str(random.randrange(1, 100))
    await ctx.send(who + ' is ' + p_gay + '% ' + 'gay!')

@bot.command(name = 'albert_fish', help= 'Albert Fish')
async def albert_fish(ctx):
    alfish = 'ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERTALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT FISH ALBERT'
    await ctx.send(alfish)

@bot.command(name= 'percent_black', help= 'Says how black someone is')
async def percent_black(ctx, who):
    p_black = str(random.randrange(1, 100))
    await ctx.send(who + ' is ' + p_black + '% ' + 'black!')

@bot.command(name= 'purge', help= 'delet message')
async def purge(ctx, amount = 5):
    await ctx.channel.purge(limit= amount)

@bot.command(name='kick', help='kick nerds')
@has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason= None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick people!")

@bot.command(name='ban', help='ban nerds')
@has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason= None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been banned')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to ban people!")


bot.run(DISCORD_TOKEN)


