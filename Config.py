import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","25091352"))
    API_HASH = os.environ.get("API_HASH","69bc4f480dd07c77aa2e370af165c39c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","6220540045:AAG0XHSe2NXkmgvMMa0Owrbq3u_g54LqLQU")
    BOT_USERNAME = os.environ.get("bot_username","azetagg")
    BOT_NAME = os.environ.get("BOT_NAME","azetagg bot")
    BOT_ID = int(os.environ.get("BOT_ID","6220540045"))
    SUDO_USERS = os.environ.get("SUDO_USERS","senanpul").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","azetagg")
    OWNER_ID = int(os.environ.get("OWNER_ID","5534897878"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","senanpul")
