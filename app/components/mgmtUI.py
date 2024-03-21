import discord

team = {
    "name": "Punks",
    "owner": "Owner",
    "coach": "Aimless",
    "manager": "Gamer",
    "starters": {"Tank": ["Roch"], "Dps": ["RealityGhost", "rishi"], "Support": ["Gamer", "Briefen"]},
    "subs": {"Tank":[], "Dps": ["illushannist"], "Support": ["JStar24", "Eggy"]},
    "tryouts": {"Tank":[], "Dps": ["geo"], "Support": []},
}

class TeamEmbed():
    def __init__(self, team):
        self.embed = discord.Embed(
            title=f"{team['name']} Roster",
            description=f"Management UI for {team['name']}.",
            color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
        )
        self.embed.add_field(name="Team Owner", value=f"{team['owner']}", inline=False)
        for role in list(team['starters'].keys()):
            self.embed.add_field(name=f"Starting {role}", value="\n".join(team['starters'][role]), inline=True)

        self.embed.set_footer(text="Footer! No markdown here.") # footers can have icons too
        self.embed.set_author(name="SHDW Management", icon_url="https://example.com/link-to-my-image.png")
        self.embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
        self.embed.set_image(url="https://example.com/link-to-my-image.png")



# Create a class called MyView that subclasses discord.ui.View
class MgmtView(discord.ui.View):

    # sign
    @discord.ui.button(label="sign", style=discord.ButtonStyle.success)
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked sign", view=DropDown())

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


class DropDown(discord.ui.Select):
    
    def __init__(self):
        super().__init__()
    
    # select dialogue
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Select user to edit", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vanilla",
                description="Pick this if you like vanilla!"
            ),
            discord.SelectOption(
                label="Chocolate",
                description="Pick this if you like chocolate!"
            ),
            discord.SelectOption(
                label="Strawberry",
                description="Pick this if you like strawberry!"
            )
        ]
    )
        
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")

# @bot.slash_command() # Create a slash command
# async def button(ctx):
#     await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button
