import discord
from .embeds import TeamEmbed


# Create a class called MgmtView that contains interactive buttons for team management
class MgmtView(discord.ui.View):

    def __init__(self, embed: TeamEmbed):
        super().__init__()
        self.embed = embed

    # sign
    @discord.ui.button(label="sign", style=discord.ButtonStyle.success)
    async def first_button_callback(self, button, interaction):
        self.embed.team.signPlayer("clover", "tryouts", "Tank")
        self.embed.updateTeam()
        await interaction.response.edit_message(embed=self.embed.embed, view=self)

    # promotes
    @discord.ui.button(label="promotes", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        self.embed.team.promotePlayer("clover")
        self.embed.updateTeam()
        await interaction.response.edit_message(embed=self.embed.embed, view=self)

    # drop
    @discord.ui.button(label="drop", style=discord.ButtonStyle.danger)
    async def third_button_callback(self, button, interaction):
        self.embed.team.dropPlayer("clover")
        self.embed.updateTeam()
        await interaction.response.edit_message(embed=self.embed.embed, view=self)

    # demotes
    @discord.ui.button(label="demotes", style=discord.ButtonStyle.secondary)
    async def fourth_callback(self, button, interaction):
        self.embed.team.demotePlayer("clover")
        self.embed.updateTeam()
        await interaction.response.edit_message(embed=self.embed.embed, view=self)


# # Create a class called DropDown that contains a dropdown menu for team management
# class DropDown(discord.ui.Select):

#     def __init__(self):
#         super().__init__()

#     # select dialogue
#     @discord.ui.select(  # the decorator that lets you specify the properties of the select menu
#         placeholder="Select user to edit",  # the placeholder text that will be displayed if nothing is selected
#         min_values=1,  # the minimum number of values that must be selected by the users
#         max_values=1,  # the maximum number of values that can be selected by the users
#         options=[  # the list of options from which users can choose, a required field
#             discord.SelectOption(
#                 label="Vanilla", description="Pick this if you like vanilla!"
#             ),
#             discord.SelectOption(
#                 label="Chocolate", description="Pick this if you like chocolate!"
#             ),
#             discord.SelectOption(
#                 label="Strawberry", description="Pick this if you like strawberry!"
#             ),
#         ],
#     )
#     async def select_callback(
#         self, select, interaction
#     ):  # the function called when the user is done selecting options
#         await interaction.response.send_message(
#             f"Awesome! I like {select.values[0]} too!"
#         )
