import discord
import os
import requests
import json
from vndb_thigh_highs import VNDB
from vndb_thigh_highs.models.operators import and_, or_, search
from vndb_thigh_highs.models import VN
client = discord.Client();
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!vn'):
    string = message.content.split(' ')
    title = string[1].lower()
    vndb = VNDB()
    try:
      vns = vndb.get_vn(search(VN.title, title))
      vn = vns[0]
    except:
      await message.channel.send("Không tìm thấy Visual Novel")
    await message.channel.send(vn.image)
    await message.channel.send("https://vndb.org/v" + str(vn.id))
    

client.run(os.getenv('TOKEN'))
