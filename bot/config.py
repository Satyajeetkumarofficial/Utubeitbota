import re, os, time
import datetime


id_pattern = re.compile(r'^.\d+$') 


class Config:

    BOT_TOKEN ="5847138551:AAFyag9VMG7ZYhZIrIZ28vjYy8k8024Puug"

    SESSION_NAME = ":memory:"

    API_ID ="27491848"

    API_HASH ="d4e84c7a5c66e705c2d721a5d32b2fff"

    CLIENT_ID ="900959880281-jacjlpi0tfeche0ekbpuk5ke83aei1ic.apps.googleusercontent.com"

    CLIENT_SECRET ="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"

    BOT_OWNER ="5051184996"

    BOT_START_TIME = time.time()
    
    BOT_START_DATETIME = datetime.datetime.now().strftime("%B %d, %Y %I:%M:%S %p")

    DB_NAME = os.environ.get("DB_NAME", "Utubeitbot")  

    DB_URL = os.environ.get("DB_URL")

    SUPPORT_CHAT_LINK = os.environ.get("SUPPORT_CHAT_LINK")

    AUTH_USERS_TEXT ="5051184996"

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
