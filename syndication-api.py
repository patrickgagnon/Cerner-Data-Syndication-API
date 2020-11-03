
if __name__ == '__main__':
    from settings import *
else:
    from .settings import *
import requests
import tarfile
import datetime as dt
import os

class Syndication(object):

    def __init__(self):

        self.uri = 'https://wny.api.us.healtheintent.com/data-syndication/v1'
        self.headers = BEARER_HEADER
        self.channel_id = None
        self.feed_id = None

    def __send_request__(self, endpoint, method = None, headers = None, params=None):
        if method == 'GET':
            return requests.get('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint), headers=headers,
                                params=params).json()
        else:
            return requests.post('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint), headers=headers)

    def get_feeds(self):
        return self.__send_request__(endpoint='/feeds', method='GET', headers=self.headers)

    def get_channels(self):
        return self.__send_request__(endpoint='/channels', method='GET',headers=self.headers)

    def get_channel_status(self, channel_id=None):
        return self.__send_request__(endpoint='/channels/{channel_id}'.format(channel_id=channel_id), method='GET',headers=self.headers)

    def get_channel_deliveries(self, channel_id=None):
        return self.__send_request__(endpoint='/channels/{channel_id}/deliveries'.format(channel_id=channel_id), method='GET', headers=self.headers)

    def get_channel_downloads(self, delivery_id=None, destination_path=None):
        return self.__send_request__(endpoint='/downloads/{delivery_id}'.format(delivery_id=delivery_id), method='GET', headers=self.headers)
        #cd=os.getcwd()
        #temp=tarfile.open(name=destination_path, mode='r:gz')
        # if downloads.status_code == 200:
        #    with open(path, 'wb') as f:
        #        f.write(downloads.content)

if __name__ == '__main__':
    s = Syndication()
    #print(s.get_channels())
    #print(s.get_channel_status(channel_id='4b1d6d81-2067-41d9-bb19-f9e1f68da036'))
    #print(s.get_channel_status(channel_id='83bec28a-b367-41c2-b468-7d8d6dd92f0c'))
