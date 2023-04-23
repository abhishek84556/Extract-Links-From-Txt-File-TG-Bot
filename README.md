# Extract-Links-From-Txt-File-TG-Bot
Simple Telegram Bot to Extract links from Text Files
Fill the variables in https://github.com/pachax001/Extract-Links-From-Txt-File-TG-Bot/blob/main/docker-compose.yml file.
Fiil the variables in https://github.com/pachax001/Extract-Links-From-Txt-File-TG-Bot/blob/main/bot.py file.
Variables need to be filled
API_ID = Get it from here https://my.telegram.org/auth
API_HASH = "" Get it from here https://my.telegram.org/auth
BOT_TOKEN = "" Create a new bot using https://t.me/BotFather
Log_Channel = "" Create a log channel and add the channel id
Bot will work for any user.
Use docker compose to host the bot on a vps.
Follow the https://docs.docker.com/engine/install/ubuntu/ to install docker.
After installing clone the repo and fill the variables save files.
Then use 'sudo docker compose up' to start the bot.
Docker image support for linux amd64, arm64/v8, arm/v7
