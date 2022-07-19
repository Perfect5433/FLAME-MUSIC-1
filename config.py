## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCseN1uk-6D9XoHGf0l3G2aaXs_M07tCqWWenXHgXakkfmTSctRmle7ogWN4CS9-9gNxXh0dD78qcFMOzEE6U4P-01wlPyzk72uUIwuhp-XkewpFBLB4VeRWZLNBsccyUqOSmUl0Bv2z-c-uPzSt0xWBQOfkheLiQoe5LgX7UGfNeJNLgrNgMGtpAeVEfGP5R-k84rrfS4Ggww53D9BpSWkBMhUDBG-7rFMWLhaxVEf6WiPOYq57j_T6Se_3Notn-2kXW9QQulnB1pSHBmNqybNNkhreCiPCSzJsIvtlUi_IA_w3shWB2aTsBCWzlLDb-30CzsxfBwGt0H0JWuStFFyfJ8ywQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5365682329:AAH50JKcxuXPnvad_MtnIIng4kJBi1aNTv4")
BOT_NAME = getenv("BOT_NAME", "FlameMusicBot")
API_ID = int(getenv("API_ID", "12190971"))
API_HASH = getenv("API_HASH", "cd1481752891b60818e9fd0ceac09848")
OWNER_NAME = getenv("OWNER_NAME", "Perfect")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xmartperson")
ALIVE_NAME = getenv("ALIVE_NAME", "Flame")
BOT_USERNAME = getenv("BOT_USERNAME", "FlameMusicBot")
OWNER_ID = getenv("OWNER_ID", "5083524212")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Musicbot32")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Flame_project")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Flame_Updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5083524212").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2c23f012984fa91267146.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/2c23f012984fa91267146.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/S780821/Flame-Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
