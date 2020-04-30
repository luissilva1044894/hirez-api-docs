
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
import functools
import json
import os
import time

from boolify import boolify
from flask import Flask, jsonify, request, redirect, url_for, send_from_directory
from pyrez.enums.avatar_id import AvatarId

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
  app = Flask(kw.pop('name', __name__), static_folder=kw.pop('static_folder', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.assets')), **kw)#, static_url_path=kw.pop('static_folder', '')
  app.url_map.strict_slashes = not on_heroku()

  def requested_json(arg):
    return arg.headers.get('Content-Type', '').lower() == app.config.get('JSONIFY_MIMETYPE', '').lower() or hasattr(arg, 'args') and 'json' in arg.args.get('json', arg.args.get('format', '')).lower()

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
  @app.errorhandler(404)
  def root(error=None):
    return redirect(get_env('REDIRECT_URL'))

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

  def get_avatar_id(avatar_id, request):
    if 'avatar_id' in request.args and request.args['avatar_id']:
      return request.args['avatar_id']
    try:
      print(request.is_json)
      print(request.get_json())
    except:
      pass
    #if request.get_json().get('avatar_id'):
    #  return request.get_json()['avatar_id']
    return avatar_id

  #@app.route('/paladins/avatar/<int:avatar_id>/', strict_slashes=False)
  @app.route('/paladins/avatar/', defaults={'avatar_id': 0}, methods=['GET', 'POST'])
  @app.route('/paladins/avatar/<avatar_id>', methods=['GET', 'POST'])
  def legacy_images(avatar_id, game='paladins', folder='avatar'):
    path, _avatar_id = os.path.join(app.static_folder, game, folder), AvatarId(get_avatar_id(avatar_id, request))
    print(_avatar_id)
    for _ in os.listdir(path):
      if AvatarId(_.split('.', 1)[0]) == _avatar_id:
        if requested_json(request):
          f_path = os.path.join(path, _)
          return jsonify({
           'created_at': get_file_date(f_path, True),
           'format': _.split('.', 1)[-1],
           'id': int(_avatar_id),#_.split('.', 1)[0],
           'name': str(_avatar_id),
           'remote_path': url_for('static', filename=f'{game}/{folder}/{_}'),
           'updated_at': get_file_date(f_path),
           'url': url_for('static', filename=f'{game}/{folder}/{_}', _external=True)
          })
        if 'redirect' in request.args:
          return redirect(url_for('static', filename=f'{game}/{folder}/{_}', _external=True))
        return send_from_directory(path, _)

  return app

def main():
  create_app().run()

if __name__ == '__main__':
  main()
