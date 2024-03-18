import discord


class Client(discord.Bot):
    def __init__(self, token, intents):
        super().__init__(intents=intents)
        self.token = token

    async def on_ready(self):
        print("ShadOW Org bot is ready")
        channel = self.get_channel(748588587599003738)
        await channel.send("Team management bot ready!")

    def activate(self):
        self.load_extension("cogs.teammgmt")
        self.run(self.token)
