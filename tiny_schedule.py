#!/usr/bin/env python3

import schedule
import time
import tiny_road
import twitter_post

schedule.every().day.at("09:00").do(twitter_post.main())

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
