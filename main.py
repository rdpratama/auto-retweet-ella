import tweepy as twitter
import config
import random
import time, datetime
import json

client = twitter.Client(bearer_token=config.BEARER_TOKEN ,consumer_key=config.API_KEY, consumer_secret=config.API_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)

screen_name = 'AM_EllaJKT48'

user_id = '1487291928257654785'

response = client.get_users_tweets(user_id, max_results='5)

# By default, only the ID and text fields of each Tweet will be returned
# for tweet in response.data:
#    print(tweet.id)
 #   print(tweet.text)


def retweet_ella(delay):
    print(f"\n{datetime.datetime.now()}\n")

    while True:
        for tweet in response.data:
            print(tweet.id)
            print(tweet.text)
            client.retweet(tweet.id)
        time.sleep(300)
retweet_ella(300)






