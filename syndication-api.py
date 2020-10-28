
if __name__ == '__main__':
    from settings import *
else:
    from .settings import *
import requests

class Syndication(object):

    def __init__(self):

        self.uri = 'https://wny.api.us.healtheintent.com/data-syndication/v1'
        self.headers =BEARER_HEADER

    def __send_request__(self, endpoint, method = None, headers = None, params=None):
        if method == 'GET':
            return requests.get('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint), headers=headers,
                                params=params).json()
        else:
            return requests.post('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint), headers=headers)

    def get_feeds(self):
        return self.__send_request__(endpoint='/feeds', method='GET', headers=self.headers)

    def get_channels(self):
        return self.__self_requsts__(endpoint='/channels')


if __name__ == '__main__':
    s = Syndication()
    print(s.get_feeds())
