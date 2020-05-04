
import os
import re
import unicodedata
import sys
import json

def slugify(value):
  """Normalizes string, converts to lowercase, removes non-alpha characters, and converts spaces to hyphens.
  From: http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python"""
  return (re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode('utf-8', 'ignore'))) or value).strip().replace(' ', '-').replace("'", '').lower()

def num_or_string(v, d=None):
  """Loads a value from MO into either an int or string value.
  String is returned if we can't turn it into an int.
  """
  try:
    return int(str(v))#.replace(',', '')
  except (ValueError, TypeError):
    try:
      _value = float(str(v).replace(',', '.'))
      if _value == 0:
        return 0
      return _value
    except (ValueError, TypeError):
      pass
  return d or v

def get_path(file=None, *args, **kw):
  file = kw.pop('file', file) or __file__
  if kw.pop('root_drive', None):
    path = sys.executable
    while os.path.split(path)[1]:
      path = os.path.split(path)[0]
    return path
  if kw.pop('root', None):
    return os.path.dirname(os.path.dirname(os.path.abspath(file)))
  if kw.pop('folder', None):
    return os.path.dirname(os.path.abspath(file))
  return os.path.abspath(file)

def open_if_exists(filename, mode='rb', encoding='utf-8'):
  """Returns a file descriptor for the filename if that file exists, otherwise ``None``."""
  if not os.path.isfile(filename) and (mode.rfind('r') != -1 or mode.rfind('a') != -1):
    return None
  try:
    import codecs
  except ImportError:
    try:
        return open(filename, mode=mode, encoding=encoding)
    except ValueError:
        return open(filename, mode=mode)#_io.BufferedReader
  else:
    return codecs.open(filename, mode)
'''
def join(params, separator=None):
  return (separator or '').join((str(_) for _ in params if _))
'''
def join_path(arr, relative_path=True):
  _j = ''
  if relative_path:
    _j = os.path.dirname(__file__).replace(__name__.split('.')[0], '')
  for _ in arr:
    _j = os.path.join(_j, str(_))
  return _j

def read_file(filename, mode='rb', **kw):
  """Loads a file"""
  is_json, silent = kw.pop('is_json', filename[-5:]=='.json'), kw.pop('silent', False)
  try:
    f = open_if_exists(filename, mode, encoding=kw.pop('encoding', 'utf-8'))
    if f:
      if is_json:
        try:
          with f:
            r = json.load(f, **kw)
            if not isinstance(r, dict) and isinstance(r, str):
              r = json.loads(r, **kw)
            return r
        except json.decoder.JSONDecodeError:
          if not silent:
            raise
        return {}
      if f.readable():
        return f.read()#lines
      return f
  except (FileNotFoundError, IsADirectoryError, IOError) as e:
    if not silent:
      raise
  return None
