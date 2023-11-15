from os import getenv

from dotenv import load_dotenv

load_dotenv()

# API_IDS
API_ID = int(getenv("API_ID")) # API_ID get it from my.telegram.org
API_HASH = getenv("API_HASH") # API_HASH get it from my.telegram.org

# SESSIONS
BOT_TOKEN = getenv("BOT_TOKEN", None) # BOT_TOKEN get it from @botfather on telegram
SESSION = getenv("SESSION", None) # SESSION get it from @sessionbot on telegram

# LIMITS
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90")) # DURATION_LIMIT fix ur bot song DURATION_LIMIT

# OWNER'S
OWNER_ID = int(getenv("OWNER_ID")) # OWNER_ID get it from @missrose_bot on telegram by send /id in miss rose bot dm
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split())) # SUDO_USERS same as OWNER_ID

# IMAGES
PING_IMG = getenv("PING_IMG", None) # PING_IMG A pic link that's use to check bot ping 
START_IMG = getenv("START_IMG", None) # START_IMG A pic link that's use to start the bot
FAILED = getenv("FAILED", None)

# SUPPORTS
SUPPORT_CHAT = getenv("SUPPORT_CHAT", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", None)
LOGGER_ID = getenv("LOGGER_ID", None)
