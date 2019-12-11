
import os
from flask import Flask, jsonify, request, redirect, url_for, send_from_directory

def create_app(*args, **kw):
  app = Flask(kw.pop('name', __name__), static_folder=kw.pop('static_folder', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.assets')), **kw)#, static_url_path=kw.pop('static_folder', '')

  @app.route('/', methods=['GET'])
  def root():
    return redirect('https://github.com/luissilva1044894/hirez-api-docs/blob/master/README.md')

  #@app.route('/paladins/avatar/<int:avatar_id>/', strict_slashes=False)
  @app.route('/paladins/avatar/', defaults={'avatar_id': 0}, strict_slashes=False)
  @app.route('/paladins/avatar/<avatar_id>', strict_slashes=False)
  def legacy_images(avatar_id, game='paladins'):
    path = os.path.join(app.static_folder, game, 'avatar')
    for _ in os.listdir(path):
      if _.split('.', 1)[0] == str(avatar_id):
        return redirect(url_for('static', filename=f'{game}/avatar/{_}'))#return send_from_directory(path, _)
    return send_from_directory(path, '0.png')

  return app

def main():
  create_app().run()

if __name__ == '__main__':
  main()
