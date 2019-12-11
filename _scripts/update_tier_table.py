import sys
ranks = { 0: 'Unranked',
  1: 'Bronze V', 2: 'Bronze IV', 3: 'Bronze III', 4: 'Bronze II', 5: 'Bronze I',
  6: 'Silver V', 7: 'Silver IV', 8: 'Silver III', 9: 'Silver II', 10: 'Silver I',
  11: 'Gold V', 12: 'Gold IV', 13: 'Gold III', 14: 'Gold II', 15: 'Gold I',
  16: 'Platinum V', 17: 'Platinum IV', 18: 'Platinum III', 19: 'Platinum II', 20: 'Platinum I',
  21: 'Diamond V', 22: 'Diamond IV', 23: 'Diamond III', 24: 'Diamond II', 25: 'Diamond I',
  26: 'Master', 27: 'Grandmaster'
}

template = """Valid values:
<table>
  <tr>
    <th>ID</th>
    <th>Description</th>
    <th>Image</th>
  </tr>
  {TIERS}
</table>"""

__ = template.format(TIERS='\n    '.join([f'<tr><td>{_}</td><td>{ranks.get(_)}</td><td><img src="./../.assets/paladins/league-tier/{_}.png" height="32" width="32"/></td></tr>' for _ in range(28)]))
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

