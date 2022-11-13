#importing packages
from itertools import count
from xml.etree.ElementInclude import include
import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    #adding access keys and secret keys
    access_key="add key here"
    access_secret="add secret here"
    consumer_key="consumer key"
    consumer_secret="consumer secret"


    #auth for tweepy
    auth=tweepy.OAuthHandler(access_key,access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    #creating api object
    api=tweepy.API(auth)

    # extracting the twitter data
    tweets= api.user_timeline(screen_name="@elonmusk",count=200,include_rts=False,tweet_mode="extended" )

    #beautrifying json
    tweet_list=[]
    for i in tweets:
        text=i._json["full_text"]
        refined_tweet= {"user": i.user.screen_name,'text':text,'favorite_count':i.favorite_count, 'retweet_count':i.retweet_count, 'created_at': i.created_at}
        tweet_list.append(refined_tweet)

    df= pd.DataFrame(tweet_list)
    df.to_csv("elonlmusk_twitter_data.csv")
