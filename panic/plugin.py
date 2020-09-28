import discord
from discord.ext import commands
import asyncio

def isStaff(ctx):
    helper = ctx.guild.get_role(718265043476807712)
    trainee = ctx.guild.get_role(718265254701826089)
    sccStaff = ctx.guild.get_role(751939549046898738)
    if helper in ctx.author.roles or trainee in ctx.author.roles or sccStaff in ctx.author.roles:
        return True
    else:
        return False


class Panic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x03a9f4
        self.error = 0xFF0000

    @commands.command(name="panic")
    async def panic_cmd(self, ctx, channel: discord.TextChannel, *, msg):
        if isStaff(ctx):
            news = ctx.guild.get_channel(738984082427346975)
            embed = discord.Embed(title="Panic Reported!", description=f"**{ctx.author}** just reported a panic!\n\nPanic Channel: {channel.mention}\n\nHis Message: ```{msg}```", color=self.color)
            await news.send("<@&751939549046898738>", embed=embed)
            await ctx.message.add_reaction("<a:SCCapproved:736730916235509832>")
            await asyncio.sleep(3)
            await ctx.message.delete()
        else:
            await ctx.message.add_reaction("🔒")
            embed = discord.Embed(title="Error", description="This command can only be used by **Staff Members**!", color=self.error)
            await ctx.send(embed=embed, delete_after=5.0)

def setup(bot):
    bot.add_cog(Panic(bot))
