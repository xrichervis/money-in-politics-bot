This the <a href="https://twitter.com/donations_bot">Money in Politics bot</a>, a Twitter bot that reguarly tweets American campaign finance data. The bot was created using Python and <a href="https://github.com/robrem/opensecrets-crpapi/">Open Secret's own client library</a>. Its two primary functions are: 1) once a day, tweeting about the political contributions a single member of Congress receives (daily_thread.py), and 2) tweeting semi-regularly about larger trends in American campaign finance (scheduled.py). 

In order to make this Twitter bot run, you need Twitter API keys (config.py). You will also need to install: the Tweepy library, httplib2, and pause. 

This bot runs on Heroku. To deploy it there, you will need to install Git and the Heroku toolbelt. You'll need to include a Procfile with a worker module and a requirements.txt file.

Read more about the bot online at http://igor.gold.ac.uk/~xrich001/sandbox_cw3/money-in-politics-bot.html







