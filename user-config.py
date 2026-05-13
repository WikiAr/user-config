"""


wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/himo/user-config.py
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/sanaa/user-config.py
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/lyan/user-config.py
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/suha/user-config.py
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/nada/user-config.py
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/himowd/user-config.py


"""
import sys
import os
# ---
family = 'wikipedia'
mylang = 'ar'
usernames['wikipedia']['ar'] = 'Mr.Ibrahembot'  # type: ignore # noqa: F821
usernames['wikidata']['www'] = 'Mr.Ibrahembot'  # type: ignore # noqa: F821

db_connect_file = user_home_path('replica.my.cnf')  # type: ignore # noqa: F821
password_file = None

user_script_paths = [
    '/data/project/himo/bots/asa_core/',
    '/data/project/himo/bots/cats_maker/',
    '/data/project/himo/bots/core1/',
    '/data/project/himo/bots/core_cat/',
    '/data/project/himo/bots/dump_core/',
    '/data/project/himo/bots/ma/',
    '/data/project/himo/bots/master2/',
    '/data/project/himo/bots/mv_bots/',
    '/data/project/himo/bots/new/',
    '/data/project/himo/bots/stub_bots/',
    '/data/project/himo/bots/wd_core/',
    '/data/project/himo/bots/',
]
# ---
_ver = sys.version_info[:3]
_python_v = str(_ver[0]) + str(_ver[1]) + str(_ver[2])
# ---
_red_ = "\033[91m%s\033[00m"
_blue_ = "\033[94m%s\033[00m"
# ---

# ---
try:
    from pywikibot.__metadata__ import __version__
    _ver_ = _blue_ % 'pywikibot VERSION' + ': ' + _red_ % __version__
except Exception:
    _ver_ = ''
# ---
print(_blue_ % 'PYTHON VERSION' + ': ' + _red_ % _python_v, _ver_)
# ---

for _u_path in user_script_paths.copy():
    if os.path.exists(_u_path):
        sys.path.append(os.path.abspath(_u_path))
    else:
        print(f"user-config.py, path not exists:{_red_ % _u_path}")
        user_script_paths.remove(_u_path)

from logging_config import setup_logging as _setup_logging  # noqa: E402

_bots = [
    "alabel",
    "API",
    "api_page",
    "api_sql",
    "artest",
    "arwiki",
    "asa",
    "asa1",
    "asapages",
    "auths",
    "b18_new",
    "bots_helps",
    "bots_src",
    "bots_mv_all",
    "c18",
    "c18_new",
    "c30",
    "catsm",
    "catsn",
    "cite",
    "config",
    "copy_to",
    "cos",
    "cy",
    "d_30",
    "day19",
    "dbs",
    "des",
    "desc_dicts",
    "dump26",
    "dump27",
    "dump_lua",
    "fals",
    "fix_cs1",
    "fotball",
    "helps",
    "himo_api",
    "ill",
    "ill_add",
    "infobox",
    "likeapi",
    "ment",
    "mk_cats",
    "mk_cats_xx",
    "mkn",
    "mm2",
    "most",
    "mv_it",
    "nav",
    "nep",
    "neq",
    "new_all",
    "new_api",
    "newapi",
    "newtra",
    "npa",
    "people",
    "petscan",
    "portal",
    "portalpages",
    "prop",
    "prop_labs",
    "prope",
    "qlever_dumps",
    "refgroups",
    "refn",
    "rice3",
    "stub",
    "stub1",
    "stub_files_bots",
    "stub_tables",
    "syria",
    "temp",
    "tempdata",
    "templatecount",
    "tests",
    "textfiles",
    "texts",
    "to_load",
    "tra",
    "typos",
    "utils",
    "vvv",
    "wd",
    "wd_api",
    "wd_api_new",
    "wd_bots",
    "wd_link",
    "wd_utils",
    "WDYe",
    "wiki_api",
]

for _bot in _bots:
    _setup_logging(name=_bot, level="INFO")
