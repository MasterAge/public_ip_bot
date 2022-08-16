# Public IP discord bot
A discord bot that returns the public IP and customised port for a server. 

This can be run on a game server to allow players to request the server's IP without needing to setup DNS.

## Setup
You'll need to run through discord's bot setup steps and acquire a `DISCORD_TOKEN` before using this script.
See: https://www.xda-developers.com/how-to-create-discord-bot/

```bash
git clone git@github.com:MasterAge/public_ip_bot.git
cd public_ip_bot
pip install -r requirements.txt
echo "DISCORD_TOKEN=\"<token>\"" > .env

python bot.py
```