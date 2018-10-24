import time
import tweepy
import csv
import datetime
currentTime = str(datetime.datetime.now().date())

####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

###StartTweepy login
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

##key in search terms
search_term=input("Track something on twitter.\n")
filename=search_term+'_search.txt'

# Open/Create a file to append data
csvFile = open(filename, 'a')#a = ap[
csvWriter = csv.writer(csvFile)
#Use csv Writer

def hashtags(tweet):
    i=0
    array_hashtag=[]
    while i < len(tweet.entities['hashtags']):
        array_hashtag.append(tweet.entities['hashtags'][i]['text'])
        i+=1
    return array_hashtag

def tweet_urls(tweet):
    i=0
    array_url=[]
    while i < len(tweet.entities['urls']):
        array_url.append(tweet.entities['urls'][i]['url'])
        i+=1
    return array_url


query=search_term

#for tweet in tweepy.Cursor(api.search,q=query,count=100,lang="en", result_type="recent",include_entities=True,since = currentTime).items():
#	print (tweet.created_at, tweet.text.encode("utf-8"))
#	csvWriter.writerow([tweet.created_at, tweet.text.encode("utf-8")])

for tweet in tweepy.Cursor(api.search,q=query,count=100,lang="en", result_type="recent",include_entities=True).items():
	#print (tweet.created_at, tweet.text.encode("utf-8"))
	print (tweet.created_at, tweet.text.encode('ascii', 'ignore'))
	i=0
	array_hashtag=''
	while i < len(tweet.entities['hashtags']):
		array_hashtag+=tweet.entities['hashtags'][i]['text']+','
		i+=1
		
	csvWriter.writerow(
	[
	tweet.id_str, 
	tweet.created_at, 
	tweet.user.screen_name.encode('ascii', 'ignore'),
	tweet.text.encode('ascii', 'ignore'),
	tweet.retweeted,
	tweet.lang,
	','.join(hashtags(tweet)),
	','.join(tweet_urls(tweet))
	]
	)
	


