#!/usr/bin/env python
# encoding: utf-8

from io import (
  BytesIO,
  StringIO,
  )
from json.decoder import JSONDecodeError
from os import (
  path,
  makedirs,
)
import time

try:
  import httpx as requests
except ImportError:
  import requests
from PIL import Image
import urllib3

PATH = path.join('..', '.assets', 'smite')
API_URL = 'https://cms.smitegame.com/wp-json/smite-api'
CDN_URL = 'https://webcdn.hirezstudios.com/smite'
CARDS_URL = f'{CDN_URL}/god-cards'
ICONS_URL = f'{CDN_URL}/god-icons'

fix_name = lambda name: str(name).lower().replace(' ', '-').replace("'", '').replace(',', '').replace('/', '-').replace('!', '')
get_path = lambda d: path.join(PATH, d)

def http_requests(url, **kw):
  buffer = BytesIO()
  max_retries = kw.pop('max_tries', 5)
  for n in range(max_retries):
    try:
      return requests.get(url)
    except:
      time.sleep(n)

def download_img(url):
  try:
    return Image.open(BytesIO(http_requests(url).content))
  except:
    pass

def make_dir(p):
  if not path.exists(p):
    try:
      makedirs(p)
    except OSError as e:
      pass

def save_img(image, folder, name, ext='png'):
  folder = get_path(folder)
  make_dir(folder)
  img_path = path.join(folder, f'{str(name).lower()}.{ext}')
  if image and not path.isfile(img_path):
    try:
      try:
        image.save(img_path, image.mode)
      except:
        image.save(img_path, 'PNG')
    except Exception as e:
      print(f'Could not save {img_path} as an image. {e}')
    else:
      print(f'Saving {img_path} - {image.format}, {image.mode}, {image.size}')

def god_card(name, god_id, ext='jpg'):
  save_img(download_img(f'{CARDS_URL}/{name}.{ext}'), 'cards', god_id, ext)

def god_icon(name, god_id, ext='jpg'):
  save_img(download_img(f'{ICONS_URL}/{name}.{ext}'), 'characters', god_id, ext)

def fetch_all(lang=(1,)):
  for l in lang:
    for c in  http_requests(f'{API_URL}/all-gods/{l}').json() or {}:
      god_name = fix_name(c.get('god_name_EN') or '')
      god_id = c.get('id') or 0
      if god_id and god_name:
        god_card(god_name, god_id)
        god_icon(god_name, god_id)

fetch_all()
