import requests


class HabiticaUser:
    notifications = []

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.data = self.make_request('GET', 'user')

    def make_request(self, method, path, data=None, params=None):
        if data is None:
            data = {}
        if params is None:
            params = {}
        args = {
            'method': method,
            'url': 'https://habitica.com/api/v3/' + path,
            'headers': {
                'x-api-user': self.user_id,
                'x-api-key': self.token
            },
            'params': params,
            'json': data
        }
        response = requests.request(**args)
        if 'error' in response.json():
            if response.json()['error'] == 'NotAuthorized':
                raise self.NotAuthorized()
        if 'notifications' in response.json():
            self.notifications = response.json()['notifications']
        return response.json()['data']

    class NotAuthorized(Exception):
        def __init__(self, **kwargs):
            super(Exception, self).__init__()
