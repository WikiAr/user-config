"""
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/c9/user_conf.py -O /data/project/himo/c9/user_conf.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/c9/user_conf.py -O /data/project/sanaa/c9/user_conf.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/c9/user_conf.py -O /data/project/lyan/c9/user_conf.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/c9/user_conf.py -O /data/project/suha/c9/user_conf.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/c9/user_conf.py -O /data/project/nada/c9/user_conf.py -v
wget https://raw.githubusercontent.com/WikiAr/user-config/refs/heads/main/c9/user_conf.py -O /data/project/himowd/c9/user_conf.py -v
"""
import sys
import os
from pathlib import Path
import json as _json
from logger_config import setup_logging as _setup_logging  # type: ignore
# ---
from dotenv import load_dotenv
try:
    load_dotenv()
except Exception as e:
    print(e)
# ---
user_script_paths = [
    'D:/hrr_25_repos',
    'I:/core/bots/new/newapi_bot',
    'I:/core/bots/new/',
    # '/data/project/himo/bots/core1/',
    # '/data/project/himo/bots/wd_core/',
    'I:/core/bots/asa_core/src/',
    'I:/core/bots/mv_bots/src/',
    'I:/core/bots/new2/',
    'I:/core/bots/ma/',
    'I:/core/bots/stub_bots/src/',
    'I:/core/bots/core1/src/',
    'I:/core/bots/core_cat/src/',
    'I:/core/bots/mo2/',
    'I:/core/bots/dump_core/',
    'I:/core/bots/master2/src/',
    'I:/core/bots/wd_core/src/',
    'I:/mdwiki/',
    'I:/mdwiki/pybot/md_core/',
    'I:/mdwiki/pybot/md_core_helps/',
    'I:/mdwiki/pybot/td_core/',
    'I:/mdwiki/pybot/',
    'I:/ncc/',
    'I:/ncc/nccbot/ncc_core/',
    'I:/ncc/nccbot/',
    'I:/core/bots/',
    'D:/CatsOrg/',
]
# ---
this_dir = Path(__file__).parent
# ---
if str(this_dir).startswith("/mnt/") or str(this_dir).startswith("/data/"):
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
print(_blue_ % 'PYTHON VERSION' + ': ' + _red_ % _python_v)
# ---
for _u_path in user_script_paths.copy():
    if os.path.exists(_u_path):
        sys.path.append(os.path.abspath(_u_path))
    else:
        print(f"user_conf.py, path not exists:{_red_ % _u_path}")
        user_script_paths.remove(_u_path)

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
