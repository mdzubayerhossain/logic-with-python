

import discord
from datetime import datetime
from dotenv import load_dotenv
import os 

load_dotenv()

# Discord bot token
TOKEN = TOKEN = os.getenv('TOKEN2')



# Channel ID of the channel you want to fetch messages from
CHANNEL_ID = 1126873503354859711
# CHANNEL_ID = 989166677390426132


# Date range (inclusive)
start_date = datetime(2024, 1, 9)  # YYYY, MM, DD
end_date = datetime(2024, 1, 10)   # YYYY, MM, DD

# Define intentsintents = discord.Intents.default()
intents.messages = True

# Initialize Discord client with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await fetch_messages()

async def fetch_messages():
    channel = client.get_channel(CHANNEL_ID)
    print(channel)
    if channel:
        async for message in channel.history(limit=None, after=start_date, before=end_date):
            print(f'{message.created_at}: {message.author.name} - {message.content}')
    else:
        print("Channel not found")

client.run(TOKEN)
