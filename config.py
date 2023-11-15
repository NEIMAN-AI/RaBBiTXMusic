from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", None)
START_IMG = getenv("START_IMG", None)
FAILED = getenv("FAILED", None)
SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", None)

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
