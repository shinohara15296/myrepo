import discord
import asyncio
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 600978911761006593 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(600978912809451551)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)

client.run("NjM4NjYyMTA3OTQ4MTIyMTIy.Xbf-oQ.2moqWsvlCK7hrfQ5lilA_BiO6B0")
