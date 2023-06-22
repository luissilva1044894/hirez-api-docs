
from datetime import (
  datetime,
  timedelta,
  timezone,
)
from email.utils import format_datetime
import functools
import json
import os
from os import path
import time

from boolify import boolify
from flask import (
  Flask,
  jsonify,
  request,
  redirect,
  url_for,
  send_from_directory,
)
from pyrez.api import API
from pyrez.enumerations.Endpoint import Endpoint

import re
import unicodedata

from utils import (
  get_path,
  join_path,
  num_or_string,
  read_file,
  slugify,
)

HERE = os.path.dirname(os.path.abspath(__file__))
def get_value(request, field, default=None):
    if request.is_json:
      _ = request.get_json(force=True, silent=True, cache=True)
      if _ and field in _:
        return _[field]
    if hasattr(request, 'args') and field in request.args and request.args[field]:
      return request.args[field]
    return default

def get_avatar(avatar_id, path):
  if str(avatar_id).isnumeric():
    for _ in os.listdir(path):
      if _.split('.', 1)[0] == str(avatar_id):
        return send_from_directory(path, _)
  return get_avatar({'default': 0, 'origin': 9918, 'vip': 23203, 'striker': 23209, 'terminating': 23226,
    'corrupter': 23442, 'the-lost-hand': 23549, 'oni-mask': 23550, 'cutesy-maeve': 23552, 'cutesy-snek': 23553, 'cutesy-zhin': 23554, 'goodnight': 23555,
    'shadowblade': 23564, 'flametongue': 23661, 'snack-time': 23662, 'death-speaker': 23714, 'knightmare': 23715, 'day-walker': 23716, 'harbinger': 23717,
    'synth': 23924, 'nom-nom': 23925, 'cutesy-yeti': 24079, 'cutesy-lian': 24080, 'rowdy-corsair': 24081, 'winter-workout': 24088, 'shield-bearer': 24143,
    'the-king': 24164, 'poppy': 24165, 'greenwood-friend': 24166, 'white-knight': 24167, 'masterpiece': 24168, 'battle-rage': 24169, 'groverling': 24170,
    'forkasen-wanderer': 24171, 'kitten': 24172, 'tigron-thief': 24173, 'i-wuv-you': 24174, 'tepid-friendship': 24175, 'vulpin': 24176, 'dumpster-diver': 24177,
    'abyssal-vessel': 24178, 'the-returned': 24179, 'twilight-assassin': 24180, 'happy-huntress': 24181, 'the-blossom': 24182, 'mirror-mirror': 24183,
    'paladins-defense-force': 24202, 'imperial-magistrate': 24203, 'fire-and-ice': 24204, 'queen-of-hearts': 24350, 'futures-protector': 24354, 'squidly': 24355,
    'forlorn-future': 24356, 'dragon-queen': 24375, 'diamond-badge': 24393, 'gold-badge': 24394, 'blue-warrior': 24482, 'how-quaint': 24505, 'champions-are-eternal': 24597,
    'best-boy': 24611, 'summer-blossom': 24612, 'vanguard': 24669, 'bubbles': 24678, 'baby-steps': 24679, 'dragon-forged': 24680, 'dwarven-strength': 24681,
    'unrelenting': 24709, 'charming': 24758, 'sunset': 24759, 'lifesaver': 24760, 'beach-vibes': 24824, 'groovy-grover': 24887, 'grohk-rock': 24888, 'celebrity-io': 24889,
    'popstar-skye': 24890, 'greaser-lex': 24891, 'fallen-champion': 24892, 'reckoning': 24897, 'resolute': 24898, 'redbeard': 24969, 'bubbly': 24970, 'pirateer': 24972,
    'kitsune': 24973, 'blu': 25021, 'molly-the-shark': 25022, 'suave-saguaro': 25138, 'wanted-man': 25139, 'bandits-fury': 25140, 'smoked': 25141,
    'lenny-the-pirate': 25161, 'goddess-of-death': 25222, 'skadrin-ash': 25223, 'dark-monarch': 25224, 'soul-briar': 25225, 'mischievous': 25227, 'forest-protector': 25228, 'ice-box': 25229}.get(str(avatar_id).lower().replace(' ', '-').replace("'", ''), 0), path)

