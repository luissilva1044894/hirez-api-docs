template = """<details markdown="1">
<summary>Gods</summary>

There are currently {LEN} playable gods in the game (Updated in {DATE}):
<table>
  <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Role</th>
    <th>Title</th>
    <th>Image</th>
  </tr>
  {GODS}
  </table>
</details>
"""
try:
  import httpx as requests
except ImportError:
  import requests
import sys
from datetime import datetime

def fix_name(o):
  return str(o).replace(' ', '-').replace("'", '').lower()
def create_value(_):
  return '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td><img src="https://webcdn.hirezstudios.com/smite/god-icons/{}.jpg" height="64" width="64"/></td></tr>'.format(
    _.get('id'),
    _.get('god_name_EN'),
    _.get('role_EN')[1:] if str(_.get('role_EN'))[0] == ' ' else _.get('role_EN'),
    _.get('title'),
    fix_name(_.get("god_name_EN")),
  )
try:
  _json_ = [f'{create_value(_)}' for _ in sorted(requests.get('https://cms.smitegame.com/wp-json/smite-api/all-gods/1').json() or {}, key=lambda x: x.get('id')) if _]
except:
  _json_ = [f'{create_value(_)}' for _ in requests.get('https://cms.smitegame.com/wp-json/smite-api/all-gods/1').json() or {} if _]
__ = template.format(GODS='\n    '.join(_json_), LEN=str(len(_json_)), DATE=datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S'))
try:
  #https://stackoverflow.com/a/25476462
  from Tkinter import Tk
except ImportError:
  from tkinter import Tk
finally:
  r = Tk()
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(__)
  r.update()
  #r.destroy()
  sys.exit(0)

