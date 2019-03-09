#!/usr/bin/env python3

import tweepy
import os

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : os.environ['TWITTER_API_KEY'],
    "consumer_secret"     : os.environ['TWITTER_API_KEY_SECRET'],
    "access_token"        : os.environ['TWITTER_ACCESS_TOKEN'],
    "access_token_secret" : os.environ['TWITTER_ACCESS_TOKEN_SECRET'] 
    }

  api = get_api(cfg)
  tweet = "Hello, world! Again!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
