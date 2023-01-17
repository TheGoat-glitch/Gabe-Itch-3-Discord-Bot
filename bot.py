import os
import random

import discord
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from dotenv import load_dotenv
import discord.ext
from discord import app_commands
import giphy_client
from giphy_client.rest import ApiException


DISCORD_TOKEN = 'THE TOKEN'

load_dotenv()
TOKEN = os.getenv(DISCORD_TOKEN)

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

bot = commands.Bot(command_prefix='$', intents= intents)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1019459465453502594))
    print("The bot is ready!")


@tree.command(guild=discord.Object(id=1019459465453502594), description='test')
async def test(interaction: discord.Interaction, number: int, string: str):
    await interaction.response.send_message(f'{number=} {string=}', ephemeral=True)


@tree.command(guild=discord.Object(id=1019459465453502594), description='hi')
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message('hi')


@tree.command(guild=discord.Object(id=1019459465453502594), description='Music Hitler supporters listen to')
async def hitler_propaganda(interaction: discord.Interaction):
    await interaction.response.send_message('https://open.spotify.com/playlist/7J3dO4u5CMUQ2UzpJGGDLK')


@tree.command(guild=discord.Object(id=1019459465453502594), description="Hitler's Long Lost Son")
async def ye(interaction: discord.Interaction):
    await interaction.response.send_message('https://imgur.com/search/score?q=kanye')


@tree.command(guild=discord.Object(id=1019459465453502594), description="Hitler's long lost son")
async def kanye(interaction: discord.Interaction,*, q: str = 'Kanye'):
    api_key = "eN57UOl0oCBIEjBJxsyL56c5KQLfbEx0"
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key, q)
        lst = list(api_response.data)
        giff = random.choice(lst)

        await interaction.response.send_message(giff.embed_url)

    except ApiException as e:
        print("Exception when calling Api")


@tree.command(guild=discord.Object(id=1019459465453502594), description="Search for a random gif!")
async def gif_search(interaction: discord.Interaction,*, q: str):
    api_key = "eN57UOl0oCBIEjBJxsyL56c5KQLfbEx0"
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key, q)
        lst = list(api_response.data)
        giff = random.choice(lst)

        await interaction.response.send_message(giff.embed_url)

    except ApiException as e:
        print("Exception when calling Api")


@tree.command(guild=discord.Object(id=1019459465453502594), description="Random gifs!")
async def random_gif(interaction: discord.Interaction, q: str = 'random'):
    api_key = "eN57UOl0oCBIEjBJxsyL56c5KQLfbEx0"
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key,q)
        lst = list(api_response.data)
        giff = random.choice(lst)

        await interaction.response.send_message(giff.embed_url)

    except ApiException as e:
        print("Exception when calling Api")


@tree.command(guild=discord.Object(id=1019459465453502594), description="Trending gifs!")
async def trending_gif(interaction: discord.Interaction):
    api_key = "eN57UOl0oCBIEjBJxsyL56c5KQLfbEx0"
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_trending_get(api_key)
        lst = list(api_response.data)
        giff = random.choice(lst)

        await interaction.response.send_message(giff.embed_url)

    except ApiException as e:
        print("Exception when calling Api")


@tree.command(guild=discord.Object(id=1019459465453502594), description="What percentage is someone of something")
async def percentage(interaction: discord.Interaction, who: str, what: str):
    percentage = str(random.randint(1, 100))
    await interaction.response.send_message(who + ' is ' + percentage + '% ' + what + '!')


@tree.command(guild=discord.Object(id=1019459465453502594), description="% generator")
async def percent(interaction: discord.Interaction):
    percent = str(random.randint(1, 100))
    await interaction.response.send_message(percent + '%')


@tree.command()
async def slash_command(int: discord.Interaction):
    await int.response.send_message("pp")

client.run(DISCORD_TOKEN)


