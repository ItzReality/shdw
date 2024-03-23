import discord
from discord.ext import commands
from components.mgmtUI import MgmtView
from components.embeds import TeamEmbed
from models.team import Team


class TeamManagement(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.players = {
            "roch": {"lineup": "starters", "role": "Tank"},
            "rishi": {"lineup": "starters", "role": "Dps"},
            "RealityGhost": {"lineup": "starters", "role": "Dps"},
            "Gamer": {"lineup": "starters", "role": "Support"},
            "Briefen": {"lineup": "starters", "role": "Support"},
            "illushannist": {"lineup": "subs", "role": "Dps"},
            "geo": {"lineup": "subs", "role": "Dps"},
            "JStar24": {"lineup": "subs", "role": "Support"},
            "Eggy": {"lineup": "subs", "role": "Support"},
            "clover": {"lineup": "tryouts", "role": "Tank"},
        }
        self.team = Team("Punks", "3", "rishi", "Aimless", "Gamer", self.players)

    def has_permission(self, member):
        # Check if the member has the "Team Owner" or "Staff" role
        # team_owner_role_name = (
        #     "apple sauce"  # Replace with the actual role name for team owners
        # )
        staff_role_name = "Staff"  # Replace with the actual role name for staff members

        # for role in member.roles:
        #     if role.name == team_owner_role_name or role.name == staff_role_name:
        #         return True
        # return False
        return True

    @discord.slash_command()
    async def getroles(self, ctx):
        roles = await ctx.guild.fetch_roles()
        await ctx.respond(f"{roles}")
        return roles

    @discord.slash_command()
    async def create_team(self, ctx, team_name: str):

        if self.has_permission(ctx.author):
            guild = ctx.guild
            member = ctx.author

            # Create a new role for the team
            role = await guild.create_role(name=team_name)

            # Add the role to the member
            await member.add_roles(role)

            await ctx.respond(
                f"The team {team_name} has been created and you have been assigned to it!"
            )
        else:
            await ctx.respond("You do not have the required role to use this command.")

    @discord.slash_command()
    async def assign_player(
        self, ctx, member: discord.Member, role: discord.Role, *, reason=""
    ):
        # Command to assign a player to a mentioned role
        if self.has_permission(ctx.author):
            # Check if the bot has the required permissions to manage roles
            if ctx.guild.me.guild_permissions.manage_roles:
                # Assign the mentioned role to the member
                await member.add_roles(role)
                await ctx.respond(
                    f"{member.mention} has been assigned to the role {role.name} for {reason}"
                )
            else:
                await ctx.respond(
                    "I do not have the required permissions to manage roles."
                )
        else:
            await ctx.respond("You do not have the required role to use this command.")

    @discord.slash_command()
    async def drop_player(
        self, ctx, member: discord.Member, role: discord.Role, *, reason=""
    ):
        # Command to drop a role from a mentioned <link>player</link>
        if self.has_permission(ctx.author):
            # Check if the bot has the required permissions to manage roles
            if ctx.guild.me.guild_permissions.manage_roles:
                # Remove the mentioned role from the member
                await member.remove_roles(role)
                await ctx.respond(
                    f"{member.mention} has been dropped from the role {role.name} for {reason}"
                )
            else:
                await ctx.respond(
                    "I do not have the required permissions to manage roles."
                )
        else:
            await ctx.respond("You do not have the required role to use this command.")

    @discord.slash_command()
    async def transfer_player(
        self, ctx, member: discord.Member, from_team: str, to_team: str
    ):
        # Command to transfer a player from one team to another
        if self.has_permission(ctx.author):
            # Logic to handle role transfer and logging
            await ctx.respond(
                f"{member.mention} has been transferred from {from_team} to {to_team}"
            )
        else:
            await ctx.respond("You do not have the required role to use this command.")

    # Other commands for promotions, roster updates, etc.

    @discord.slash_command()
    async def manage_roster(self, ctx, team_name: str):
        teamEmbed = TeamEmbed(self.team)
        await ctx.respond(
            "This is a button!", embed=teamEmbed.embed, view=MgmtView(teamEmbed)
        )

    # we can add event listeners to our cog
    # this is called when a member joins the server
    # you must enable the proper intents
    # to access this event.
    # See the Popular-Topics/Intents page for more info
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("Welcome to the server!")

    # on member role change checks to see if both the player and LFT role exist at once if so it removes the LFT role
    # note: this will require every member that is on a team to have the player role
    # @commands.Cog.listener()
    # async def on_member_update(self, before, after):
    #     player_role = discord.utils.get(after.guild.roles, name="player")
    #     lft_role = discord.utils.get(after.guild.roles, name="LFT")

    #     if player_role not in after.roles:
    #         if lft_role not in after.roles:
    #             await after.add_roles(lft_role)
    #             print(f"Gave LFT role back to {after.display_name}")

    #     if player_role in after.roles and lft_role in after.roles:
    #         await after.remove_roles(lft_role)
    #         print(f"Removed LFT role from {after.display_name}")


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(TeamManagement(bot))  # add the cog to the bot
