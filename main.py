import discord,os,asyncio
from discord.ext import commands
game=discord.Game("글링아 도움")
bot = commands.Bot(command_prefix='글링아 ',status=discord.Status.online, activity=game)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def 안녕(ctx):
    await ctx.send('반가워요.')
@bot.command()
async def 도움(ctx):
    embed=discord.Embed(title= f"글링이 도움",description=f"글링이 도움말")
    embed.add_field(name=f"글링아", value=f"글링이 명령어를 실행", inline=False)
    embed.add_field(name=f"도움", value=f"글링이 도움말을 실행", inline=False)
    await ctx.send(embed=embed)

bot.run('NzQxMTk2MjE2MTg0MDc4Mzg3.Xy0CxA.0RrO0nnuQJJ1aaMVxDYUt6FjSGY')
