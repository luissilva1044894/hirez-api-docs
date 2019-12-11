import requests
from PIL import Image

import os
from io import BytesIO, StringIO
from json.decoder import JSONDecodeError

def fix_name(name, lower=True):
  if lower: return str(name).lower().replace(' ', '-').replace("'", '').replace(',', '').replace('/', '-').replace('!', '')
  return str(name).replace(' ', '-').replace("'", '').replace(',', '').replace('/', '-').replace('!', '')
def save_image(image_url, folder, name, ext='png'):
  try:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder)
    if not os.path.exists(path):
      try: os.makedirs(path)
      except OSError as e: pass
    image = Image.open(BytesIO(http_requests(image_url)))
    path = f'{path}/{name}.{ext}'
    if not os.path.isfile(path):
      try:
        image.save(path, image.mode)# if image.mode.lower() in ['png', 'jpeg'] else 'PNG'
      except KeyError:
        image.save(path, 'PNG')
  except OSError:
    print(f'Could not save {image_url} as an image.')
  #else: print(f'Saved {image_url} - {image.format}, {image.mode}, {image.size}')
def save_champ_icon(name):
  save_image(f'https://web2.hirez.com/paladins/champion-icons/{name}.jpg', './../.assets/paladins/characters', fix_name(name), 'jpg')
def save_champ_header(name):
  save_image(f'https://web2.hirez.com/paladins/champion-headers/{name}.png', './../.assets/paladins/headers', fix_name(name), 'png')
  save_image(f'https://web2.hirez.com/paladins/champion-headers/{name}/bkg.jpg', './../.assets/paladins/headers', f'{fix_name(name)}-bkg', 'jpg')
def save_champ_carousel(name):
  save_image(f'https://web2.hirez.com/paladins/assets/Carousel/{name}.png', './../.assets/paladins/carousels', fix_name(name), 'png')
def http_requests(url, method='GET', **kw):
  import time
  import requests
  import urllib3
  import io
  buffer = io.BytesIO()
  for n in range(kw.pop('max_tries', 5)):
    try:
      r = requests.get(url)
      return r.content
    except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as exc:
      time.sleep(n)
def fetch_all():
  for _ in  requests.get('https://cms.paladins.com/wp-json/api/champion-hub/1').json() or {}:
    save_champ_icon(fix_name(_.get('feName')))
    save_champ_header(fix_name(_.get('feName')))
    save_champ_carousel(fix_name(_.get('feName'), False))

if __name__ == 'main':
  fetch_all()
