# This branch of the bot is dedicated to following back those who follow the bot.
# It won't follow you back right away, the function is only called once a minute, so it might take a second (or a minute hahahaha)

from config import *

import time

def follow_back():
        for follower in tweepy.Cursor(api.followers).items():
            follower.follow()

while True:
    follow_back()
    time.sleep (60)
