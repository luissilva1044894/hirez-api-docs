
import os
from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__, static_folder='./../_assets', static_url_path='')

@app.route('/', methods=['GET'])
def root():
  return redirect('https://github.com/luissilva1044894/hirez-api-docs/blob/master/README.md')

def main():
  app.run()
if __name__ == '__main__':
  main()