def get_env(name, _default=None, verbose=False):
  try:
    from dotenv import load_dotenv
  except ImportError:
    pass
  else:
    load_dotenv(verbose=verbose)
  finally:
    return os.getenv(name) or _default

def on_heroku():
  return 'heroku' in get_env('PYTHONHOME', '').lower() or boolify(get_env('ON_HEROKU'))

def create_app(*args, **kw):
  app = Flask(
    kw.pop('name', __name__),
    static_folder=kw.pop('static_folder', os.path.join(os.path.dirname(HERE), '.assets')),
    static_url_path=kw.pop('static_folder', ''),
    **kw
  )
  app.url_map.strict_slashes = not on_heroku()

  def requested_json(arg):
    return str(arg.headers.get('Content-Type', '')).lower() == str(app.config.get('JSONIFY_MIMETYPE', '')).lower() or hasattr(arg, 'accept_mimetypes') and arg.accept_mimetypes.accept_json and not arg.accept_mimetypes.accept_html or hasattr(arg, 'args') and 'json' in arg.args.get('json', arg.args.get('format', '')).lower()

  @app.after_request
  def jsonify_func(response):
    if requested_json(response):
      _indent_, separators = None, (',', ':')
      if request.args.get('format', 'json') in ['json_pretty', 'pretty'] or app.config['JSONIFY_PRETTYPRINT_REGULAR']:
        _indent_, separators = 2, (',', ': ')
      response.set_data(json.dumps(response.get_json(), sort_keys=app.config['JSON_SORT_KEYS'], ensure_ascii=app.config['JSON_AS_ASCII'], indent=_indent_, separators=(',', ':')))
      response.headers['Cache-Control'] = 'public, max-age=300'
      response.headers['Expires'] = format_datetime((datetime.utcnow() + timedelta(seconds=300)).replace(tzinfo=timezone.utc), usegmt=True)
    return response

  @app.route('/', methods=['GET'])
  #@app.errorhandler(404)
  def root(error=None):
    if not requested_json(request) and get_env('REDIRECT_URL'):
      return redirect(get_env('REDIRECT_URL'))
    def get_endpoint(n):
      if n.lower().startswith('realm'):
        return Endpoint.REALM_ROYALE
      if n.lower().startswith('smite'):
        return Endpoint.SMITE
      return Endpoint.PALADINS
    method, secret_key, params, endpoint = get_value(request, 'method'), get_value(request, 'secret_key'), get_value(request, 'params'), get_value(request, 'endpoint', 'paladins')
    if params and isinstance(params, str):
      params = params.split(',')
    api = API(get_env('PYREZ_DEV_ID'), get_env('PYREZ_AUTH_ID'), endpoint=get_endpoint(endpoint), storeSession=True)
    if not method or method.lower() in ['createsession', 'testsession', 'getdataused'] and not secret_key or secret_key and not secret_key == get_env('APP_SECRET_TOKEN'):
      return jsonify({})
    _r = api.makeRequest(method, params)
    if isinstance(_r, (dict, list)):
      return jsonify(_r)
    return jsonify({})

