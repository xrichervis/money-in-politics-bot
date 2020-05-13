# This branch of the bot contains the keys necessary to access the two APIs essential to running the @donations_bot:
# the Twitter API and the Center for Responsive Politics' (Open Secrets) API

import tweepy

# OpenSecrets' API key
crp_api_key = "XXX"

# Twitter API keys and tokens
ACCESS_TOKEN = "XXX"
ACCESS_TOKEN_SECRET = "XXX"
CONSUMER_KEY = "XXX"
CONSUMER_SECRET = "XXX"

# Twitter API authorization
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
