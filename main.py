import discord
import os
from stay_awake import stay_awake

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
  "yeehaw",
  "oh_no",
  "kirby_dab",
  "poggy",
  "kirbyknife",
  "kirbyF",
  "kirbylove",
  "kirbycry",
  "kirbyahhh",
  "kirbysweat",
  "kirbysparkle",
  "pepeignore",
  "pepecry",
  "angerysad",
  "hehe",
  "angery",
  "kirbysit",
  "pikalul",
  "surprise",
  "reverse",
  "sheesh",
  "frog_knife",
  "fight",
  "zoop",
  "shy",
  "sad_cowboy_bread",
  "kya",
  "tiredcat",
  "pain",
  "kekdog",
  "zoomeyes",
  "crylaugh",
  "shockedpika",
  "IEatAChip",
  "Kirbyhug",
  "peepoe",
  "hmmhuh",
  "fuq",
  "ghosthug",
  "blobthonk",
  "gunright",
  "gunleft",
  "vibeFail",
  "vibeCheck",
  "kirb",
  "kitty_boba",
  "party_boba"]
custom_emoji = {}

@bot.event
async def on_ready():
  print("We have logged in. as {0.user}".format(bot))
  for name in custom_names:
    custom_emoji[name] = discord.utils.get(bot.emojis, name=name)
  print("Updated custom emojis")

@bot.event
async def on_message(message):
  if message.author == bot or message.author.id == 854021759564906497:
    return

  text = message.content.lower().strip()

  await autoreact(
    message, 
    "milk" in text, 
    [emoji["milk"], emoji["cow"]])

  vanja_id = 176483923868647424
  cc_id = 233744742154764288
  stuff_id = 320313823905054720
  milk_id = 584451089521442846

  await autoreact(
    message,
    "nut" in text,
    [custom_emoji["frog_knife"], custom_emoji["kirbyknife"]]
  )

  await autoreact(
    message,
    "anime" in text,
    [custom_emoji["kya"]]
  )

  await reply(
    message,
    "candice" in text,
    "can dis 🤪  fit in your mouth"
  )

  await reply(
    message,
    "dragon" in text,
    "imagine dragon deez 🤪"
  )

  await reply(
    message,
    message.author.id == vanja_id and "nut" in text,
    "jail"
  )

async def autoreact(message, condition, emojis):
  if condition:
    for emoji in emojis:
      await message.add_reaction(emoji)

async def reply(message, condition, response):
  if condition:
    await message.channel.send(response)

bot.run(token)
