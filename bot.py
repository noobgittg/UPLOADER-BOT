import os
from plugins.config import Config
from pyrogram import Client

if __name__ == "__main__" :
    
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Client = Client("@UploaderXNTBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    upload_boost=True,
    sleep_threshold=200,
    plugins=plugins)
    print("I am Working..!!")
    Client.run()
