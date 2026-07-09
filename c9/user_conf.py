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
    "D:/marifa_new_repo/repo",
    'D:/hrr_25_repos',
    'D:/CatsOrg/',

    "I:/core/ARWIKI_ONE_REPO/src/asa_core",
    "I:/core/ARWIKI_ONE_REPO/src/core_cat",
    "I:/core/ARWIKI_ONE_REPO/src/core1",
    "I:/core/ARWIKI_ONE_REPO/src/new",
    "I:/core/ARWIKI_ONE_REPO/src/shared",
    "I:/core/ARWIKI_ONE_REPO/src/stub_bots",
    "I:/core/ARWIKI_ONE_REPO/src/wd_core",
    "I:/core/ARWIKI_ONE_REPO/src",
    'I:/BOTS_REPOS/mv_bots/src/',
    'I:/MD_TOOLS/mdwiki.toolforge.org/PYTHON_REPOS/',
    'I:/MD_TOOLS/mdwiki.toolforge.org/PYTHON_REPOS/pybot/src/',
    'I:/TOOLFORGE_TOOLS/ncc/',
    'I:/TOOLFORGE_TOOLS/ncc/nccbot/ncc_core/',
    'I:/TOOLFORGE_TOOLS/ncc/nccbot/',

    'I:/core/bots/',
    'I:/core/bots/ma/',
    'I:/core/bots/mo2/',
    'I:/core/bots/master2/src/',
]
# ---
this_dir = Path(__file__).parent
# ---
if str(this_dir).startswith("/mnt/") or str(this_dir).startswith("/data/"):
    _user_script_paths_file = Path("/data/project/himo/c9/users_paths.json")
    user_script_paths = [
        "/data/project/himo/ARWIKI_ONE_REPO/asa_core/",
        "/data/project/himo/ARWIKI_ONE_REPO/core_cat/",
        "/data/project/himo/ARWIKI_ONE_REPO/core1/",
        "/data/project/himo/ARWIKI_ONE_REPO/new/",
        "/data/project/himo/ARWIKI_ONE_REPO/stub_bots/",
        "/data/project/himo/ARWIKI_ONE_REPO/wd_core/",
        "/data/project/himo/ARWIKI_ONE_REPO/",
    ]
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
print(_blue_ % "PYTHON VERSION" + ": " + _red_ % _python_v)
# ---
for _u_path in user_script_paths.copy():
    if os.path.exists(_u_path):
        sys.path.append(os.path.abspath(_u_path))
    else:
        print(f"user_conf.py, path not exists:{_red_ % _u_path}")
        user_script_paths.remove(_u_path)


_bots = [
    "asa_core",
    "core1",
    "core_cat",
    "new",
    "logging_config",
    "shared",
    "stub_bots",
    "wd_core",
    "__main__",
    "API",
    "api_page",
    "api_sql",
    "arwiki",
    "asa",
    "asa1",
    "asapages",
    "auths",
    "bots_helps",
    "c18",
    "catsm",
    "catsn",
    "cite",
    "cos",
    "cy",
    "dbs",
    "des",
    "desc_dicts",
    "himo_api",
    "ill",
    "ill_add",
    "jsons",
    "likeapi",
    "mkn",
    "most",
    "nep",
    "neq",
    "new_all",
    "newapi",
    "people",
    "petscan",
    "portal",
    "portal_lists",
    "refn",
    "remove_today",
    "stub",
    "stub-logs",
    "stub1",
    "stub_tables",
    "textfiles",
    "to_load",
    "wd",
    "wd_api",
    "wd_link",
    "wd_utils",
    "c30",
    "bots_mv_all",
    "copy_to",
    "core1.src",
    "npa",
    "portalpages",
    "refgroups",
    "repo",
    "results",
    "rice3",
    "rice4",
    "src",
    "tempdata",
    "templatecount",
    "texts",
    "tra",
    "typos",
    "wd_api_new",
    "WDYe",
    "wikiapi",
]

for _bot in _bots:
    _setup_logging(name=_bot, level="INFO")
