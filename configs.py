# (c) kryptonian coder
import os
#from dotenv import load_dotenv

#load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 29283028))
    API_HASH = os.getenv("API_HASH", "00e080762d7d5f20fcb5a9337d7a1bac")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5851110616:AAGxEXc76vsovtSdoPjbhy8Q9OPkI9kP-kI")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "BRAVESTONE")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOIcBu2bvMXb04Ct-yoJVxyWk4QZkbSVLIl_0YdXxoLMWC1K58qK4oqih8Ib44jHhAlvpKgh0v4qalPzDU9MhCzaNKVTadpkXRmVgcyjNYTABD52Hj17lYaoy1b6m7p8gj3ICaIlAHR9wF85pIDFmsUrS3aF2xjBrOiRRoLdkkdKRn6YJtyvrib6xgL-MoVq6wyejm2V70BdtSZZWDECVlnfuvnfTjFYmNuCaW7SwnUngUl7_vzmsARc23D0IDGQvR-UtJtdxQSN1TFQn_ANRD6YKFIIHZzsCnx0awx1_UOKCaRhyzgDFajOvdIChTXk5LKIdXKkHSPLdOoVn4h4eVG6RZQA=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1001805094850))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Bravemoviesprovider_bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", 1739321854))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Jackkjack")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "A12111111111")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", '''Hᴇʏ Boss! 

Yᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ first contact me to get access.☺️

Fᴏʀ Mᴏʀᴇ Iɴꜰᴏ Cʟɪᴄᴋ Oɴ Hᴇʟᴘ ✅''')
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/3073c7543fc3ab93659d9.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", '''ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ,
ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅''')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001897220638")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Jhonbrave:16nihalpk16@cluster0.piqasdd.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001654343251"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 8))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "click_for_all_updates")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 100))
    MDISK_API = os.getenv("MDISK_API", "xerksgsIlGJBRm3TCNRo")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "365"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''IAM DEVELOPED MY,SON OF KRYPTON✅

ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ, @click_for_all_updates''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", ''' HEY THERE MUST JOIN,@click_for_all_updates

 Sᴛᴇᴘ 1 - FOR ALL DETAILS JOIN THIS.@click_for_all_updates

 Sᴛᴇᴘ 2 - FOR ALL UPDATES JOIN THIS.@click_for_all_updates''')
