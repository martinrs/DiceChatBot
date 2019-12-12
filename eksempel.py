import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='roll', help='Roll any number of dice with any number of sides. E.g. "!roll d8" rolls a single eight sided die,\nwhile "!roll 4d12" rolls four separate twelve sided dice.')
async def roll(ctx, dice=None):
    response = 'Invalid use of roll command. Try "!help roll".'
    if dice != None:
        dice = dice.lower().split('d')

        if dice[0].isdigit():
            dice[0] = int(dice[0])
        elif dice[0] == '':
            dice[0] = 1

        if dice[1].isdigit() and isinstance(dice[0], int):
            response = ''
            dice[1] = int(dice[1])
            for die in range(dice[0]):
                response += '{} '.format(random.randint(1, dice[1]))

    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(token)
