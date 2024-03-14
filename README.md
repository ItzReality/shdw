# SHDW eSports Team Management Discord Bot

## About

Discord bot made for SHDW eSports to assist team owners in managing their team, by supporting operations such as dropping, signing, and moving players within a team.

## How to run

- [ ] Use Discord developer portal to create a bot and copy the bot token (if you didn't previously have a bot or a token) and then add the bot to your desired server.

- [ ] Create a `.env` file and put the bot token and other sensitive variables inside of it and should look something like this:
  
```bash
CLIENT_ID=<YOUR_CLIENT_ID>
GUILD_ID=<YOUR_GUILD_ID>
DISCORD_TOKEN=<DISCORD_BOT_TOKEN>
```

- [ ] Run the following commands
  
```bash
python -m venv venv
source venv/bin/activate # only if you have UNIX/MacOS or are using a WSL shell
.\venv\Scripts\activate.bat # only if you have windows
python setup.py install
python app/bot.py
```
