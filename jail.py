async def jail_check(bot, message):
  if message.content.startswith("!jail"):
    jailed_info = get_jailed_info(bot, message)
    await jailed_info[0].add_roles(jailed_info[1])
    await message.channel.send(jailed_info[2] + " you've been jailed 👮‍♀️", tts=True)

  if message.content.startswith("!pardon"):
    if message.author == message.mentions[0]:
      await message.channel.send("shut up 👊 u can't pardon yourself")
      return
    jailed_info = get_jailed_info(bot, message)
    await jailed_info[0].remove_roles(jailed_info[1])

def get_jailed_info(bot, message):
  guild = bot.get_guild(688913497710395429)
  jailed = message.mentions[0]
  jailed_name = jailed.nick if jailed.nick else jailed.name
  jailed_role = guild.get_role(852300326026739732)
  return [jailed, jailed_role, jailed_name]