# Python
# Init
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

roleGreeter = "<@&873675914578378842>"
rules = "873296117629079613"
nameChange = "872511776565129316"
announcement = "872351515661201449"
roleAssign = "872367240882814976"

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
        f"<@&873675914578378842> \n **Please welcome {member.name} !!!** \nRules are posted in 873296117629079613 \n Name change requests go here: 872511776565129316 \n Announcements are posted in 872351515661201449 \n"
        .." And lastly! Don't forget to assign your roles in 872367240882814976.. !"
    )

client.run(TOKEN)
