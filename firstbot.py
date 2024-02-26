import discord
from discord.ext import commands
from discord.ui import Button, View


intents = discord.Intents.all()
client = discord.Client(intents=intents)
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
BOT_TOKEN = ""
channel_id = 1161079903094063204
@client.event
async def on_ready():
    # Create a button
    button = Button(label="Click me!")

    # Create a view
    view = View()
    view.add_item(button)

    # Send the view to a user
    await client.get_user(350052097682833418).send(view)
    async def on_ready():
        print('ShadOW Org bot is ready')
        channel = bot.get_channel(channel_id)
        await channel.send("Team management bot ready!")
    @button.callback
    async def on_button_Click(interaction, button):
        # Send a message to the user
        await interaction.respond("You clicked the button!")
client.run(BOT_TOKEN)




def has_permission(member):
    # Check if the member has the "Team Owner" or "Staff" role
    team_owner_role_name = "team owner"  # Replace with the actual role name for team owners
    staff_role_name = "Staff"  # Replace with the actual role name for staff members
    
    for role in member.roles:
        if role.name == team_owner_role_name or role.name == staff_role_name:
            return True
    return False

@bot.event
async def on_ready():
    print('ShadOW Org bot is ready')
    channel = bot.get_channel(channel_id)
    await channel.send("Team management bot ready!")

@bot.command()
async def create_team(ctx, team_name: str):
    # Command to create a role representing a team and assign it to the user
    if has_permission(ctx.author):
        guild = ctx.guild
        member = ctx.author

        # Create a new role for the team
        role = await guild.create_role(name=team_name)

        # Add the role to the member
        await member.add_roles(role)

        await ctx.send(f'The team {team_name} has been created and you have been assigned to it!')
    else:
        await ctx.send("You do not have the required role to use this command.")

@bot.command()
async def assign_player(ctx, member: discord.Member, role: discord.Role, *, reason=""):
    # Command to assign a player to a mentioned role
    if has_permission(ctx.author):
        # Check if the bot has the required permissions to manage roles
        if ctx.guild.me.guild_permissions.manage_roles:
            # Assign the mentioned role to the member
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been assigned to the role {role.name} for {reason}')
        else:
            await ctx.send("I do not have the required permissions to manage roles.")
    else:
        await ctx.send("You do not have the required role to use this command.")

@bot.command()
async def drop_player(ctx, member: discord.Member, role: discord.Role, *, reason=""):
    # Command to drop a role from a mentioned <link>player</link>
    if has_permission(ctx.author):
        # Check if the bot has the required permissions to manage roles
        if ctx.guild.me.guild_permissions.manage_roles:
            # Remove the mentioned role from the member
            await member.remove_roles(role)
            await ctx.send(f'{member.mention} has been dropped from the role {role.name} for {reason}')
        else:
            await ctx.send("I do not have the required permissions to manage roles.")
    else:
        await ctx.send("You do not have the required role to use this command.")
@bot.command()
async def transfer_player(ctx, member: discord.Member, from_team: str, to_team: str):
    # Command to transfer a player from one team to another
    if has_permission(ctx.author):
        # Logic to handle role transfer and logging
        await ctx.send(f'{member.mention} has been transferred from {from_team} to {to_team}')
    else:
        await ctx.send("You do not have the required role to use this command.")


# Other commands for promotions, roster updates, etc.

bot.run(BOT_TOKEN)  # Use the BOT_TOKEN variable here
