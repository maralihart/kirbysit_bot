import random

def get_autoreact(message, custom_emoji, emoji):
  text, split = text_cleaning(message)
  autoreactions = [
    ["milk" in text, [emoji["milk"], emoji["cow"]]],
    [True in ["nut" == i or "nuts" == i for i in split], [custom_emoji["kirbyknife"], custom_emoji["kirbythreaten"]]],
    ["anime" in text, [custom_emoji["kya"]]],
    ["kirby" in text and not ":ki" in text, [custom_emoji["surprise"], custom_emoji["kirbylove"], custom_emoji["kirbydab"]]]
  ]
  return autoreactions

def get_autoreply(message, ids):
  text, split = text_cleaning(message)
  autoresponses = [
    [message.author.id == ids["cc"] and "gacha" in text, "pull another, do it"],
    [message.author.id == ids["stuff"] and "swag" in text, "get swagged on B)"],
    ["candice" in text, "can dis 🤪  fit in your mouth"],
    ["dragon" in text, "imagine dragon deez 🤪"],
    [message.author.id == ids["vanja"] and True in ["nut" == i or "nuts" == i for i in split], "jail"],
    [message.author.id == ids["nasrat"] and "doodo" in text, ":("],
    [message.author.id == ids["shae"] and "validation" in text, "you are valid"],
    ["kms" in text or "kill myself" in text, "haha no you're so sexy 😜😎"]
  ]
  return autoresponses

def table_unflip(message):
  text, split = text_cleaning(message)
  if "┬─┬ ノ( ゜-゜ノ)" in text: 
    if random.random() < .7:
      await message.channel.send("thanks")
    else:
      await message.channel.send("no")
      await message.channel.send("(╯°□°）╯︵ ┻━┻")


def text_cleaning(message):
  text = message.content.lower().strip()
  split = text.split()
  return text, split