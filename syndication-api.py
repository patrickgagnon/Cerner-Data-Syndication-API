from settings import *
import requests

class Syndication(object):

        def __init__(self):

            self.uri = 'https://wny.api.us.healtheintent.com/data-syndication/v1/'

        def __send_request__(self, params=None, method=None, postdata=None, json=None, headers=None):
            if method == 'GET':
                return requests.get().json()
            else:
