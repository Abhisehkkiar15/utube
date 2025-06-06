import os


class Config:

    BOT_TOKEN = os.environ.get("7550835247:AAFckRORTZhuy5wG0zICJSn-livYG8a5H-4")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("25331263"))

    API_HASH = os.environ.get("cab85305bf85125a2ac053210bcd1030")

    CLIENT_ID = os.environ.get("343438892583-f2bedg8cocfkuos628637fnhhuqjp4qo.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("1955406483"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
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
