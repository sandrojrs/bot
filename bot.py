# Import Tweepy, credentials.py
from datetime import time

import tweepy
import json
import logging

from tweepy import Stream

consumer_key ='Qvuyn4Z7ItrCt7xMpgTPLMjlK'
consumer_secret ='QoyGHdXAZWFrdy1lRKv87O2BMMok0tiWdYuPVpgBTCtbdvCTDU'
access_token ='1250860147704057856-5FKiBocJsXdlALeZ2zxqipJFlGlTZf'
access_token_secret='XRyW4vnfNLhLjP6dqu7KybnGCIP2PkPMmVbbRvenIIL4j'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):

        tweet = json.loads(data)

        try:
            #api.retweet(tweet['id'])
            api.create_favorite(tweet['id'])
            print(tweet['user']['name'] + ' gostei do post!')
        except:
            print('Falha em retweetar ' + tweet['user']['name'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    stream = Stream(auth, l)
    stream.filter(track=['Bolsonaro2022'], languages=['pt'])
