import discord
from models.team import Team


class TeamEmbed:
    def __init__(self, team: Team):
        self.team = team
        self.embed = None
        self.buffer = None
        self.fillBuffer()
        self.drawEmbed()

    # format Team object to a buffer that can be embedded
    def fillBuffer(self):
        buffer = {
            "starters": {"Tank": [], "Dps": [], "Support": []},
            "subs": {"Tank": [], "Dps": [], "Support": []},
            "tryouts": {"Tank": [], "Dps": [], "Support": []},
        }

        for player in list(self.team.players.keys()):
            # print(player, self.team.players[player])

            buffer[self.team.players[player]["lineup"]][
                self.team.players[player]["role"]
            ].append(player)

        self.buffer = buffer

    def drawEmbed(self):
        if self.embed:
            self.embed.clear_fields()

        self.embed = discord.Embed(
            title=f"{self.team.name} Roster",
            description=f"Management UI for Div-{self.team.div} {self.team.name}.",
            color=discord.Colour.blurple(),  # Pycord provides a class with default colors you can choose from
        )

        self.embed.add_field(name="Coach", value=f"{self.team.coach}", inline=False)

        self.embed.add_field(
            name="Team Owner", value=f"{self.team.owner}", inline=False
        )

        self.embed.add_field(name="Manager", value=f"{self.team.manager}", inline=False)

        # add starters to the embed
        for role in list(self.buffer["starters"].keys()):
            self.embed.add_field(
                name=f"Starting {role}",
                value="\n".join(self.buffer["starters"][role]),
                inline=True,
            )

        # add subs to the embed
        for role in list(self.buffer["subs"].keys()):
            self.embed.add_field(
                name=f"Sub {role}",
                value="\n".join(self.buffer["subs"][role]),
                inline=True,
            )

        # add tryouts to the embed
        self.embed.add_field(
            name=f"Tryouts",
            value=f"{"\n".join(self.buffer["tryouts"]['Tank'])}{"\n".join(self.buffer["tryouts"]['Dps'])} {"\n".join(self.buffer["tryouts"]['Support'])}",
            inline=True,
        )

        self.embed.set_author(
            name="SHDW Management", icon_url="https://example.com/link-to-my-image.png"
        )

    def updateTeam(self):
        self.fillBuffer()
        self.drawEmbed()
