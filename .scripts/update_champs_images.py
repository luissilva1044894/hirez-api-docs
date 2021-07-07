from PIL import Image

import os
from io import BytesIO, StringIO
from json.decoder import JSONDecodeError

import time
try:
  import httpx as requests
except ImportError:
  import requests
import urllib3
import io

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
  except OSError as e:
    print(f'Could not save {image_url} as an image. {e}')
  #else: print(f'Saved {image_url} - {image.format}, {image.mode}, {image.size}')
def save_champ_icon(name, id_):
  save_image(f'https://webcdn.hirezstudios.com/paladins/champion-icons/{name}.jpg', '.assets/paladins/characters', f'{id_}', 'jpg')#./../
def save_champ_header(name):
  save_image(f'https://webcdn.hirezstudios.com/paladins/champion-headers/{name}.png', '.assets/paladins/headers', fix_name(name), 'png')
  save_image(f'https://webcdn.hirezstudios.com/paladins/champion-headers/{name}/bkg.jpg', '.assets/paladins/headers', f'{fix_name(name)}-bkg', 'jpg')
def save_champ_carousel(name):
  save_image(f'https://webcdn.hirezstudios.com/paladins/assets/carousel/{fix_name(name)}.png', '.assets/paladins/carousels', fix_name(name), 'png')
def http_requests(url, method='GET', **kw):
  buffer = io.BytesIO()
  for n in range(kw.pop('max_tries', 5)):
    try:
      r = requests.get(url)
      return r.content
    except:
      time.sleep(n)
def fetch_all():
  for _ in  requests.get('https://cms.paladins.com/wp-json/api/champion-hub/1').json() or {}:
    #save_champ_icon(fix_name(_.get('feName')), _.get('id'))
    save_champ_header(fix_name(_.get('feName')))
    #save_champ_carousel(fix_name(_.get('feName'), False))

fetch_all()

if __name__ == 'main':
  fetch_all()
