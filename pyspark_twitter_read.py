
'''
downloaded as python file format from Jupyter notebook
run this at command line with python3 command

This script is for connectting to Twitter API thru the app registered in my Twitter developer account
use socket to create Streamlistener at localhost (127.0.0.1) and port 5555 (or 5556, etc) to read tweets 

'''

#!/usr/bin/env python
# coding: utf-8


#get_ipython().system('pip3 install tweepy')


import tweepy


# In[ ]:


from tweepy.auth import OAuthHandler


# In[ ]:


from tweepy import Stream


# In[ ]:


from tweepy.streaming import StreamListener


# In[ ]:


import socket


# In[ ]:


import json


# In[ ]:


# set up credentials from https://apps.twitter.com
consumer_key = 'lkOWgRaCuyCeuBPxHlRz1mpya'
consumer_secret = 'ZRI3DjxZ1AmDLSGkFerS9DcQ2gTjQg0r9XUf7A9r3Qj52RSz3U'
access_token = '1062388761928065024-lvNBaFOiU3LDMpePqUiJayHihbFo5E'
access_secret = 'cFAxCp6frybXx1mEwt7bVTBbRse21WxLa76Ku0nIslYGS'


# In[ ]:


class TweetsListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True

    def on_error(self, status):
        print(status)
        return True


# In[ ]:


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=['HongKong'])


# In[ ]:


if __name__ == "__main__":
    s = socket.socket()
    host = "127.0.0.1"
    port = 5556
    s.bind((host, port))

    print("listening on port: %s" % str(port))

    s.listen(5)
    c, addr = s.accept()

    print("Received request from: " + str(addr))

    sendData(c)


# In[ ]:
