import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!ping":
        await message.channel.send("pong")

client.run(os.environ['MTM3NjIxNTg5NjAzNjQ3NDk5MQ.GGBwVF.Tv6Fr_EO91n2BnNHSqo-vvSflZPL2r7ZCfAewY'])
