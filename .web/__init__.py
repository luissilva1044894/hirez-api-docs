
import os
from flask import Flask, jsonify, request, redirect, url_for, send_from_directory

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
    'lenny-the-pirate': 25161}.get(str(avatar_id).lower().replace(' ', '-').replace("'", ''), 0), path)

def create_app(*args, **kw):
  app = Flask(kw.pop('name', __name__), static_folder=kw.pop('static_folder', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.assets')), **kw)#, static_url_path=kw.pop('static_folder', '')

  @app.route('/', methods=['GET'])
  @app.errorhandler(404)
  def root(error=None):
    return redirect('https://github.com/luissilva1044894/hirez-api-docs/blob/master/README.md')

  @app.route('/assets')
  def list_assets():
    #return jsonify(os.listdir(os.path.join(app.static_folder)))#os.getcwd()
    def get_directory_structure(rootdir):
      """http://code.activestate.com/recipes/577879-create-a-nested-dictionary-from-oswalk/
      Creates a nested dictionary that represents the folder structure of rootdir"""
      __dir__ = {}
      import functools
      rootdir = rootdir.rstrip(os.sep)
      start = rootdir.rfind(os.sep) + 1
      for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        parent = functools.reduce(dict.get, folders[:-1], __dir__)
        parent[folders[-1]] = dict.fromkeys(files)
      return __dir__
    if request.args.get('nested', None):
      return jsonify(get_directory_structure(os.path.join(app.static_folder)))
    return jsonify({ p[p.rfind('.') - 1:].replace('\\', '/'): [f for f in files] for (p, dirs, files) in os.walk(os.path.join(app.static_folder))})

  #@app.route('/paladins/avatar/<int:avatar_id>/', strict_slashes=False)
  @app.route('/paladins/avatar/', defaults={'avatar_id': 0}, strict_slashes=False, methods=['GET'])
  @app.route('/paladins/avatar/<avatar_id>', strict_slashes=False, methods=['GET'])
  def legacy_images(avatar_id, game='paladins'):
    path = os.path.join(app.static_folder, game, 'avatar')
    if request.args.get('redirect') or request.args.get('direct'):
      for _ in os.listdir(path):
        if _.split('.', 1)[0] == str(avatar_id):
          if request.args.get('redirect'):
            return redirect(url_for('static', filename=f'{game}/avatar/{_}', _external=True))
          return send_from_directory(path, _)
      return send_from_directory(path, '0.png')
    return get_avatar(avatar_id, path)

  return app

def main():
  create_app().run()

if __name__ == '__main__':
  main()
