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
usernames['wikipedia']['ar'] = 'Mr.Ibrahembot'
usernames['wikidata']['www'] = 'Mr.Ibrahembot'

db_connect_file = user_home_path('replica.my.cnf')
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
_ver_ = ''
# ---
try:
    from pywikibot.__metadata__ import __version__
    _ver_ = _blue_ % 'pywikibot VERSION' + ': ' + _red_ % __version__
except:
    pass
# ---
print(_blue_ % 'PYTHON VERSION' + ': ' + _red_ % _python_v, _ver_)
# ---

for _u_path in user_script_paths.copy():
    if os.path.exists(_u_path):
        sys.path.append(os.path.abspath(_u_path))
    else:
        print(f"user-config.py, path not exists:{_red_ % _u_path}")
        user_script_paths.remove(_u_path)

from logging_config import setup_logging as _setup_logging

_setup_logging(name="alabel")
_setup_logging(name="API")
_setup_logging(name="api_page")
_setup_logging(name="api_sql")
_setup_logging(name="artest")
_setup_logging(name="arwiki")
_setup_logging(name="asa")
_setup_logging(name="asa1")
_setup_logging(name="asapages")
_setup_logging(name="auths")
_setup_logging(name="b18_new")
_setup_logging(name="bots_helps")
_setup_logging(name="bots_mv_all")
_setup_logging(name="c18")
_setup_logging(name="c18_new")
_setup_logging(name="c30")
_setup_logging(name="catsm")
_setup_logging(name="catsn")
_setup_logging(name="cite")
_setup_logging(name="config")
_setup_logging(name="copy_to")
_setup_logging(name="cos")
_setup_logging(name="cy")
_setup_logging(name="d_30")
_setup_logging(name="day19")
_setup_logging(name="dbs")
_setup_logging(name="des")
_setup_logging(name="desc_dicts")
_setup_logging(name="dump26")
_setup_logging(name="dump27")
_setup_logging(name="dump_lua")
_setup_logging(name="fals")
_setup_logging(name="fix_cs1")
_setup_logging(name="fotball")
_setup_logging(name="helps")
_setup_logging(name="himo_api")
_setup_logging(name="ill")
_setup_logging(name="ill_add")
_setup_logging(name="infobox")
_setup_logging(name="likeapi")
_setup_logging(name="ment")
_setup_logging(name="mk_cats")
_setup_logging(name="mk_cats_xx")
_setup_logging(name="mkn")
_setup_logging(name="mm2")
_setup_logging(name="most")
_setup_logging(name="mv_it")
_setup_logging(name="nav")
_setup_logging(name="nep")
_setup_logging(name="neq")
_setup_logging(name="new_all")
_setup_logging(name="new_api")
_setup_logging(name="newapi")
_setup_logging(name="newtra")
_setup_logging(name="npa")
_setup_logging(name="people")
_setup_logging(name="petscan")
_setup_logging(name="portal")
_setup_logging(name="portalpages")
_setup_logging(name="prop")
_setup_logging(name="prop_labs")
_setup_logging(name="prope")
_setup_logging(name="qlever_dumps")
_setup_logging(name="refgroups")
_setup_logging(name="refn")
_setup_logging(name="rice3")
_setup_logging(name="stub")
_setup_logging(name="stub1")
_setup_logging(name="stub_files_bots")
_setup_logging(name="stub_tables")
_setup_logging(name="syria")
_setup_logging(name="temp")
_setup_logging(name="tempdata")
_setup_logging(name="templatecount")
_setup_logging(name="tests")
_setup_logging(name="textfiles")
_setup_logging(name="texts")
_setup_logging(name="to_load")
_setup_logging(name="tra")
_setup_logging(name="typos")
_setup_logging(name="utils")
_setup_logging(name="vvv")
_setup_logging(name="wd")
_setup_logging(name="wd_api")
_setup_logging(name="wd_api_new")
_setup_logging(name="wd_bots")
_setup_logging(name="wd_link")
_setup_logging(name="wd_utils")
_setup_logging(name="WDYe")
_setup_logging(name="wiki_api")
