import requests
import logging

try:
    import json
except ImportError:
    import simplejson as json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

host = 'http://www.guitarparty.com'
api_endpoint = '%s/api/v2' % host
port = 80
api_key = None


def deserialize(raw_data):
    data = json.loads(raw_data)
    if 'objects' in data.keys():
        return data['objects']
    else:
        return data


class Guitarparty(object):
    def __init__(self, api_key=None, host=None, port=None):
        _globals = globals()
        self.api_key = api_key or _globals['api_key']
        self.api_endpoint = api_endpoint or _globals['api_endpoint']
        self.port = port or _globals['port']

    def get_songbooks(self):
        url = '%s/songbooks/?api_key=%s' % (self.api_endpoint, self.api_key)
        r = requests.get(url)
        return deserialize(r.content)

    def create_songbook(self, title, description=None, is_public=False):
        url = '%s/songbooks/?api_key=%s' % (self.api_endpoint, self.api_key)
        data = {
            'title': title,
            'description': description,
            'is_public': is_public,
        }
        r = requests.post(url, data=json.dumps(data))
        return deserialize(r.content)

