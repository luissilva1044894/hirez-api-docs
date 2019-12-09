template = """<details markdown="1">
<summary>Champions</summary>

There are currently {LEN} playable champions (Updated in {DATE}):
<table>
  <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Role</th>
    <th>Title</th>
    <th>Image</th>
  </tr>
  {CHAMPS}
  </table>
</details>"""
import requests
import sys
from datetime import datetime

def fix_name(o):
  return str(o).replace(' ', '-').replace("'", '').lower()
def create_value(_):
  return '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td><img src="https://web2.hirez.com/paladins/champion-icons/{}.jpg" height="64" width="64"/></td></tr>'.format(_.get('id'), _.get('feName'), _.get('role').split(' ', 1)[1].replace('er', ''), _.get('title'), fix_name(_.get('feName')))
_json_ = [f'{create_value(_)}' for _ in requests.get('https://cms.paladins.com/wp-json/api/champion-hub/1').json() or {} if _]
__ = template.format(CHAMPS='\n    '.join(_json_), LEN=str(len(_json_)), DATE=datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S'))
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

