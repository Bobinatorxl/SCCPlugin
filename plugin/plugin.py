import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime

class allInOne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x00FF00
        self.timer = 10

    @tasks.loop(seconds=10)
    async def loopy(self):
        guild = self.bot.get_guild(717859817032515755)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"SCC | DM For Help | {guild.member_count} Members"))
        await asyncio.sleep(5)

    @commands.command(name="start_status")
    async def start_the_status(self, ctx):
        self.loopy.start()
        await ctx.send("Started! If you are encountering any issues please run this command again!")

    @commands.command(name="rule")
    async def rule_command(self, ctx, ruleNum = None):
        await ctx.message.delete()
        if not ruleNum:
            await ctx.send("Hey there! This is the rules command, please include the Rule Number and ill let you know what it is!")
        else:
            if int(ruleNum) == 1:
                await ctx.send("Discord Terms of Service can be found here: https://discord.com/new/terms. Discord needs you to be 13 or above to join this server.")
            elif int(ruleNum) == 2:
                await ctx.send("YT Terms of Service can be found here: https://www.youtube.com/static?template=terms, Twitch Terms of Service can be found here: https://www.twitch.tv/p/legal/terms-of-service/")
            elif int(ruleNum) == 3:
                await ctx.send("No swearing, gory language, 18+ images or text should be posted here. This is a family friendly server and if you do that you will be punished. Don't have your status, name or profile picture say anything inappropriate. Please have ping-able names, this means at least having a few normal characters where staff can ping you if necessary.")
            elif int(ruleNum) == 4:
                await ctx.send("Only advertise in the correct areas, look above in the FAQ for a list of all the advertising channels possible. Only promote in the correct areas. Please do not direct message members with any sort of promotion as that will be a ban.")
            elif int(ruleNum) == 5:
                await ctx.send("All punishment is up to staff and if you think you were falsely punished or want to report a staff <@735200954026033286>. Staff can punish you at any time for any reason and have the final say.")
            elif int(ruleNum) == 6:
                await ctx.send("Do not talk about self harm or suicide here. While it is important this is not the right place, if you or a friend is contemplating suicide call this number: 1-800-273-8255. Please do not post downloadable files or anything that is spyware, malware or any type of ip grabber or hack. The bots advertised in <@720712592812671057> are use at your own risk.")
            elif int(ruleNum) > 6 or int(ruleNum) <= 0:
                await ctx.send("This rule has not been found!")
    
    #commands.BucketType.user for user
    #commands.BucketType.guild for server
    # change the "10" to whatever time
    @commands.command(name="welcome", aliases=['wel'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def welcome_cmd(self, ctx):
        await ctx.message.delete()
        await ctx.send("<a:SCCwelcome:752725582449737808> Welcome to the server, we hope you have a great time here!")

    @commands.command(name="topic")
    async def topic_cmd(self, ctx):
        await ctx.message.delete()
        await ctx.send("Please change the topic/discussion, any furthur discussion of this may lead to punishments!")

    @commands.command(name="boost")
    async def boost_cmd(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title="Booster Perks",
            description=f"<:SCCnitro:744273792527892570> If you boost 1 time the rewards are: \n➢ A free spotlight\n➢ Access to all 3 premium advertising channels\n➢ All chat perms!\n<:SCCnitro:744273792527892570> If you boost 2 times you get:\n➢ Everything from before but another free spotlight!",
            color=self.color
            timestamp=ctx.message.created_at
        )
        await ctx.send(embed=embed)

    @commands.command(name="verify")
    async def verify_cmd(self, ctx):
        if not ctx.channel.id == 720012169567010836:
            return
        else:
            await ctx.message.add_reaction("✅")
            await asyncio.sleep(3)
            await ctx.message.delete()
            # Verify roles
            role1 = ctx.guild.get_role(718174958936653884)
            role2 = ctx.guild.get_role(726859506339938365)
            role3 = ctx.guild.get_role(725807695990358057)
            role4 = ctx.guild.get_role(726853712320004227)
            role5 = ctx.guild.get_role(726862277965512816)
            # Add the role
            await ctx.author.add_roles(role1, role2, role3, role4, role5)
            # Send the log msg
            log_channel = ctx.guild.get_channel(758759424235405312)
            embed = discord.Embed(
                title="Someone just verified!",
                description=f"**{ctx.author}** just verified!\n\nTheir ID is: {ctx.author.id}\nTheir name is: {ctx.author.name}\nTheir discriminator is: {ctx.author.discriminator}\n\nThe message ID is: {ctx.message.id}\nThe channel ID is: {ctx.message.channel.id}\n\nMessage was sent at {datetime.utcnow()} UTC",
                color=self.color,
                timestamp=ctx.message.created_at
            )
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 720012169567010836:
            if message.content.lower() == ".verify":
                return
            if message.author.id != 735200954026033286: # The Bot ID
                await message.delete()
            else:
                return
        else:
            return
    
    @welcome_cmd.error
    async def wel_cmd_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.add_reaction("<:SCCtimer:754060791455416321>")
        else:
            raise error
    
def setup(bot):
    bot.add_cog(allInOne(bot))
