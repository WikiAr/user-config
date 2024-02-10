
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
    '/data/project/himo/core1/',
    '/data/project/himo/wd_core/',
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
if _python_v.startswith('311'):
    user_script_paths.append('./local/lib/python3.11/site-packages')
else:
    user_script_paths.append('./local/lib/python3.10/site-packages')


for _u_path in user_script_paths.copy():
    if os.path.exists(_u_path):
        sys.path.append(os.path.abspath(_u_path))
    else:
        print(f"user-config.py, path not exists:{_red_ % _u_path}")
        user_script_paths.remove(_u_path)
