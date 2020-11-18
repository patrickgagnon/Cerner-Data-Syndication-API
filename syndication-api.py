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

    def __send_request__(self, endpoint, method = None, json = None, headers = None, params = None):
        if method == 'GET':
            return requests.get('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint), headers=headers,
                                params=params).json()
        else:
            return requests.get('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint), headers=headers,
                                    json=json)

    def get_feeds(self):
        return self.__send_request__(endpoint='/feeds', method='GET', headers=self.headers)

    def get_channels(self):
        return self.__send_request__(endpoint='/channels', method='GET', headers=self.headers)

    def get_channel_status(self, channel_id = None):
        return self.__send_request__(endpoint='/channels/{channel_id}'.format(channel_id=channel_id), method='GET',
                                     headers=self.headers)

    def get_channel_deliveries(self, channel_id = None):
        return self.__send_request__(endpoint='/channels/{channel_id}/deliveries'.format(channel_id=channel_id),
                                     method='GET', headers=self.headers)

    def get_channel_downloads(self, delivery_id = None, destination_path = None):
        response = self.__send_request__(endpoint='/downloads/{delivery_id}'.format(delivery_id=delivery_id), headers=self.headers)


        wd = os.getcwd()
        path = destination_path + '/' + dt.datetime.strftime(dt.datetime.today(), '%Y-%m-%d') + '.tar.gz'

        if response.status_code == 200:
            with open(path, 'wb') as i:
                i.write(response.content)
        i.close()

        temp = tarfile.open(name=path, mode='r:gz')
        os.chdir(destination_path)
        temp.extractall()
        temp.close()
        os.chdir(wd)

if __name__ == '__main__':
    s = Syndication()
    s.get_channel_downloads(delivery_id='217a4ee0-bb87-4877-a017-83880b5ee399',destination_path=TEST_PATH)

