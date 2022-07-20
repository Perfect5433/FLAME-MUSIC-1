## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAQ9FbKu_yS7ONO9YUdkgSp5PU6hOyscW9Nki4VEglK6jmhRp85Zf3ADVoZT_HJSPwILSfL5Qw8p5qlDKf11egzpS2ybQmPB7apYZvWDrxjx0Xp07jx5PtZvfvm-4rIYzaDUvNX3OwV5JeuNAvziDoENJKaVP9UvRQCWROelxa2Evd1Dq0MaTMVZEQhjF3KI2015aJzx4-ZtWGLrQ9ShPCzsM7hO7mVjxKQeT_KeF_D8UIHyNEsOaPBOmfjNjC8fC0JM1EE9avopqPwAfProaQ4DokQlG44gN1CgVK4fu0ZqN_OIG3gbmaFK7RQUIcptcEnje6FwgowaU8JPvdhTY0YeDgIGAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5300563520:AAGcZ1kQeipKuu3rAW7I7SvmuAx0f67YDN4")
BOT_NAME = getenv("BOT_NAME", "Flamemusicbot")
API_ID = int(getenv("API_ID", "6393543"))
API_HASH = getenv("API_HASH", "88fcd4f66f322a6cc483dd4cd33bdc84")
OWNER_NAME = getenv("OWNER_NAME", "Xmartperson")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xmartperson")
ALIVE_NAME = getenv("ALIVE_NAME", "Flame")
BOT_USERNAME = getenv("BOT_USERNAME", "Flamemusicbot")
OWNER_ID = getenv("OWNER_ID", "5083524212")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Checkbt5")
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
