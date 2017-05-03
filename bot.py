#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import datetime

#enter the corresponding information from your Twitter application:
configfile = open("twitterconfig.txt").read().splitlines()

CONSUMER_KEY = configfile[0]#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = configfile[1]#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = configfile[2]#keep the quotes, replace this with your access token
ACCESS_SECRET = configfile[3]#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

error = True
while (error):
    error = False
    tweet = raw_input("What would you like to tweet\n")
    strdate = raw_input("enter date: (dd-mm-yyyy-hh-mm)\n")

    if len(tweet) > 140:
        print("ERROR: exceeding character tweet limit")
        print("Current charactercount: " + len(tweet))
        error = True
    date = datetime.datetime.strptime(strdate, "%d-%m-%Y-%H-%M")
    waittime = date - datetime.datetime.now()
    time.sleep(waittime.total_seconds())
    api.update_status(tweet)
