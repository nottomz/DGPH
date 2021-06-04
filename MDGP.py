import discord, asyncio, datetime, os



client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!모집'):
        global user0
        user0 = message.author
        global switch
        switch = 1
        recruite = message.content[4:].split(" / ")
        embed = discord.Embed(title=user0.display_name + "님의 화력팀모집",description=recruite[0], timestamp = datetime.datetime.utcnow(), color=0x00ff00)
        embed.add_field(name="Join - \U00002705", value="하단 확인 이모지를 클릭해 합류신청", inline=True)
        embed.add_field(name="Spare - \U00002754", value="하단 물음표 이모지를 클릭해 예비인원신청", inline=True)
        embed.set_footer(text="Made by NOTTOMZ", icon_url="https://cdn.discordapp.com/attachments/848922428893167616/850365287810465812/90685415899733960.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/848922428893167616/848929661256728596/JPEG_20191207_2153201.jpg")
        await message.channel.purge(limit=1)
        msg = await message.channel.send(embed=embed)     
        await msg.add_reaction("\U00002705") #합류
        await msg.add_reaction("\U00002754") #예비




    if message.content.startswith('!취소'):
        if user0 != message.author:
            await message.channel.purge(limit=1)
            await message.channel.send("======================================")
            await message.channel.send("모집중인 파티가 없습니다. \U0001F914")
            await message.channel.send("======================================")
            switch = 1
            return None
        if switch == 1:
            await message.channel.purge(limit=1)
            await message.channel.send("======================================")
            await message.channel.send(user0.display_name + "님이 화력팀 모집을 취소 하였습니다. \U0001F97A")
            await message.channel.send("======================================")
            switch = 0





@client.event 
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇 체크
        return None
    if switch == 0:    
        await reaction.message.channel.send(user0.display_name + "님의 파티는 취소되어 신청 할 수 없습니다. \U0001F61C")
        return None
    if str(reaction.emoji) == "\U00002705": #이모지 리액션 체크
        await reaction.message.channel.send(user0.display_name + "님의 파티에 " + user.display_name + "님이 참여를 신청하셨습니다.")
    if str(reaction.emoji) == "\U00002754":
        await reaction.message.channel.send(user0.display_name + "님의 파티에 " + user.display_name + "님이 예비인원으로 신청하셨습니다.")


access_token = os.environ['BOT_TOKEN']
client.run(access_token)
