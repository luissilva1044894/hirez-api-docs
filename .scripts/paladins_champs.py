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

PATH = path.join('..', '.assets', 'paladins')
CDN_URL = 'https://webcdn.hirezstudios.com/paladins'
API_URL = 'https://cms.paladins.com/wp-json/api'
ABITILITIES_URL = f'{CDN_URL}/champion-abilities'
CAROUSELS_URL = f'{CDN_URL}/assets/carousel'
FRAMES_URL = f'{CDN_URL}/cards/frame'
HEADERS_URL = f'{CDN_URL}/champion-headers'
ICONS_URL = f'{CDN_URL}/champion-icons'
TALENTS_URL = f'{CDN_URL}/champion-legendaries-badge'

fix_name = lambda name: str(name).lower().replace(' ', '-').replace("'", '').replace(',', '').replace('/', '-').replace('!', '')
get_path = lambda d: path.join(PATH, d)

def http_requests(url, **kw):
  buffer = BytesIO()
  max_retries = kw.pop('max_tries', 5)
  for n in range(max_retries):
    try:
      r = requests.get(url)
      return r.content
    except:
      time.sleep(n)

def download_img(url):
  try:
    return Image.open(BytesIO(http_requests(url)))
  except:
    pass

def make_dir(p):
  if not path.exists(p):
    try:
      makedirs(p)
    except OSError as e:
      pass

def save_img(image, folder, name, ext='png'):
  if image:
    folder = get_path(folder)
    make_dir(folder)
    for n in name:
      img_path = path.join(folder, f'{str(n).lower()}.{ext}')
      try:
        try:
          image.save(img_path, image.mode)
        except:
          image.save(img_path, 'PNG')
      except Exception as e:
        print(f'Could not save {img_path} as an image. {e}')
      else:
        print(f'Saving {img_path} - {image.format}, {image.mode}, {image.size}')

def ability_icon(name, icon_id, ext='jpg'):
  save_img(download_img(f'{ABITILITIES_URL}/{name}.{ext}'), 'skills', (icon_id), ext)

def champ_carousel(name, champ_id, ext='png'):
  save_img(download_img(f'{CAROUSELS_URL}/{name}.{ext}'), 'carousels', (name, champ_id), ext)

def champ_header(name, champ_id, ext='png'):
  save_img(download_img(f'{HEADERS_URL}/{name}.{ext}'), 'headers', (name, champ_id), ext)
  champ_header_bkg(name, champ_id)

def champ_header_bkg(name, champ_id, ext='jpg'):
  save_img(download_img(f'{HEADERS_URL}/{name}/bkg.{ext}'), 'headers', (f'{name}-bkg', f'{champ_id}-bkg'), ext)

def champ_icon(name, champ_id, ext='jpg'):
  save_img(download_img(f'{ICONS_URL}/{name}.{ext}'), 'characters', (name, champ_id), ext)

def talent_icon(name, icon_id, ext='png'):
  save_img(download_img(f'{TALENTS_URL}/{name}.{ext}'), 'talents', (icon_id), ext)

def fetch_all(lang=(1,)):
  for l in lang:
    for c in  requests.get(f'{API_URL}/champion-hub/{l}').json() or {}:
      champ_name = fix_name(c.get('feName') or '')
      champ_id = c.get('id') or 0
      if champ_id and champ_name:
        champ_icon(champ_name, champ_id)
        champ_header(champ_name, champ_id)
        champ_carousel(champ_name, champ_id)

fetch_all()

if __name__ == 'main':
  fetch_all()
