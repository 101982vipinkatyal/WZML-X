# REQUIRED CONFIG
BOT_TOKEN = "7343143974:AAFjaSFCrgv5MdrZDyLXv_YXhDPiYphLFq0"                              # Require restart after changing it while bot running
OWNER_ID = "943270135"                               # Require restart after changing it while bot running
TELEGRAM_API = "28983177"                           # Require restart after changing it while bot running
TELEGRAM_HASH = "a0da2f0c10923e1c080fd86ab4c04051"                          # Require restart after changing it while bot running
DATABASE_URL = "mongodb+srv://resourjickm1:Cidcompressrot@cidcompressrot.v2g1mqi.mongodb.net/?retryWrites=true&w=majority&appName=Cidcompressrot"                           # Require restart after changing it while bot running

# OPTIONAL CONFIG
DEFAULT_LANG = "en"
TG_PROXY = {}            # {"scheme": ”socks5”, "hostname": ””, "port": 1234, "username": ”user”, "password": ”pass”}
USER_SESSION_STRING = ""
CMD_SUFFIX = ""
AUTHORIZED_CHATS = ""
SUDO_USERS = ""
STATUS_LIMIT = 10
DEFAULT_UPLOAD = "rc"
STATUS_UPDATE_INTERVAL = 15
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SWAP = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}

# Hyper Tg Downloader
HELPER_TOKENS = ""

#Insta video downloader api
INSTADL_API = ""

# Media Search
IMDB_TEMPLATE = """<b>Title: </b> {title} [{year}]
<b>Also Known As:</b> {aka}
<b>Rating ⭐️:</b> <i>{rating}</i>
<b>Release Info: </b> <a href="{url_releaseinfo}">{release_date}</a>
<b>Genre: </b>{genres}
<b>IMDb URL:</b> {url}
<b>Language: </b>{languages}
<b>Country of Origin : </b> {countries}

<b>Story Line: </b><code>{plot}</code>

<a href="{url_cast}">Read More ...</a>"""

# Task Tools
FORCE_SUB_IDS = ""
MEDIA_STORE = True
DELETE_LINKS = False
CLEAN_LOG_MSG = False

# Limiters
BOT_MAX_TASKS = 0
USER_MAX_TASKS = 0
USER_TIME_INTERVAL = 0
VERIFY_TIMEOUT = 0
LOGIN_PASS = ""

# Bot Settings
BOT_PM = False
SET_COMMANDS = True
TIMEZONE = "Asia/Kolkata"

# GDrive Tools
GDRIVE_ID = ""
GD_DESP = "Uploaded with WZ Bot"
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# JDownloader
JD_EMAIL = ""
JD_PASS = ""

# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    }
]

# Update
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "master"
UPDATE_PKGS = False

# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
USER_TRANSMISSION = True
HYBRID_LEECH = True
LEECH_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
LEECH_CAPTION = ""
LEECH_DUMP_CHAT = ""
THUMBNAIL_LAYOUT = ""

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 0
WEB_PINCODE = True

# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0

# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]
