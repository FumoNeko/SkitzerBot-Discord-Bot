# Python
# Init
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Startup event
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# On member join event
@client.event
async def on_member_join(member):
    guild = client.get_guild(783515548192866345)
    channel = guild.get_channel(872356789822312479)
    await channel.send(
        f"<@&873675914578378842> \n **Please welcome** {member.mention} **!!!** \n Rules are posted in <#873296117629079613> \n Name change requests go here: <#872511776565129316> \n Announcements are posted in <#872351515661201449> \n"
        .." And lastly! Don't forget to assign your roles in <#872367240882814976> !"
    )

    if member == client.user:
        return

client.run(TOKEN)
