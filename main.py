import discord
import os
from stay_awake import stay_awake
import commands
import jail
import conditions

stay_awake()

token = os.environ['TOKEN']
bot = discord.Client()

emoji = {
  "milk": "🥛",
  "cow": "🐄",
  "shark": "🦈",
  "basketball": "🏀",
  "boba": "🧋",
  "wave": "👋",
  "heart_face":"🥰",
  "shy": "🥺",
  "shush": "🤫"
  }

custom_names = [
  "kirbyknife",
  "kirbydab",
  "kirbythreaten",
  "kya",
  "surprise",
  "kirbylove"]
custom_emoji = {}

ids = {
  "vanja": 176483923868647424,
  "cc": 233744742154764288,
  "stuff": 320313823905054720,
  "milk": 584451089521442846,
  "nasrat": 149370232413224961,
  "shae": 689672010716282969,
  "ib": 288495370869407745,
}

@bot.event
async def on_ready():
  print("We have logged in. as {0.user}".format(bot))
  for name in custom_names:
    custom_emoji[name] = discord.utils.get(bot.emojis, name=name)

@bot.event
async def on_message(message):
  global ids

  if message.author == bot.user:
    return

  # auto reactions
  for autoreaction in conditions.get_autoreact(message, custom_emoji, emoji):
    await autoreact(message, autoreaction[0], autoreaction[1])

  # auto responses
  for autoresponse in conditions.get_autoreply(message, ids):
    await automessage(message, autoresponse[0], autoresponse[1])

  conditions.table_unflip(message)

  # auto roles
  await jail.jail_check(bot, message)
  
  # misc commands
  await commands.commands(message)

async def autoreact(message, condition, emojis):
  if condition:
    for emoji in emojis:
      await message.add_reaction(emoji)

async def automessage(message, condition, response):
  if condition:
    await message.channel.send(response)

bot.run(token)