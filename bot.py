import discord
import os

from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

words = [["youre", "you're"], ["im", "i'm"], ["Im", "I'm"], ["hes", "he's"], ["shes", "she's"]]

@client.event
async def on_ready():
    print(f"Bot successfully logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for word in words:
        if word[0] in message.content:
            await message.channel.send(
                f"{message.author}, you misspelled {word[1]} as {word[0]}", 
                reference=message
            )

try:
    client.run(token)
except Exception:
    print("Error running client, token thrown = " + str(token))
