from os import getenv

from dotenv import load_dotenv

load_dotenv()

# API_IDS
API_ID = int(getenv("API_ID")) # API_ID get it from my.telegram.org
API_HASH = getenv("API_HASH") # API_HASH get it from my.telegram.org

# SESSIONS
BOT_TOKEN = getenv("BOT_TOKEN", None)
SESSION = getenv("SESSION", None)

# LIMITS
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

# OWNER'S
OWNER_ID = int(getenv("OWNER_ID"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

# IMAGES
PING_IMG = getenv("PING_IMG", None)
START_IMG = getenv("START_IMG", None)
FAILED = getenv("FAILED", None)

# SUPPORTS
SUPPORT_CHAT = getenv("SUPPORT_CHAT", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", None)
LOGGER_ID = getenv("LOGGER_ID", None)
