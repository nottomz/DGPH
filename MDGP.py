import discord
import os
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/모집'):
        global user0
        user0 = message.author
        recruite = message.content[4:].split(" / ")
        embed = discord.Embed(title=user0.name + "님의 화력팀모집",description=recruite[0])
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/848922428893167616/848929661256728596/JPEG_20191207_2153201.jpg")
        embed.add_field(name="Join - \U00002705", value="하단 확인 이모지를 클릭해 합류신청", inline=True)
        embed.add_field(name="Spare - \U00002754", value="하단 물음표 이모지를 클릭해 예비인원신청", inline=True)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("\U00002705") #합류
        await msg.add_reaction("\U00002754") #예비
        
@client.event 
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇 체크
        return None
    if str(reaction.emoji) == "\U00002705": #이모지 리액션 체크
        await reaction.message.channel.send(user0.display_name + "님의 파티에 " + user.display_name + "님이 참여를 신청하셨습니다.")
    if str(reaction.emoji) == "\U00002754":
        await reaction.message.channel.send(user0.display_name + "님의 파티에 " + user.display_name + "님이 예비인원으로 신청하셨습니다.")

#@client.event        
#async def on_reaction_remove(reaction, user):
#    if user.bot == 1: #봇 체크
#        return None
#    if str(reaction):
#        await reaction.message.channel.send(user.name + "님이 합류를 취소하였습니다.")
#    if str(reaction.emoji) == "\U00002754":
#        await reaction.message.channel.send(user.name + "님이 예비인원 합류를 취소하셨습니다.")

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
