from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import textwrap
import csv

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

search_term=input("Track something on twitter.\n")
filename=search_term+'.txt'

csvFile = open(filename, 'a')#a = ap[
csvWriter = csv.writer(csvFile)


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        d = json.loads(data)
        if not d['retweeted'] and 'RT @' not in d['text']:
           tweet=d['text'].encode("utf-8")
           tweet_date=d['created_at']
           print (tweet)
           csvWriter.writerow([tweet_date, tweet])
           return True
        else:
           tweet=d['text'].encode("utf-8")
           tweet_date=d['created_at']
           print (tweet)
           csvWriter.writerow([tweet_date, tweet,'rt'])
           return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=[search_term])