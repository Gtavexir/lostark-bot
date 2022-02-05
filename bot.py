import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="싀무룩 보호"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.command()
async def hello(ctx):
    await ctx.send("hello")
    
@client.command()
async def 페온(ctx):
    await ctx.send("로아샵 골드 시세*17 / 190")

@client.command()
async def 경매(ctx,*para):
    try:
        cost = int(para[0])
    except:
        await ctx.send("잘못된 입력입니다.")
    cost = cost * 0.95
    await ctx.send(f"4인 기준: {int(cost * 3/4)}\n8인 기준: int(cost * 0.95 * 7/8)\n16인 기준: int(cost * 0.95 * 15/16)")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")        

client.run(os.environ['token'])