import discord


# Create a class called MyView that subclasses discord.ui.View
class MgmtView(discord.ui.View):

    # sign
    @discord.ui.button(label="sign", style=discord.ButtonStyle.success)
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked sign")

    # promotes
    @discord.ui.button(label="promotes", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked promotes")

    # drop
    @discord.ui.button(label="drop", style=discord.ButtonStyle.danger)
    async def third_button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked drop")

    # demotes
    @discord.ui.button(label="demotes", style=discord.ButtonStyle.secondary)
    async def fourth_callback(self, button, interaction):
        await interaction.response.send_message("You clicked demotes")


# @bot.slash_command() # Create a slash command
# async def button(ctx):
#     await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button
