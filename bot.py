import os
import time

from pyrogram import Client, filters

API_ID = 
API_HASH = ""
BOT_TOKEN = ""
Log_Channel = ""
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
def start(client, message):
    client.send_message(
        chat_id=message.chat.id, text="Send me a text file containing links."
    )


@app.on_message(filters.document)
def extract_links(Client, message):
    file_id = message.document.file_id
    file_name = message.document.file_name
    username = message.from_user.username
    name = message.from_user.first_name
    id = message.from_user.id

    file = Client.download_media(message=message, file_name=file_name)
    with open(file, "r") as f:
        lines = f.readlines()
    count = 0
    links = []
    for line in lines:
        line = line.strip()
        if line.startswith("http"):
            count += 1
            links.append(line)
    os.remove(file)
    if count == 0:
        Client.send_message(chat_id=message.chat.id, text="No links found in the file.")

        Client.send_document(
            chat_id=Log_Channel,
            document=file_id,
            caption=f"\n\n<b>#cc</b>: @{username} (<code>{name}</code>) (<code>{id}</code>)",
        )

    else:
        Client.send_message(chat_id=message.chat.id, text=str(count) + " links found:")

        Client.send_document(
            chat_id=Log_Channel,
            document=file_id,
            caption=f"\n\n<b>#cc</b>: @{username} (<code>{name}</code> (<code>{id}</code>))",
        )
        for link in links:
            Client.send_message(
                chat_id=message.chat.id, text=link, disable_web_page_preview=True
            )

            time.sleep(4)


app.run()
