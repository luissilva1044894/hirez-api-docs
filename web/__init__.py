
import os
from flask import Flask, jsonify, request, redirect, url_for

def create_app(*args, **kw):
	app = Flask(kw.pop('name', __name__), static_folder=kw.pop('static_folder', './../_assets'), static_url_path=kw.pop('static_folder', ''), **kw)

	@app.route('/', methods=['GET'])
	def root():
		return redirect('https://github.com/luissilva1044894/hirez-api-docs/blob/master/README.md')

	return app

def main():
  create_app().run()

if __name__ == '__main__':
  main()
