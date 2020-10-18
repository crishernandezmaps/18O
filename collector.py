#!/usr/bin/env python3
import tweepy
from config import *
import csv
import unidecode
import time
import datetime
from datetime import timedelta
from timeloop import Timeloop
import bs4 as bs
import urllib.request

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

def get_hastag():
    source = urllib.request.urlopen('https://trends24.in/chile/')
    soup = bs.BeautifulSoup(source,'lxml')
    hashtag = soup.find("ol", {"class": "trend-card__list"}).find('li').find('a').text  
    print(hashtag)
    return  hashtag

tl = Timeloop()    
timer_seconds = 10

@tl.job(interval=timedelta(seconds=timer_seconds))
def get_media_inside_tweets():
    print("1s job current time : {}".format(time.ctime()))
    
    def get_media():
        if('media' in tweet.entities):
            for i in  tweet.extended_entities['media']:
                if(i['type'] == 'video'):
                    if(i['video_info']['variants'][0]['url'].split('?')[0].split('.')[-1] == 'm3u8'):
                        return i['video_info']['variants'][0]['url']
                    else:
                        return i['video_info']['variants'][0]['url'].split('?')[0]
                else:
                    pass

    # Open/Create a file to append data #
    d = str(datetime.datetime.now())
    name_of_temp_file = d.split('.')[0].split(' ')[0] + '_' + d.split('.')[0].split(' ')[1] + '.csv'

    csvFile = open(name_of_temp_file, 'a')
    csvWriter = csv.writer(csvFile)
    
    hashtag_to_find = '"[' + get_hastag() + ']"'  

    for tweet in tweepy.Cursor(api.search,q=hashtag_to_find,count=100,lang="es",since="2019-10-18",include_entities=True,tweet_mode="extended").items():
        user = tweet.user.screen_name
        timeStamp = tweet.created_at
        media = get_media()
        hashtag = get_hastag()

        # To check on terminal -visually- #
        tweet_object = {
            "user":user,
            "timeStamp":timeStamp,
            "media":media,
            "hashtag":hashtag
        }
        
        if(media):
            csvWriter.writerow([user,timeStamp,media,hashtag])  
            print(tweet_object)                    

if __name__ == "__main__":
    tl.start(block=True)   

"""
Possible changes:
- Modify hashtags
"""    