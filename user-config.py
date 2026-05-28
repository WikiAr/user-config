"""
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/himo/user-config.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/sanaa/user-config.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/lyan/user-config.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/suha/user-config.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/nada/user-config.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/user-config.py -O /data/project/himowd/user-config.py -v
"""
import sys
import os
import json as _json
from pathlib import Path
# ---
family = 'wikipedia'
mylang = 'ar'
usernames['wikipedia']['ar'] = 'Mr.Ibrahembot'  # type: ignore # noqa: F821
usernames['wikidata']['www'] = 'Mr.Ibrahembot'  # type: ignore # noqa: F821

db_connect_file = user_home_path('replica.my.cnf')  # type: ignore # noqa: F821
password_file = None

_user_script_paths_file = Path("/data/project/himo/c9/users_paths.json")
user_script_paths = []
# ---
if _user_script_paths_file.exists():
    with open(_user_script_paths_file, 'r') as _f:
        user_script_paths = _json.load(_f)
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

from logging_config import setup_logging as _setup_logging  # type: ignore # noqa: E402

_bots = [
    "__main__",
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
    "bots_mv_all",
    "bots_src",
    "c18",
    "c18_new",
    "c30",
    "catsm",
    "catsn",
    "cite",
    "config",
    "copy_to",
    "core1.src",
    "cos",
    "cy",
    "d_30",
    "day19",
    "dbs",
    "dbs_not_yet",
    "des",
    "desc_dicts",
    "dump26",
    "dump27",
    "dump_files",
    "dump_lua",
    "fals",
    "fix_cs1",
    "fotball",
    "helps",
    "himo_api",
    "hrr4",
    "ill",
    "ill_add",
    "imgx",
    "info",
    "infobox",
    "jsons",
    "lex-examples",
    "likeapi",
    "ment",
    "mk_cats",
    "mk_cats_xx",
    "mkn",
    "mm2",
    "most",
    "mv_it",
    "mvafrica",
    "mw_api",
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
    "pr",
    "prop",
    "prop_labs",
    "prope",
    "qlever_dumps",
    "refgroups",
    "refn",
    "results",
    "rice4",
    "src",
    "rice3",
    "rice4",
    "src",
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
    "wikiapi",
]

for _bot in _bots:
    _setup_logging(name=_bot, level="INFO")