#api: smite
#method: createsession
#params: []

  @app.route('/assets')
  def list_assets():
    #return jsonify(os.listdir(os.path.join(app.static_folder)))#os.getcwd()
    def get_directory_structure(rootdir):
      """http://code.activestate.com/recipes/577879-create-a-nested-dictionary-from-oswalk/
      Creates a nested dictionary that represents the folder structure of rootdir"""
      __dir__ = {}
      rootdir = rootdir.rstrip(os.sep)
      start = rootdir.rfind(os.sep) + 1
      for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        parent = functools.reduce(dict.get, folders[:-1], __dir__)
        parent[folders[-1]] = dict.fromkeys(files)
      return __dir__
    if request.args.get('nested'):
      return jsonify(get_directory_structure(os.path.join(app.static_folder)))
    return jsonify({ p[p.rfind('.') - 1:].replace('\\', '/'): [f for f in files] for (p, dirs, files) in os.walk(os.path.join(app.static_folder))})

  def date_from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).isoformat()

  def get_file_date(path, t=None):
    if not t:
      #return time.ctime(os.path.getmtime(path))
      return date_from_timestamp(os.stat(path).st_mtime)
    return date_from_timestamp(os.stat(path).st_ctime)
    #time.ctime(os.path.getatime(path))

  #@app.route('/paladins/avatar/<int:avatar_id>/', strict_slashes=False)
  @app.route('/paladins/avatar/', defaults={'avatar_id': 0}, methods=['GET', 'POST'])
  @app.route('/paladins/avatar/<avatar_id>', methods=['GET', 'POST'])
  def legacy_images(avatar_id, game='paladins', folder='avatar'):
    path, _avatar_id, _avatars = os.path.join(app.static_folder, game, folder), get_value(request, 'avatar_id', avatar_id), read_file(join_path([get_path(root=True).replace('.web', ''), '.assets', 'paladins', 'avatar', 'avatars.json']))
    if not str(_avatar_id).isnumeric():
      _avatar_id = slugify(_avatar_id)
    _avatar_id = {**{slugify(_avatars[_]):num_or_string(_) for _ in _avatars}, **{str(num_or_string(_)):num_or_string(_) for _ in _avatars}}.get(str(_avatar_id), '0')
    _avatar_name = _avatars.get(str(_avatar_id))
    print(_avatar_id, _avatar_name)
    if boolify(get_env('OLD_SCRIPT')):
      if 'redirect' in request.args or 'link' in request.args.keys():
        for _ in os.listdir(path):
          if _.split('.', 1)[0] == str(avatar_id):
            """
            if 'link' in request.args.keys():
              #link' in request.args
              f_path = os.path.join(path, _)
              return jsonify({
               'created_at': get_file_date(f_path, True),
               'format': _.split('.', 1)[-1],
               'id': _.split('.', 1)[0],
               'name': _avatar_name,
               'path': f'{game}/avatar/{_}',
               'remote_path': url_for('static', filename=f'{game}/avatar/{_}'),
               'updated_at': get_file_date(f_path),
               'url': url_for('static', filename=f'{game}/avatar/{_}', _external=True)
              })
            """
          return redirect(url_for('static', filename=f'{game}/avatar/{_}', _external=True))#send_from_directory(path, _)
        #return send_from_directory(path, '0.png')
      return get_avatar(avatar_id, path)
    for _ in os.listdir(path):
      if _.split('.', 1)[0] == str(_avatar_id):
        """
        if requested_json(request):
          f_path = os.path.join(path, _)
          return jsonify({
           'format': _.split('.', 1)[-1],
           'id': int(_avatar_id),
           'name': _avatar_name,
           'path': f'{game}/{folder}/{int(_avatar_id)}',
           'remote_path': url_for('static', filename=f'{game}/{folder}/{_}'),
           'url': url_for('static', filename=f'{game}/{folder}/{_}', _external=True)
          })
        """
        if 'redirect' in request.args:
          return redirect(url_for('static', filename=f'{game}/{folder}/{_}', _external=True))
        return send_from_directory(path, _)

  @app.route('/<game>/<folder>/', defaults={'file': None}, methods=['GET'])
  @app.route('/<game>/<folder>/<file>', methods=['GET'])
  def cdn_(game, folder, file):
    p = path.join(app.static_folder, game, folder)
    if file is not None:
      f = file.rsplit('.', 1)
      if len(f) > 1:
        ext = f'{f[-1]}'
      elif '.' not in str(f):
        ext = '.jpg'
      f = f'{slugify(f[0])}{ext}'
    else:
      f = f'{slugify(file)}'
    if not path.isfile(path.join(p, f)):
      r = read_file(path.join(p, f'{folder}.json'))
      return jsonify(r or {}), 404
    return send_from_directory(p, f)
  return app

def main():
  create_app().run()

if __name__ == '__main__':
  main()
#/.assets/paladins/avatar/None

"""
import json
import requests

url = 'https://hirez-api-docs.herokuapp.com/paladins/avatar/25434'

r = requests.post(url, headers={'content-type': 'application/json'})
print(r.json())

r = requests.get(url, headers={'content-type': 'application/json'})
print(r.json())

r = requests.get(url, params={'avatar_id': '25434'}, headers={'content-type': 'application/json'})
print(r.json())

r = requests.get(url, data=json.dumps({'avatar_id': '25434'}), headers={'content-type': 'application/json'})
print(r.json())
"""
