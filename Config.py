import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","18049084"))
    API_HASH = os.environ.get("API_HASH","7e74b1e22026fcc291d32b3d431aa21e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","6110153217:AAGY1JLW78Ng9gpIyBtLpK2NHB7U4NgNhZQ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","AhriTaggerBot")
    BOT_NAME = os.environ.get("BOT_NAME","Ahri")
    BOT_ID = int(os.environ.get("BOT_ID","6445812901"))
    SUDO_USERS = os.environ.get("SUDO_USERS","rahmetinc").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","redhackarsiv")
    OWNER_ID = int(os.environ.get("OWNER_ID","5944841427"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","rahmetİnc")
