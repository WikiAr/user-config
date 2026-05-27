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


_setup_logging(name="__main__")
_setup_logging(name="alabel")
_setup_logging(name="API")
_setup_logging(name="api_page")
_setup_logging(name="api_sql")
_setup_logging(name="arwiki")
_setup_logging(name="asa")
_setup_logging(name="asa1")
_setup_logging(name="asapages")
_setup_logging(name="auths")
_setup_logging(name="bots_helps")
_setup_logging(name="bots_mv_all")
_setup_logging(name="c18")
_setup_logging(name="c30")
_setup_logging(name="catsm")
_setup_logging(name="catsn")
_setup_logging(name="cite")
_setup_logging(name="copy_to")
_setup_logging(name="cos")
_setup_logging(name="cy")
_setup_logging(name="d_30")
_setup_logging(name="day19")
_setup_logging(name="dbs")
_setup_logging(name="dbs_not_yet")
_setup_logging(name="des")
_setup_logging(name="desc_dicts")
_setup_logging(name="dump26")
_setup_logging(name="dump27")
_setup_logging(name="dump_files")
_setup_logging(name="dump_lua")
_setup_logging(name="fals")
_setup_logging(name="fotball")
_setup_logging(name="himo_api")
_setup_logging(name="hrr4")
_setup_logging(name="ill")
_setup_logging(name="ill_add")
_setup_logging(name="imgx")
_setup_logging(name="info")
_setup_logging(name="infobox")
_setup_logging(name="jsons")
_setup_logging(name="lex-examples")
_setup_logging(name="likeapi")
_setup_logging(name="ment")
_setup_logging(name="mkn")
_setup_logging(name="most")
_setup_logging(name="mv_it")
_setup_logging(name="mvafrica")
_setup_logging(name="mw_api")
_setup_logging(name="nav")
_setup_logging(name="nep")
_setup_logging(name="neq")
_setup_logging(name="new_all")
_setup_logging(name="newapi", level="INFO")
_setup_logging(name="newtra")
_setup_logging(name="npa")
_setup_logging(name="people")
_setup_logging(name="petscan")
_setup_logging(name="portal")
_setup_logging(name="portalpages")
_setup_logging(name="pr")
_setup_logging(name="prop")
_setup_logging(name="prop_labs")
_setup_logging(name="prope")
_setup_logging(name="qlever_dumps")
_setup_logging(name="refgroups")
_setup_logging(name="refn")
_setup_logging(name="results")
_setup_logging(name="rice3")
_setup_logging(name="rice4")
_setup_logging(name="stub")
_setup_logging(name="stub1")
_setup_logging(name="stub_tables")
_setup_logging(name="tempdata")
_setup_logging(name="templatecount")
_setup_logging(name="textfiles")
_setup_logging(name="texts")
_setup_logging(name="to_load")
_setup_logging(name="tra")
_setup_logging(name="typos")
_setup_logging(name="wd")
_setup_logging(name="wd_api")
_setup_logging(name="wd_api_new")
_setup_logging(name="wd_link")
_setup_logging(name="wd_utils")
_setup_logging(name="WDYe")
_setup_logging(name="wikiapi")
_setup_logging(name="src")
_setup_logging(name="core1.src")
