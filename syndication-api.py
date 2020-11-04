
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

    def __send_request__(self, endpoint, method = None, json=None, headers = None, params=None):
        if method == 'GET':
            return requests.get('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint), headers=headers,
                                params=params)#.json()
        else:
            if json:
                return requests.post('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint), headers=headers,
                                     json=json)
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
        response=self.__send_request__(endpoint='/downloads/{delivery_id}'.format(delivery_id=delivery_id), method='GET', headers=self.headers)
        wd=os.getcwd()
        path= destination_path+dt.datetime.strftime(dt.datetime.today(), '%Y-%m-%d') +'.tar'


        with open(path, 'wb') as i:
            i.write(response.content)
            i.close()

        temp=tarfile.open(name=path, mode='r:gz')
        os.chdir(destination_path)
        temp.extractall()
        temp.close()
        os.chdir(wd)




if __name__ == '__main__':
    s = Syndication()
    s.get_channel_downloads('f92df8bc-021f-4f0e-b107-5edb89be5690', destination_path= 'C:/Users/PatrickGagnon/Documents/Python-Projects/Cerner-Data-Syndication-API/Test_Files/')
    #print(foo)
    #print(s.get_channels()
    #print(s.get_channel_deliveries(channel_id='83bec28a-b367-41c2-b468-7d8d6dd92f0c'))
