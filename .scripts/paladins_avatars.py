#!/usr/bin/env python
# encoding: utf-8

import os
from os.path import (
  abspath,
  dirname,
  join,
  isfile,
)
import json

import requests

enum_template = """
## Avatar Id - Paladins
> int

<details markdown="1">
<summary>Avatars</summary>

Valid values are:
<table>
  <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Image</th>
  </tr>
  [AVATARS]
</table>
</details>
"""

root_path = join('../', '../')
avatars_folder = join(root_path, '.assets', 'paladins', 'avatar')

def read_json(path, default={}):
  try:
    with open(path, 'r', encoding='utf-8') as f:
      return json.load(f) or default
  except (FileNotFoundError, ValueError):
    return default

def get_extension(n):
  if isfile(join(avatars_folder, f'{n}.png')):
    return 'png'
  if isfile(join(avatars_folder, f'./{n}.gif')):
    return 'gif'
  if isfile(join(avatars_folder, f'./{n}.jpg')):
    return 'jpg'

def create_value(k, v):
  return f'''
  <tr>
    <td>{k}</td>
    <td>{v}</td>
    <td><img src="./{k}.{get_extension(k)}" height="32" width="32"/></td>
  </tr>
  '''

def update(*args, **kw):
  if avatars := read_json(join(avatars_folder, 'avatars.json')):
    __ = enum_template.replace('[AVATARS]', ''.join([f'{create_value(a, avatars[a])}' for a in avatars]))
    try:
      with open(join(avatars_folder, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(__)
    except OSError as exc:
      print(exc)

if __name__ == '__main__':
  update()
