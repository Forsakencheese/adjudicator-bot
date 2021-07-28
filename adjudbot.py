#bot.py
#creating client instance for discord

#a client is an object that represents a connection to discord
#an event is something that happens on discord that you can use to trigger a reaction in your code
import os
import discord
import random
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='*')#establishing connection with discord to adjudicator

@bot.command(name='bestow', help= 'give a small chunk of wisdom')
async def on_message(ctx): #Blurt random wisdom on_message is

    wisdom_quotes = [
        'Heresy grows from idleness',
        'an open mind is like a fortress with its gates unbarred and unguarded',
        'Men without Faith are Men without direction',
        'There is no such thing as innocence, only degrees of guilt',
        'Through the destruction of our enemies do we earn our salvation',
        'Fear denies Faith',
        'DAMN THEE TO HELL',
        (
            'There is no enemy. The foe on the battlefield is merely the manifestation of that which we must overcome.'
            'He is doubt, and fear, and despair. Every battle is fought within. Conquer the battlefield that lies inside'
            'you, and the enemy disappears like the illusion he is'
        ),
        'Remember my dear brothers, the honed blade cuts deepest',
        'Hope is the first step on the road to disappointment'
    ]


    response = random.choice(wisdom_quotes)
    await ctx.send(response)

@bot.command(name='poll', help=' Creates a poll for the judging of the guilty')
async def poll_poll(ctx):

    response = 'Be silent, I must learn this knowledge first'
    await ctx.send(response)

bot.run(TOKEN)
