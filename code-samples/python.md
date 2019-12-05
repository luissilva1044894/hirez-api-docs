
## Python

#### Requeriments:
* [Requests](https://pypi.org/project/requests) - Http Client

```python
import requests
from hashlib import md5
from datetime import datetime

class HiRezAPI:
  def __init__ (self, dev_id, auth_key, *args, **kw):
    self.auth_key = auth_key;
    self.dev_id = dev_id;
    self.endpoint = kw.pop('endpoint', 'http://api.paladins.com/paladinsapi.svc') 
    self.headers = kw.pop('headers', {})
    if 'user-agent' not in self.headers:
      from sys import version_info
      self.headers['user-agent'] = f'HiRezAPIWrapper [Python/{version_info.major}.{version_info.minor}]'

  def request(self, url, *args, **kw):
    r = requests.get(url=url, headers={**self.headers, **kw.pop('headers', {})}, *args, **kw)
    if r.headers.get('Content-Type', '').rfind('json') != -1:
      return r.json()
    return r.text

  def generate_signature(self, method, timestamp=None, *, encoding=None):
    return md5(f'{self.dev_id}{method.lower()}{self.auth_key}{timestamp or self.timestamp()}'.encode(encoding or 'utf-8')).hexdigest()

  def timestamp(self, _format=None):
    return datetime.utcnow().strftime(_format or '%Y%m%d%H%M%S')

  def create_session(self):
    r = self.request(f'{self.endpoint}/createsessionjson/{self.dev_id}/{self.generate_signature("createsession")}/{self.timestamp()}')
    if r.get('ret_msg', '').lower() == 'approved':
      self.session_id = r.get('session_id')

  def ping(self):
    return self.request(f'{self.endpoint}/pingjson')

  def test_session(self, session_id=None):
    return self.request(f'{self.endpoint}/testsessionjson/{self.dev_id}/{self.generate_signature("testsession")}/{session_id or self.session_id}/{self.timestamp()}')

  def data_used(self):
    return self.request(f'{self.endpoint}/getdatausedjson/{self.dev_id}/{self.generate_signature("getdataused")}/{self.session_id}/{self.timestamp()}')

  def server_status(self):
    return self.request(f'{self.endpoint}/gethirezserverstatusjson/{self.dev_id}/{self.generate_signature("gethirezserverstatus")}/{self.session_id}/{self.timestamp()}')

  def patch_info(self):
    return self.request (f'{self.endpoint}/getpatchinfojson/{self.dev_id}/{self.generate_signature("getpatchinfo")}/{self.session_id}/{self.timestamp()}')

hirez_api = HiRezAPI(dev_id=1004, auth_key='23DF3C7E9BD14D84BF892AD206B6755C')
hirez_api.create_session()
print(hirez_api.data_used())
print(hirez_api.server_status())
print(hirez_api.patch_info())
print(hirez_api.ping())
print(hirez_api.test_session())
```
